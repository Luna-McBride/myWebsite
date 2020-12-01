FROM python:3.8-alpine
MAINTAINER Luna-McBride <luna.mcbride24@gmail.com>

ENV PATH = "/scripts:${PATH}"

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /requirements.txt
COPY ./manage.py /app/manage.py
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install -r /requirements.txt
RUN apk del .tmp

CMD ["python", "manage.py", "collectstatic"]
CMD ["python", "manage.py", "runserver", "--nostatic", "0.0.0.0:8000"]
COPY . /app/

EXPOSE 8000