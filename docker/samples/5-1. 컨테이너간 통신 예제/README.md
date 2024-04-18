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
### 단계1: 네트워크 생성 
```shell
docker network create my-net
docker network ls
```
![Alt text](./img/image-2.png)

---
### 단계2: database 디렉토리 생성 
1. 테스트할 폴더로 이동 
2. database 디렉토리(폴더) 생성 
![bg right w:600](./img/image.png)

---
### 단계3: mysql 컨테이너 생성 및 실행 
```shell
docker run -d --name mysql-container -v /Users/gyoungwon-cho/dev/docker/test/database:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=pass mysql:latest

docker ps
```
![Alt text](./img/image-1.png)

---
### 단계4: mysql > 네트워크 연결 
```shell
docker network connect my-net mysql-container
```
![Alt text](./img/image-3.png)

---
### 단계5: pymysql 이미지 생성 
- Dockerfile이 있는 폴더로 이동 후 실행 
```shell
docker build -t pymysql:latest .
```
![w:800](./img/image-4.png)

---
### 단계6: pymysql 컨테이너 생성/실행 및 네트워크 연결 
```shell
docker run -d --name pymysql-container --network=my-net pymysql
```
![Alt text](./img/image-5.png)

---
### 단계7: main.py > 결과 확인 
```shell
docker logs pymysql-container
```
![Alt text](./img/image-6.png)

