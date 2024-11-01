FROM python:3.11-slim
#FROM ubuntu:latest
#LABEL authors="Oleksii"
#
#ENTRYPOINT ["top", "-b"]

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]