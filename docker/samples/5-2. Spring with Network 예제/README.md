---
style: |
  img {
    display: block;
    float: none;
    margin-left: auto;
    margin-right: auto;
  }
marp: true
paginate: true
---
# Docker Network

---
### Docker Network 생성
```shell
docker network create spring-net
docker network ls
```
![alt text](image.png)

---
# MySQL 

---
### 단계1: MySQL Image 
```shell
docker images

# 만약 없다면,
docker pull mysql
```
![alt text](image-1.png)

---
### 단계2: MySQL Container
```shell
docker run -d --name mysql-container -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass mysql

docker ps
```
![alt text](image-2.png)

---
### 단계3: dbeaver 및 CREATE DATABASE
```sql
CREATE DATABASE springdocker;

show databases;
```
![alt text](image-3.png)

---
### 단계4: Network Connect
```shell
docker network connect spring-net mysql-container
```
![alt text](image-4.png)

---
# SpringBoot JPA

---
### 단계1: application.yaml
```yaml
spring:
    output:
        ansi:
            enabled: always
    # 데이터베이스 설정 
    datasource:
        # jdbc:mysql://[mysql 도커 컨테이너명]:3306/[database이름]
        url: jdbc:mysql://mysql-container:3306/springdocker?userSSL=false&allowPublicKeyRetrieval=true&serverTimezone=Asia/Seoul
        username: root
        password: pass
        driver-class-name: com.mysql.cj.jdbc.Driver
    # jpa 설정 
    jpa:
        hibernate:
            ddl-auto: update
        properties:
            hibernate:
                show_sql: true
                format_sql: true
                
```
---
### 단계2: @SpringBootTest & @Test 주석처리 
- Test 과정에서 JPA가 MySQL 접속하는 과정에 오류가 발생할 수 있음 
- 아직 MySQL이 포함된 docker network에 접속을 할 수 없기 때문에 오류가 발생함 

![alt text](image-6.png)

---
### 단계3: Dockerfile
```docker
FROM gradle:7.6-jdk17-alpine as build

ENV APP_HOME=/apps

WORKDIR $APP_HOME

COPY build.gradle settings.gradle gradlew $APP_HOME

COPY gradle $APP_HOME/gradle

RUN chmod +x gradlew

RUN ./gradlew build || return 0

COPY src $APP_HOME/src

RUN ./gradlew clean build

FROM openjdk:17.0.2-jdk

ENV APP_HOME=/apps
ARG ARTIFACT_NAME=app.jar
# ARG JAR_FILE_PATH=build/libs/[프로젝트명]-0.0.1-SNAPSHOT.jar 
ARG JAR_FILE_PATH=build/libs/springdockernetwork-0.0.1-SNAPSHOT.jar 

WORKDIR $APP_HOME

COPY --from=build $APP_HOME/$JAR_FILE_PATH $ARTIFACT_NAME

EXPOSE 8080

#ENTRYPOINT ["java", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseCGroupMemoryLimitForHeap", "-Djava.security.egd=file:/dev/./urandom", "-jar", "app.jar"]
ENTRYPOINT ["java", "-jar", "app.jar"]
```
---
### 단계4: docker build
```shell
docker build -t springdockernetwork .
```
![alt text](image-5.png)

---
### 단계5: docker run 
```shell
docker run -d --name spring-container --network=my-net springdockernetwork
```




