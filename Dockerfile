FROM python

RUN pip install -Ur requirements.txt
ENV FLASK_APP=app.py

ENTRYPOINT gunicorn app:app