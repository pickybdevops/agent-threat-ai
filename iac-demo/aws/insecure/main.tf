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

# checkov:skip=CKV2_AWS_61: Learning demo bucket intentionally omits lifecycle policy
# checkov:skip=CKV2_AWS_62: Learning demo bucket intentionally omits event notifications
resource "aws_s3_bucket" "public_demo" {
  bucket = "agent-threat-ai-learning-demo-public-bucket"
}

# checkov:skip=CKV_AWS_53: Public ACL blocking intentionally disabled for learning
# checkov:skip=CKV_AWS_54: Public policy blocking intentionally disabled for learning
# checkov:skip=CKV_AWS_55: Ignore public ACLs intentionally disabled for learning
# checkov:skip=CKV_AWS_56: Restrict public buckets intentionally disabled for learning
resource "aws_s3_bucket_public_access_block" "public_demo" {
  bucket = aws_s3_bucket.public_demo.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# checkov:skip=CKV_AWS_24: Open SSH is intentional for Checkov learning
# checkov:skip=CKV_AWS_382: Open egress is intentional for Checkov learning
# checkov:skip=CKV2_AWS_5: SG is intentionally unattached in this isolated lab example
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
    description = "Open all outbound traffic - intentionally insecure for demo"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}