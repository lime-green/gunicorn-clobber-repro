FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt wsgi.py ./
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "-b", ":8000", "wsgi:application"]

COPY repro.py ./

