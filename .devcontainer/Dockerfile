# FROM python:3.12-slim

# # Install required OS packages
# RUN apt-get update && apt-get install -y curl ca-certificates git && rm -rf /var/lib/apt/lists/*

# # Create a non-root user 'vscode'
# # RUN useradd -ms /bin/bash vscode

# # Download the latest installer
# ADD https://astral.sh/uv/install.sh /uv-installer.sh

# # Run the installer then remove it
# RUN sh /uv-installer.sh && rm /uv-installer.sh

# # Ensure the installed binary is on the `PATH`
# ENV PATH="/root/.local/bin/:$PATH"

# WORKDIR /workspace

# # Copy the project files (if not using a volume mount)
# COPY . /workspace


ARG UV_VERSION=latest
ARG DEBIAN_VERSION=bookworm


FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv


FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VERSION
LABEL maintainer="a5chin <a5chin.origin+contact@gmain.com>"

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # For OpenCV etc...
    libgl1 libglib2.0-0 \
    # To remove the image size, it is recommended refresh the package cache as follows
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=uv --chown=vscode: /uv /uvx /bin/