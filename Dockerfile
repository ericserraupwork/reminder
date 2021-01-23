FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install cron
SHELL ["/bin/bash", "-c", "-l"]
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT /code/start.sh
EXPOSE 8000
