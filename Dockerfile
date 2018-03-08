FROM python:2

ADD index.py /

#RUN pip install httplib

CMD [ "python", "/index.py" ]

EXPOSE 8080
