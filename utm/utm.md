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
### 1단계: 새 가상머신 만들기 
![bg right w:600](./img/image-1.png)

---
### 2단계: Virtualize 선택 
- Virtualize
  - arm64(즉, M1)용 우분투 이미지 구동 
  - 매우 빠르게 구동됨 
- Emulate
  - x86(즉, 인텔)용 우분투 이미지 구동 
  - 호환 과정에 의한 추가 연산으로 느림 

![bg right w:600](./img/image-2.png)

---
### 3단계: Linux 선택 
- 우분투는 리눅스 배포판임 

![bg right w:600](./img/image-3.png)

---
### 4단계: 우분투 이미지 적용
- 탐색 -> Continue

![bg right w:600](./img/image-4.png)

---
### 5단계: 장치 설정
- 메모리: 2048 MB
- CPU: 1

![bg right w:600](./img/image-5.png)

---
### 6단계: 하드디스크 설정 
![bg right w:600](./img/image-6.png)

---
### 7단계: 공유폴더 > 생략 
![bg right w:600](./img/image-7.png)

---
### 8단계: 이름 작성 
![bg right w:600](./img/image-8.png)
