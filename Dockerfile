FROM python

COPY . /app
WORKDIR /app

RUN pip install -Ur /app/requirements.txt
ENV FLASK_APP=/app/app.py

ENTRYPOINT gunicorn app:app