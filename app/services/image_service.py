from uuid import uuid4
from app.integrations import upload_file

async def save_image(file):
    content = await file.read()
    image_id = str(uuid4())
    object_name = f"{image_id}.jpg"

    url = upload_file(content, object_name)

    return image_id, url, content