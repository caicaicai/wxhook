FROM python:3

ADD index.py /

CMD [ "python", "/index.py" ]

EXPOSE 8080
