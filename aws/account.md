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
# [AWS IAM](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/intro-structure.html)
- AWS Identity and Access Management(IAM)은 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다. 
- IAM을 사용하면 사용자가 액세스할 수 있는 AWS 리소스를 제어하는 권한을 중앙에서 관리할 수 있습니다. 
- IAM을 사용하여 리소스를 사용하도록 인증(로그인) 및 권한 부여(권한 있음)된 대상을 제어합니다.

---
### [IAM 작동 방식](https://aws.amazon.com/ko/blogs/korea/new-for-identity-federation-use-employee-attributes-for-access-control-in-aws/)

![Alt text](./img/account/image1.png)

---
# [AWS Admin 계정 만들기](https://docs.aws.amazon.com/ko_kr/streams/latest/dev/setting-up.html)
- AWS에 처음 가입한 이메일로 로그인하면 루트 사용자입니다.
- 루트 사용자는 AWS의 요금/정산 등 중요한 리소스에 접근이 가능한 계정이다. 
- 따라서 AWS에서 제공하는 리소스를 사용(개발)하는 경우에는 IAM 사용자를 만들어서 계정별 권한을 부여하여 사용해야 한다. 

---
### 단계1: IAM 접속
![Alt text](./img/account/image2-10.png)

---
### 단계2: User groups
![Alt text](./img/account/image2-11.png)

---
- User groups 설정
![w:700](./img/account/image2-12.png)
- Policies 정의 
![w:700](./img/account/image2-13.png)

---
### 단계3: Users
![Alt text](./img/account/image2-14.png)

---
- Specify user details
![w:900](./img/account/image2-17.png)

---
- Set permissions
![w:900](./img/account/image2-16.png)

---
- Review and create
![w:900](./img/account/image2-18.png)

---
- Retrieve password
![Alt text](./img/account/image2-19.png)
![Alt text](./img/account/image2-20.png)

---
### 단계4: 콘솔 로그인 
![w:800](./img/account/image2-21.png)

---
- 새 비밀번호 생성 
![w:800](./img/account/image2-22.png)

---
### 단계5: MFA devices 설정 
![w:600](./img/account/image2-23.png)
![w:600](./img/account/image2-24.png)

---
![w:600](./img/account/image2-25.png)

---
- [사용가능한 앱 목록](https://docs.aws.amazon.com/ko_kr/singlesignon/latest/userguide/mfa-types.html#mfa-types-apps?icmpid=docs_sso_user_portal)
![w:700](./img/account/image2-26.png)

---
### 단계6: [AWS CLI 설정](https://docs.aws.amazon.com/ko_kr/streams/latest/dev/setup-awscli.html)
- [AWS CLI 설치](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html)
  - [맥북인 경우 root 계정으로 변경 후 진행](https://heeestorys.tistory.com/877)

![w:500](./img/account/image.png)

---
### 단계7: Access Key 생성 
![w:550](./img/account/image3.png)
![w:550](./img/account/image3-1.png)

---
![w:800](./img/account/image3-2.png)

---
![w:800](./img/account/image3-3.png)
![w:800](./img/account/image3-4.png)

---
### 단계8: [AWS configure에 적용](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-quickstart.html)  
- 다운로드 파일의 내용을 이용하여 입력 
```shell
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE(아이디 입력)
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPx(비번 입력)
Default region name [None]: ap-northeast-2
Default output format [None]: json
```
![bg right w:600](./img/account/image3-5.png)

---
### 단계8: VS Code 적용 
- AWS 익스텐션 설치 
![w:600](./img/account/image-27.png)

---
- AWS config 설정 확인 
![w:600](./img/account/image-28.png)
![w:600](./img/account/image-29.png)

---
- [AWS CLI 예제](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-services-s3-commands.html)
```shell
$ aws s3 ls # 생성된 s3 버킷 조회 
$ aws s3 mb s3://s3이름 # s3이름 >> 해당 이름으로 s3 버킷 생성  
$ aws s3 ls # 생성된 s3 버킷 조회 
```
![w:1000](./img/account/image-1.png)

---
![w:600](./img/account/image-30.png)




---
# [IAM Identity Center (SSO) 계정만들기](https://growth-coder.tistory.com/115)
- [IAM Identity Center란?](https://docs.aws.amazon.com/ko_kr/singlesignon/latest/userguide/what-is.html)

### 단계1: IAM 접속 > 사용자 선택 
![Alt text](./img/account/image-2.png)

---
### 단계2: 사용자 생성 
![Alt text](./img/account/image-3.png)
- Identity Center에서 사용자 지정 
![Alt text](./img/account/image-4.png)

---
### 단계3: Identity Center 활성화 
![w:500](./img/account/image-5.png)
![w:500](./img/account/image-6.png)
![w:500](./img/account/image-7.png)

---
### 단계4: Identity Center를 이용한 사용자 계정생성
![w:500](./img/account/image-8.png)
![w:500](./img/account/image-9.png)

---
### 단계5: Identity Center를 이용한 그룹 생성
![w:500](./img/account/image-10.png)
![w:500](./img/account/image-11.png)

---
### 단계6: Identity Center의 그룹에 사용자 추가
![w:600](./img/account/image-12.png)
- 생성된 사용자 확인 
![w:600](./img/account/image-20.png)

---
### 단계7: 사용자 생성때 입력한 이메일 주소로 설정 메일 확인 
- 이메일로 받은 `Accept invitation`을 누르면 비밀번호를 설정
![w:600](./img/account/image-13.png)

---
### 단계8: 이메일로 받은 `AWS access portal URL`에 접속 및 로그인
![w:600](./img/account/image-13.png)
- 로그인 성공 
![Alt text](./img/account/image-15.png)

---
### 단계9: 사용할 권한 생성 
![w:500](./img/account/image-16.png)
- AdministratorAccess(관리자 권한) 선택 
![w:500](./img/account/image-17.png)

---
![Alt text](./img/account/image-18.png)

---
![Alt text](./img/account/image-19.png)

---
- 생성된 권한 확인 
![Alt text](./img/account/image-14.png)

---
### 단계10: 관리계정 선택
![w:600](./img/account/image-21.png)
- 사용자 또는 그룹 할당
![w:600](./img/account/image-22.png)

---
![w:500](./img/account/image-23.png)
![w:500](./img/account/image-24.png)

---
![w:500](./img/account/image-25.png)
- 이메일로 받은 Your AWS access portal URL로 접속하여 다시 로그인하면 아래와 같은 이미지를 볼 수 있다. 
![w:500](./img/account/image-26.png)

---
### 단계11: MFA devices 설정 
- 생성된 user 선택 
![Alt text](./img/account/image1-10.png)
- MFA 등록 
![Alt text](./img/account/image1-11.png)

---
![w:800](./img/account/image1-12.png)

---
- [사용가능한 앱 목록](https://docs.aws.amazon.com/ko_kr/singlesignon/latest/userguide/mfa-types.html#mfa-types-apps?icmpid=docs_sso_user_portal)
![w:700](./img/account/image1-13.png)

---
### 단계12: [AWS CLI 설정](https://docs.aws.amazon.com/ko_kr/streams/latest/dev/setup-awscli.html)
- [AWS CLI 설치](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html)
  - [맥북인 경우 root 계정으로 변경 후 진행](https://heeestorys.tistory.com/877)

![w:500](./img/account/image.png)

---
- [aws configure sso 마법사를 사용하여 프로파일 구성](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/sso-configure-profile-token.html)
  - [us-east-1(region) 고정 관련 오류](https://github.com/aws/aws-toolkit-vscode/issues/3009)
```shell
$ aws configure sso
SSO session name (Recommended): 적당한 이름입력
SSO start URL [None]: 이메일로 받은 Your AWS access portal URL
SSO region [None]: us-east-1 # us-east-1으로 해야함
SSO registration scopes [None]: sso:account:access
```

---
- AWS config 설정 확인 

![w:600](./img/account/image-28.png)
![w:600](./img/account/image-29.png)


---
- [AWS CLI 예제](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-services-s3-commands.html)
```shell
$ aws s3 ls # 생성된 s3 버킷 조회 
$ aws s3 mb s3://s3이름 # s3이름 >> 해당 이름으로 s3 버킷 생성  
$ aws s3 ls # 생성된 s3 버킷 조회 
```
![w:1000](./img/account/image-1.png)

---
![w:600](./img/account/image-30.png)


