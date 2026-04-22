import httpx
from typing import Optional

from app.core.config import settings

async def detect_ingredients_from_image(image_url: str, lang: Optional[str] = "en") -> str:
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Extract all ingredient foods from this image thoroughly. "
                        "Don't need to give any explanation, just provide the extracted list, separated by comma."
                        f"Response in language {lang}"
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            ]
        }
    ]

    payload = {
        "model": "google/gemma-3-12b-it:free",
        "messages": messages
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            settings.OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload
        )

    data = response.json()

    return (
        data.get("choices", [{}])[0]
        .get("message", {})
        .get("content", "")
    )