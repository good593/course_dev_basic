FROM ubuntu:18.04 

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade && \
    apt-get install -y python3-pip

RUN pip3 install --upgrade pip && \
    pip3 install pandas PyMySQL

COPY main.py /root/ 

CMD ["python3"]
