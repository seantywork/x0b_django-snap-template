FROM python:3.9


WORKDIR /djangosnap

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install python3-venv -y \
    && apt-get install default-libmysqlclient-dev -y \
    && apt-get install gcc -y \
    && apt-get install python3-dev -y \
    && apt-get install libssl-dev -y \
    && apt-get install python3-pip -y


COPY . /djangosnap


RUN pip3 install -r requirements.txt


EXPOSE 8000

CMD ["gunicorn","--bind=0.0.0.0:8000","--workers=2","djangosnap.wsgi:application","--access-logfile=-","--error-logfile=-"]



