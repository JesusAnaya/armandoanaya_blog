# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# needed for pillow
RUN apt update && apt-get install -y \
    libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev \
    netcat

# create directory for the app user
RUN mkdir -p /home/app

# user and group
ENV USER=app-www
ENV GROUP=app-www

# create the app user
RUN useradd -ms /bin/bash $USER

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static_root
RUN mkdir $APP_HOME/media_root
WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY ./docker/production/config/web/entrypoint.prod.sh $APP_HOME

# Copy the current directory contents into the containe to $APP_HOME
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R $USER:$GROUP $APP_HOME

# change to the app user
USER $USER

ENTRYPOINT $APP_HOME/entrypoint.prod.sh
