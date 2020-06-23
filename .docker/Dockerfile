ARG QGIS_TEST_VERSION=latest
FROM  qgis/qgis:${QGIS_TEST_VERSION}
MAINTAINER Denis Rouzaud <denis@opengis.ch>


RUN pip3 install pytest

#COPY ./requirements.txt /tmp/
#RUN pip3 install -r /tmp/requirements.txt

ENV LANG=C.UTF-8

WORKDIR /
