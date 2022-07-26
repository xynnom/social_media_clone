FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt .
COPY ./src /app
COPY .env .env
WORKDIR /app
RUN pip install -r requirements.txt && rm requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]