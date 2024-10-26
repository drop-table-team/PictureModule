from fastapi import APIRouter, UploadFile, Depends
from fastapi.openapi.models import APIKey

from models.models import BackendResponse
from source.ai import loader_test_unstructured, convert_image_ollama

import api.auth as auth

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@router.get("/testUnstructured")
async def test_unstructured():
    return {"message": loader_test_unstructured()}

@router.get("/testOllama")
async def test_ollama():
    return {"message": f"{convert_image_ollama()}"}

@router.post("/convertImage")
async def convert_image(file: UploadFile, api_key: APIKey = Depends(auth.get_api_key)):

    #return BackendResponse(
    #    title="test",
    #    tags=["tag1", "tag2"],
    #    summary="summary",
    #    original_file=file
    #)
    return convert_image_ollama(file.file)