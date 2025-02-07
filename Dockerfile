# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# Install foma package
RUN apt update && apt install -y foma && rm -rf /var/lib/apt/lists/*

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to Pipfile data to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
--mount=type=bind,source=Pipfile,target=Pipfile \
--mount=type=bind,source=Pipfile.lock,target=Pipfile.lock \
python -m pip install pipenv && pipenv install
        
COPY . .
ENV PYTHONSTARTUP=.pythonstartup

# USER appuser
CMD ["python"]