from fastapi import APIRouter, UploadFile, Depends
from fastapi.openapi.models import APIKey

from source.ai import convert_image_ollama

import api.auth as auth

router = APIRouter()

@router.post("/convertImage")
async def convert_image(file: UploadFile, api_key: APIKey = Depends(auth.get_api_key)):
    return convert_image_ollama(file.file)