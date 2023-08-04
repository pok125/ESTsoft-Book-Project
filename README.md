## 프로젝트 소개

- 유저가 책 상품을 구매 및 판매 할 수 있는 온라인 서점 프로젝트

## 프로젝트 기간

- 2023.06.03 - 2023.07.02

## 기술 스택

- Javascript
- Python, Django
- PostgreSQL
- Docker, Nginx
- Amazon S3, Amazon EC2, Amazon RDS

## 구현 내용

- 프론트엔드 담당이 따로 없습니다.
- 백엔드 담당이 프론트엔드까지 모두 구현하였습니다.
 
#### 전체 기능
- 유저 회원가입, 로그인, 프로필 수정, 회원 탈퇴 기능
- OAuth를 활용한 구글, 네이버, 카카오 회원가입 및 로그인
  (배포 후 구글 로그인은 https 도입 후 이용 가능합니다)
- 상품 추가, 수정, 삭제 및 댓글 기능
- 장바구니 기능
- Stripe, 카카오페이를 활용한 결제 및 결제 취소
- 결제에 따른 재고 수량 변경

<br>

| 기능 | 담당자 |
|---------|--------|
|유저|최승현, 김영민|
|OAuth|김이도|
|상품|김영민|
|댓글|김영민, **이광호**|
|결제|김영민, **이광호**|
|장바구니|최승현|
|주문|최승현, 김태은|
|배포|김영민, 최승현|

<br>

#### 내가 기여한 부분 

- 로그인 로직 작성
- 상품삭제 로직 작성
- 상품 모델 리펙토링
- 댓글 추가/삭제 로직 작성
- 결제 모델 리펙토링
- 결제 시작/성공/중단 로직 작성
- 결제 환불 로직 작성
- 결제 후 장바구니 비우기 및 재고 수량 변경

<br>


## UI 

<br>

![](https://velog.velcdn.com/images/iankimdev/post/47e4db0e-dd74-4c0e-b9b5-164a495db8c7/image.png)


![](https://velog.velcdn.com/images/iankimdev/post/1cff1f05-c54f-4dfb-9a7e-73a6349fe880/image.png)


<br>
<br>

## 나의 Pull Request





## 느낀점
마지막으로 docker를 사용하여 이미지를 빌드하고 끝을 냈다. 집필도 마무리를 짓고 최종본을 송부만 남겨두었다. 개발을 모르는 사람들을 이끌어야하는 상황이여서 힘들었지만 필요할 때 역할을 해준 팀원들이 있었기에 끝까지 해낼 수 있었다. 진행하면서 기술적으로도 많이 실력이 향상했지만, 소통하는 부분에서 가장 크게 배울 수 있는 시간이었다.
