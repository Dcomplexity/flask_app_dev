FROM python:3.6
MAINTAINER Chuang cdengcnc@outlook.com
WORKDIR /flask/flaskr
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]



