# Learning Block 2: Container image used only for CI security scanning demonstration.
#
# Why this file exists:
# - Trivy scans built container images for OS/package vulnerabilities and misconfigurations.
# - We keep it simple so you can inspect it line by line.
# - The application still runs locally with `python main.py`; this Dockerfile is mainly for pipeline learning.
#
# Note: we intentionally use a general Python base image instead of an aggressively minimized image so Trivy
# has something realistic to inspect. In production you would usually prefer a smaller hardened base image.
FROM python:3.11

# Set a predictable working directory inside the image.
WORKDIR /app

# Copy dependency manifest first for better Docker layer caching.
COPY requirements.txt ./

# Install application dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code into the image.
COPY . .

# Expose the Flask demonstration port used by vuln-test/vuln-test.py if you run it manually.
EXPOSE 5000

# Default command for local image execution.
CMD ["python", "main.py"]
