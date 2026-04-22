import json
import urllib3
from minio import Minio
from io import BytesIO
from app.core.config import settings
from datetime import timedelta
from app.schemas.ingredient import ImageObject

client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_ENDPOINT_SECURE,
    http_client=urllib3.PoolManager(timeout=urllib3.Timeout(connect=5, read=10)),
)


def ensure_bucket(bucket_name: str):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*",
            }],
        }
        client.set_bucket_policy(bucket_name, json.dumps(policy))

def upload_file(file_bytes, object_name, content_type="image/jpeg") -> ImageObject:
    client.put_object(
        settings.MINIO_BUCKET,
        object_name,
        BytesIO(file_bytes),
        length=len(file_bytes),
        content_type=content_type,
    )

    if settings.MINIO_IS_PUBLIC_BUCKET:
        presigned_url =  f"https://{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET}/{object_name}"
    else:
        presigned_url = client.presigned_get_object(
            settings.MINIO_BUCKET,
            object_name,
            expires=timedelta(days=settings.MINIO_PRESIGNED_URL_EXPIRY_DAYS),
        )
    return ImageObject(
        image_name=object_name,
        presigned_url=presigned_url,
        bucket_name=settings.MINIO_BUCKET
    )
