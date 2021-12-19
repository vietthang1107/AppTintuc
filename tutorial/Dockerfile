FROM debian:stable-slim

COPY . /usr/src/app

RUN apt-get update -y \
    && apt-get install -y python3 python3-pip gettext default-libmysqlclient-dev python3-dev build-essential libjpeg-dev \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 5 \
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 5 \
    && pip install -r /usr/src/app/req.txt --no-cache-dir \
    && apt-get remove -y python3-dev build-essential libjpeg-dev \
    && apt-get autoremove -y \
    && apt-get clean

WORKDIR /usr/src/app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
