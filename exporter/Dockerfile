FROM python:3.12-slim

WORKDIR /app/

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8080

CMD ["gunicorn", "wsgi:metrics", "--log-level=info", "--workers", "3", "--bind", "0.0.0.0:8080"]