# Base Image
FROM ubuntu:18.04 

# 이미지에 대한 정보 
LABEL maintainer="my name <my email@gmail.com>"

# Install Apache
RUN apt-get update && \
    apt-get install -y apache2 

# index.html 소스 수정 
RUN echo "This is my Apache Web Page" > /var/www/html/index.html 

# 외부에 공개할 port 정의
EXPOSE 80 

# Apache 실행
CMD [ "/usr/sbin/apache2ctl", "-DFOREGROUND" ]
