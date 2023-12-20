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
# [Git 기본 명령어](https://subicura.com/git/guide/basic.html#git-init-%E1%84%8C%E1%85%A5%E1%84%8C%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A9-%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5)

## git init - (로컬)저장소 만들기 

```shell
$ mkdir sample # 디렉토리 생성 
$ cd sample # 디렉토리 이동 
$ touch red orange # 파일 만들기 
$ echo "빨강" >> red # 파일 수정하기 
$ echo "주황" >> orange # 파일 수정하기 

$ git init # (로컬)저장소 만들기 
$ ls -al # 데랙토리 생성 
```

---
![w:1000](./img/command/image-5.png)

---
## git status - 현재 상태 확인 
현재 작업 중인 파일의 상태를 확인합니다.

```shell
$ git status 
```

![w:900](./img/command/image-6.png)

---
## git add - 현재 상태 추적 
파일의 변경사항을 인덱스index에 추가합니다. Git은 커밋하기 전, 인덱스에 먼저 커밋할 파일을 추가합니다.

```shell
$ git add -A # all이라는 뜻으로 새로운 파일들 전체 추적 
$ git status 
```

![w:800](./img/command/image-7.png)

---
## git commit - 현재 상태 저장
인덱스에 추가된 변경 사항을 이력에 추가합니다.

```shell
$ git commit -m "v1 commit" # v1 commit이라는 메시지와 함께 상태 저장 
$ git log # 커밋 히스토리 조회(화면 나가기: q) 
```
![Alt text](./img/command/image-9.png)

---
![Alt text](./img/command/image-8.png)
![w:600](./img/command/image.png)

---
## git log - 커밋 히스토리 조회 
- 새 파일 추가 및 커밋 
- log화면 나가기: q 
```shell
# 새 파일 추가 
$ touch yellow
$ echo "노랑" >> yellow
$ git status 

# 새 파일 커밋 
$ git add -A 
$ git commit -m "v2 commit" 
$ git log # 2개의 커밋 이력이 조회됨 
```
---
![w:700](./img/command/image-10.png)
![w:700](./img/command/image-1.png)

---
# 다양한 변화(시도)

### 작업
1. red 삭제
2. orange에 내용 추가
3. green 파일 추가
4. 상태 확인
5. 전체 파일 인덱스에 추가
6. 세 번째 이력 커밋
7. 커밋 이력 조회 

```shell
$ rm red # 1.
$ echo "오렌지" >> orange # 2. 
$ touch green # 3. 
$ git status # 4.
$ git add -A # 5.
$ git commit -m "v3 commit" # 6.
$ git log # 7.
```
---
![w:600](./img/command/image-11.png)
![w:600](./img/command/image-2.png)

---
# git reset - 이전 상태로(이력제거)
- 특정 커밋까지 이력을 초기화합니다. 바로 전, 또는 n번 전까지 작업했던 내용을 취소할 수 있습니다. 
- 열심히 작업했는데, 전혀 엉뚱한 걸 했거나 작업한 내용이 필요 없어질 때 사용합니다. 
- 이력이 지워지기 때문에 주의해야 합니다.

---
### 작업 
1. 커밋 이력(ID) 조회
2. 2번 커밋으로 이력 초기화(3번 이력 삭제)
3. 커밋 이력 조회(3번 이력 삭제 확인)
  - 지웠던 `red 파일`이 되살아나고 `orange 파일` 내용이 수정되고,
  - `green 파일`이 사라졌다.

---
```shell
$ git log 
$ git reset {v2 커밋 아이디} --hard # 커밋 아이디 예) 27a00b7 (앞에 7자 정도 복사)
$ git log # 3번 이력이 삭제됨...
```

![Alt text](./img/command/image-12.png)

---
![w:700](./img/command/image-13.png)
![w:700](./img/command/image-3.png)

---
# git revert - 이전 상태로 (이력 유지)
- 특정 커밋을 취소하는 새로운 커밋을 만듭니다. 여기선 3번 커밋을 취소하는 새로운 커밋을 생성하여 마치 2번 커밋 상태로 돌아간 것 같지만 기존 이력을 유지하는 모습을 확인합니다.
- 일반적으로 특정 버전을 배포했는데 문제가 생기면 문제가 생긴 커밋을 revert합니다. (빠른 조치/롤백) 다시 원복한 상태로 작업을 이어서 하고 해당 문제를 수정하면 다시 커밋하는 방식을 사용합니다.

---
### 작업 
1. git reset 명령어로 3번 커밋이 지워졌다면 이전 실습을 통해 다시 커밋 추가
2. git log로 3번 커밋 ID 조회
3. 3번 커밋 취소
  - 지웠던 red가 되살아나고 orange 내용이 수정되고 green 파일이 사라진 것을 확인
  - git log를 통해 새로운 커밋이 추가된 것을 확인

---
```shell
$ git add -A 
$ git commit -m "v4 commit"
$ git log
$ git revert --no-commit {v4 커밋 아이디} # 커밋 아이디 예) 306b947 (앞에 7자 정도 복사)
$ git commit -m "new revert"
$ git log
```
![Alt text](./img/command/image-16.png)

---
![w:500](./img/command/image-15.png)
![w:500](./img/command/image-4.png)














