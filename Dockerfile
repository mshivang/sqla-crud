FROM --platform=linux/amd64 python:3.11.7

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "manage:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

