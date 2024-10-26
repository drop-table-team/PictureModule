from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN

from api.config import Settings, get_settings

api_key_header = APIKeyHeader(name="access_token", auto_error=False)

async def get_api_key(settings: Settings = Depends(get_settings), input_api_key_header: str = Security(api_key_header)):
    if input_api_key_header == settings.API_KEY:
        return input_api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )