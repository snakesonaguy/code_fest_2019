FROM python:2

ADD http_script.py /
ADD websites.txt /

RUN pip install urllib3

CMD [ "python", "-u", "./http_script.py"]

