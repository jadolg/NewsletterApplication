FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /app
WORKDIR /app
EXPOSE 8000
CMD ["gunicorn", "NewsletterApplication.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

