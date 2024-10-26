from fastapi import APIRouter, UploadFile, Depends
from fastapi.openapi.models import APIKey

from api.config import Settings
from source.ai import convert_image_ollama

import api.auth as auth
from config import Settings, get_settings
import requests

router = APIRouter()

@router.post("/convertImage")
async def convert_image(file: UploadFile, api_key: APIKey = Depends(auth.get_api_key)):
    output = convert_image_ollama(file.file)

    settings = get_settings()

    requests.post(f"{settings.BACKEND_BASE_URL}/modules/input", json=output, files={"file":file})

    return output