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
# Shell
- Shell(쉘)은 커널과 사용자 사이를 이어주는 역할을 해준다.
- Shell은 하나의 명령어 처리기(Command Processor)이다.

### Shell 종류 
- `Bourne-Again Shell (bash)`: 리눅스에서 가장 많이 사용하는 쉘 
- `Bourne Shell (sh)`: 최초의 쉘 

그 외에도 다양한 쉘이 존재함  

---
# Bash Shell

---
### 단계1: 설치된 Shell 확인 
```shell
cat /etc/shells
``` 
![bg right w:600](image.png)

---
### 단계2: 현재 지정된 Shell 확인 
```shell
echo $SHELL
```
![Alt text](image-1.png)

---
# [1. bash 변수](./1.%20bash%20변수.md)

---
# [2. bash Metacharacters](./2.%20bash%20Metacharacters.md)

---
# [3. shell script](./3.%20shell%20script.md)

---
# [4. Positional Parameters](./4.%20Positional%20Parameters.md)

---
# [5. if then fi](./5.%20if%20then%20fi.md)

---
# [6. loop](./6.%20loop.md)

