FROM python:3.7

ENV APP_HOME /APP_HOME
WORKDIR $APP_HOME
COPY . .

RUN pip install Flask gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app