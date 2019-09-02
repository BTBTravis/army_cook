FROM python:3.6
LABEL maintainer "Travis Shears <t@travisshears.com>"

RUN apt-get update
RUN mkdir /army
WORKDIR /army
COPY . /army
RUN pip install --no-cache-dir .
CMD armycook
