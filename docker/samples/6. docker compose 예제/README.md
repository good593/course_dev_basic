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
### 단계1: docker-compose.yml 디렉토리로 이동 
- 디렉토리에 존재해야할 것들
  - docker-compose.yml, Dockerfile, main.py, database(폴더)
```shell
ls -al
```
![Alt text](./img/image.png)

----
### 단계2: docker compose 실행 
```shell
docker-compose up -d
```
![Alt text](./img/image-1.png)

---
### 단계3: 생성된 컨테이너 확인 
```shell
docker ps -a
```
![Alt text](./img/image-2.png)

---
### 단계4: compose-python-mysql 실행 결과 확인 
```shell
docker logs compose-python-mysql
```
![Alt text](./img/image-4.png)

---
### 단계5: compose에 포함된 컨테이너 모두 stop
```shell
docker-compose stop
docker ps -a
```
![Alt text](./img/image-5.png)

---
### 단계6: compose에 포한된 리소스 모두 제거 
![Alt text](./img/image-6.png)

---
### 단계7: 제거된 리소스 확인 
- container
```shell
docker ps -a
```
![Alt text](./img/image-7.png)

---
- network
```shell
docker network ls
```
![Alt text](./img/image-8.png)

---
### 단계8: compose 이미지 삭제 
```shell
docker rmi 6dockercompose-python-mysql
docker image ls
```
![Alt text](./img/image-9.png)


