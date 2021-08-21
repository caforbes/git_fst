import os
import re

from .lexicon import Lexicon


class BuilderError(Exception):
    pass


class FomaBuilder:
    """ Uses a configuration dictionary to locate components of lexc files and foma rules;
        Then splits and copies these files, writing to a single .foma file at a specified location.
    """

    def __init__(self, config: dict) -> None:
        self._validate_config_file(config)
        self.config = config
        self._set_directory()

    def build(self) -> None:
        """ Builds lexc/foma files as specified with config settings from input dict.
            Writes both files to foma/ inside specified directory from config file.
            If no dir specified, writes to ../fst/foma
        """
        target_path = os.path.join(self.config['dir'], 'foma')
        if not os.path.exists(target_path):
            os.mkdir(target_path)

        self._build_lexc()
        self._build_foma()

    def lexc_filepath(self) -> str:
        return os.path.join(self.config['dir'], 'foma', self.config['name'] + '.txt')

    def foma_filepath(self) -> str:
        return os.path.join(self.config['dir'], 'foma', self.config['name'] + '.foma')

    def fomabin_filepath(self) -> str:
        return os.path.join(self.config['dir'], 'foma', self.config['name'] + '.fomabin')

    def _build_lexc(self) -> None:
        """ Calls the processing commands and writes the lexc info to file.
        """
        self._build_dictionary()
        self._build_morph_description()

        with open(self.lexc_filepath(), 'w') as f:
            f.write(self._multichar_symbs)
            f.write(self._stems)
            f.write(self._morphotactics + '\n')

    def _build_dictionary(self) -> None:
        self._stems = Lexicon(self.config).as_lexc_str()

    def _build_morph_description(self) -> None:
        '''
        Builds a lexc file from all specified files in lexc directory.
        File has three chunks: multicharacter symbols, stems, morphotactic descriptions.
        '''

        multichar_symbs = ''
        morphotactics = []

        # read/process files in lexc directory
        for file in self.config['lexc_files']:
            with open(os.path.join(self.config['dir'], file)) as f:
                content = f.read()

            # split multichar symbols from morphotactic description
            chunks = content.split('\n\n', 1)
            header = chunks[0]
            if '\n' in header:
                multichar_symbs += header.split('\n', 1)[1] + '\n'
            morphotactics.append(chunks[1])
            
        self._morphotactics = '\n\n'.join(morphotactics)

        # clean up the multicharacter symbols
        self._build_multichars(multichar_symbs)

    def _build_multichars(self, text) -> None:
        '''
        Input a chunk of text with a collection of multicharacter symbols for foma on newlines.
        Outputs all unique symbols, sorted and alphabetized with neat header/footer.
        '''
        symbols = text.split('\n')
        symbols = sorted(set(symbols) - set(['']))
        new_text = '\n'.join(symbols)

        self._multichar_symbs = 'Multichar_Symbols\n' + new_text + '\n\n'

    def _build_foma(self) -> None:
        """ Calls processing commands and arranges header/footer for foma file.
            Writes foma file to "specified_directory/foma/name.foma"
            Lists bin file as "specified_directory/foma/name.fomabin"
        """
        self._build_rules()

        header = "read lexc {}\ndefine Lexicon ;".format(self.lexc_filepath())
        footer = "save stack {}".format(self.fomabin_filepath())

        with open(self.foma_filepath(), 'w') as f:
            f.write(header + '\n\n')
            f.write(self._rules + '\n\n')
            f.write(footer)

    def _build_rules(self) -> None:
        '''
        Reads rules files, removes stem variation section unless dialect_variation
        parameter in the config dictionary set to True.
        '''

        self._rules = ''
        for file in self.config['rules_files']:
            with open(os.path.join(self.config['dir'], file)) as f:
                self._rules += f.read()

        if not self.config.get('dialect_variation'):
            lines = self._rules.splitlines()
            valid_lines = []
            delete_toggle = False
            for line in lines:
                if re.search(r'! (end )?stem variation', line):
                    delete_toggle = not delete_toggle
                    continue
                if delete_toggle:
                    continue
                valid_lines.append(line)
            self._rules = '\n'.join(valid_lines)

    @staticmethod
    def _validate_config_file(config) -> None:
        required_keys = ['name', 'lexc_files', 'rules_files']
        for key in required_keys:
            if not config.get(key):
                raise BuilderError('Key {} not found in config file')

    def _set_directory(self) -> None:
        if not self.config.get('dir'):
            if self.config.get('test'):
                dir = os.path.join(
                    os.path.dirname(__file__), '../test/fixtures')
            else:
                dir = os.path.join(os.path.dirname(__file__), '../fst')
            self.config['dir'] = os.path.abspath(dir)
