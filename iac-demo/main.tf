# Learning Block 2: Intentionally insecure Terraform example for Checkov.
#
# Why this file exists:
# - Checkov scans Infrastructure as Code for misconfigurations.
# - This file is NOT meant to be deployed.
# - It exists so you can see how a CI pipeline flags bad cloud security patterns.
#
# Expected examples of findings from security scanners:
# - Public S3 bucket exposure
# - Missing bucket encryption
# - Missing versioning
# - Overly permissive security group ingress

terraform {
  required_version = ">= 1.5.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "public_demo" {
  bucket = "agent-threat-ai-learning-demo-public-bucket"
}

resource "aws_s3_bucket_public_access_block" "public_demo" {
  bucket = aws_s3_bucket.public_demo.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_security_group" "demo_open_sg" {
  name        = "agent-threat-ai-demo-open-sg"
  description = "Intentionally insecure SG for Checkov learning"

  ingress {
    description = "Open SSH to the world - intentionally insecure for demo"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
