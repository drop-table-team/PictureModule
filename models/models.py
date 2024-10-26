from fastapi import UploadFile
from pydantic import BaseModel


class BackendResponse(BaseModel):
    title: str
    tags: list[str]
    summary: str
    originalFile: UploadFile

