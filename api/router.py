import json
import os

import aiohttp
from fastapi import APIRouter, UploadFile, HTTPException

from source.ai import convert_image_ollama
BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")
router = APIRouter()

@router.post("/input")
async def convert_image(file: UploadFile):
    output = convert_image_ollama(file.file)

    output["short"] = output.pop("summary")
    output["transcription"] = output.pop("description")

    backend_url = f"{BACKEND_BASE_URL}/modules/input"

    # Send multipart request to backend
    async with aiohttp.ClientSession() as session:
        form = aiohttp.FormData()
        form.add_field(
            "json", json.dumps(output), content_type="application/json"
        )
        await file.seek(0)
        form.add_field(
            "file",
            await file.read(),
            filename=file.filename,
            content_type=file.content_type,
        )

        async with session.post(backend_url, data=form) as response:
            if response.status >= 400:
                raise HTTPException(
                    status_code=response.status,
                    detail=f"Backend service error: {await response.text()}",
                )

    return output
