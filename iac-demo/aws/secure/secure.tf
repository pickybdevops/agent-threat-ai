terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "secure_demo" {
  bucket = "agent-threat-ai-learning-demo-secure-bucket"
}

resource "aws_s3_bucket_versioning" "secure_demo" {
  bucket = aws_s3_bucket.secure_demo.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "secure_demo" {
  bucket = aws_s3_bucket.secure_demo.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "secure_demo" {
  bucket = aws_s3_bucket.secure_demo.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_lifecycle_configuration" "secure_demo" {
  bucket = aws_s3_bucket.secure_demo.id

  rule {
    id     = "expire-old-objects"
    status = "Enabled"

    expiration {
      days = 30
    }
  }
}

resource "aws_s3_bucket_notification" "secure_demo" {
  bucket = aws_s3_bucket.secure_demo.id
  # In real production this would reference SNS, SQS, or Lambda.
  # Left intentionally minimal for learning.
}

resource "aws_security_group" "secure_demo_sg" {
  name        = "agent-threat-ai-demo-secure-sg"
  description = "Restricted SG for Checkov learning"

  ingress {
    description = "SSH only from internal corporate CIDR"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    description = "HTTPS egress only to internal CIDR for demo"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  tags = {
    Name = "agent-threat-ai-demo-secure-sg"
  }
}