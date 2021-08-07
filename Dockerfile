FROM python:3.9.6-alpine
WORKDIR /code
ENV FLASK_APP=main.py
RUN apk add gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["gunicorn", "main:app"]


