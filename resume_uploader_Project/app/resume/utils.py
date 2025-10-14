from operator import mul
import uuid
from warnings import deprecated
import boto3.session
from fastapi import UploadFile, HTTPException, status
import os
from pathlib import Path
from decouple import config
import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from botocore.client import Config

MINIO_ROOT_USER = config("MINIO_ROOT_USER")
MINIO_ROOT_PASSWORD = config("MINIO_ROOT_PASSWORD")
MINIO_BUCKET = config("MINIO_BUCKET")
MINIO_ENDPOINT = "http://minio:9000"  # For container-to-container communication
MINIO_PUBLIC_URL = "http://localhost:9000"  # For browser access

# Client for internal operations (uploads)
session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ROOT_USER,
    aws_secret_access_key=MINIO_ROOT_PASSWORD,
    config=Config(signature_version="s3v4", s3={"addressing_style": "path"}),
    region_name='us-east-1'
)

# Separate client for generating public URLs
s3_client_public = session.client(
    service_name='s3',
    endpoint_url=MINIO_PUBLIC_URL,  # Use localhost for presigned URLs
    aws_access_key_id=MINIO_ROOT_USER,
    aws_secret_access_key=MINIO_ROOT_PASSWORD,
    config=Config(signature_version="s3v4", s3={"addressing_style": "path"}),
    region_name='us-east-1'
)

TRANSFER_CONFIG = TransferConfig(
    multipart_threshold=5 * 1024 * 1024,
    multipart_chunksize=5 * 1024 * 1024,
    max_concurrency=4,
    use_threads=True
)

async def save_upload_file_on_minio(upload_file: UploadFile, sub_dir: str) -> str:
    try:
        allow_types = ["image/jpeg", "image/jpg", "image/png", "application/pdf"]
        if upload_file.content_type not in allow_types:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                detail="Invalid file type"
            )
        
        file_size = upload_file.size
        if file_size is None:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="Could not determine file size"
            )
        if file_size > 10 * 1024 * 1024:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="File size too large"
            )
        
        await upload_file.seek(0)
        
        file_extension = Path(upload_file.filename).suffix
        file_name = f"{uuid.uuid4().hex}{file_extension}"
        file_path = str((Path(sub_dir) / file_name))
        
        # Use internal client for uploads
        s3_client.upload_fileobj(
            Fileobj=upload_file.file,
            Bucket=MINIO_BUCKET,
            Key=str(file_path),
            ExtraArgs={'ACL': 'public-read', 'ContentType': upload_file.content_type},
            Config=TRANSFER_CONFIG
        )
        return file_path
        
    except ClientError as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to upload file to MinIO: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Upload Error: {str(e)}"
        )


def get_file_url(file_path: str) -> str:
    # Use public client to generate presigned URLs with localhost
    presigned: str = s3_client_public.generate_presigned_url(
        "get_object",
        Params={"Bucket": MINIO_BUCKET, "Key": file_path},
        ExpiresIn=(7 * 24 * 60 * 60)  # 7 days
    )
    return presigned  # No need to replace anymore!
async def save_upload_file(abc, bcd):
    return "Mai pagal hu"