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
### 1단계: 우분투 접속 
![alt text](./img/image-29.png)

### 2단계: ubuntu 계정으로 로그인 
![alt text](./img/image-30.png)

---
### 3단계: GUI 우분투 설치
```shell
sudo apt-get -y update
sudo apt-get -y install ubuntu-desktop
```
![alt text](./img/image-31.png)

---
### 4단계: 종료 
![alt text](./img/image-32.png)

### 5단계: 다시 실행 
![alt text](./img/image-33.png)

---
### 6단계: ubuntu 계정 접속 
![w:800](./img/image-34.png)

---
### 7단계: 터미널 > 필수 라이브러리 설치 
```shell
# 업데이트 목록 갱신
sudo apt-get -y update
# 현재 패키지 업그레이드 
sudo apt-get -y upgrade
# 신규 업데이트 설치 
sudo apt-get -y dist-upgrade
# 필수 라이브러리 설치 
sudo apt-get install -y vim wget unzip ssh openssh-* net-tools
```
![alt text](./img/image-35.png)

---
### 8단계: 우분투 시간 설정 
```shell
sudo timedatectl set-timezone Asia/Seoul --adjust-system-clock
timedatectl
```
![alt text](./img/image-37.png)









