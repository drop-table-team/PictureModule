# PictureModule
Provides a Module to convert pictures to text.

## Input:
- A picture (preferred png or jpg) through the api endpoint ("/input")

## Output:
- Backend POST request with the extracted text of the picture
    - Extracted infos are: title, tags, short summary, transcription
    - Also sends original file to the backend
- Endpoint returns only extracted text if successful

# Env Variables

|Variable| Description                                                                                   |
|--------|-----------------------------------------------------------------------------------------------|
|`OLLAMA_BASE_URL`| URL of the OLLAMA instance                                                                    |
|`OLLAMA_MODEL`| Ollama model to be used for picture analysis (should usually be "llava" for picture analysis) |
|`BACKEND_BASE_URL`| Base URL of backend                                                                           |
