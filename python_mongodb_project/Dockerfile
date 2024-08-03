FROM python:3.9-slim

RUN pip install pymongo

WORKDIR /app

COPY write_to_mongodb.py /app

CMD ["python", "write_to_mongodb.py"]
