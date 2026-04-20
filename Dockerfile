# Learning Block 2: container image for CI security scanning demonstration.
#
# Why this version is better:
# - Uses a slimmer Python base image to reduce OS package count
# - Reduces attack surface and usually lowers Trivy findings
# - Keeps the file simple enough for learning and interviews
#
# In production, you would also consider:
# - pinning the base image by digest
# - multi-stage builds
# - regularly rebuilding from patched base images
FROM python:3.11-slim

# Keep Python output predictable in containers.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory.
WORKDIR /app

# Copy dependency manifest first for better layer caching.
COPY requirements.txt ./

# Upgrade pip and install dependencies without cache.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source.
COPY . .

# Expose demo Flask port if run manually.
EXPOSE 5000

# Default command.
CMD ["python", "main.py"]