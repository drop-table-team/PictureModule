FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./main.py /app/main.py
COPY ./api /app/api
COPY ./source /app/source

CMD ["fastapi", "run", "main.py", "--port", "80"]