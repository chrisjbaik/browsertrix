FROM python:3.7.2

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD uvicorn --reload --host 0.0.0.0 --port 8000 crawlmanager.api:app 

