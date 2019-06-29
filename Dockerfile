FROM python:3.6
LABEL maintainer "Travis Shears <t@travisshears.com>"

ENV ORIGIN_DATE="2019,6,28"
RUN apt-get update
RUN mkdir /army
WORKDIR /army
COPY . /army
#RUN pip install --no-cache-dir -r requirements.txt
