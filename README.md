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
- RESTful API에 대한 이해
 
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

| Done               								|        PR         |
|---------------------------------------------------|-------------------|
|상품 삭제 요청 기능 추가<br>상품 ajax로 요청 및 응답<br>products delete url추가|[Products delete #28](https://github.com/ESTsoft-Book-Project/bookstore/pull/28)|
|카카오페이 결제 버튼 생성<br>결제 완료 시 주문 확인 페이지로 리다이렉트<br>결제 중단 시 책 디테일 페이지로 복귀|[Add kakaopay API #58](https://github.com/ESTsoft-Book-Project/bookstore/pull/58)|
|단일 상품 결제 되는 것을 여러 상품 결제 되게 변경|[Kakaopay from order detail #76](https://github.com/ESTsoft-Book-Project/bookstore/pull/76)|
|상품 결제 가격 오류 수정|[kakaopay total_price, when purchases are stopped, red… #87](https://github.com/ESTsoft-Book-Project/bookstore/pull/87)|
|카카오페이 결제 취소 기능 추가|[Add kakaopay purchases cancel #97](https://github.com/ESTsoft-Book-Project/bookstore/pull/97)|
|비밀번호 변경 시, 로그아웃 후 리다이렉트 signin 페이지<br>로그인 안한 유저, 댓글에 대한 삭제 권한이 없는 유저에게는 댓글 삭제 버튼이 보이지 않게 처리<br>Book detail에서 삭제 되면 book list로 리다이렉트<br>Comment model에 user 속성 추가|[Error Handling in profile, book_detail, comment, auth #108](https://github.com/ESTsoft-Book-Project/bookstore/pull/108)|
|비로그인, 로그인 유저 댓글 처리<br>댓글 삭제 시, 유저 인증 추가<br>comment 코드 리펙토링<br>|[Resolve issue 108 (Comments) #114](https://github.com/ESTsoft-Book-Project/bookstore/pull/114)|
|로그인, 비로그인 유저 카트 버튼 처리|[Change hidden style, anonymous user redirect login page #116](https://github.com/ESTsoft-Book-Project/bookstore/pull/116)|
|수량에 따른 결제 처리<br>product모델 수정<br>결제 취소 로직 수정|[when making payment, update product stock / refactor: stripe payment #126](https://github.com/ESTsoft-Book-Project/bookstore/pull/126)|


<br>

## 프로젝트 회의록

<br>

### 5월 20일 / 1차미팅
#### 논의 사항
- 간단한 자기소개 시간
- 프로젝트 진행 방향 의논
#### 정리
- 이미 프로젝트 경험이 있는 사람이 2명정도 있었고 대부분 처음 진행하는 상태
- 프로젝트 주제를 도서 구매 서비스로 결정
- 개인적으로 해당 주제에 관련 필요 기능들 생각해오기

<br>

### 5월 27일 / 2차미팅
#### 논의 사항
- 프로젝트 계획 설정
#### 계획(초안)

| Meeting | Agenda |
|---------|--------|
| 6월 3일| - 기본 유저모델 + 커스텀, CRUD 기본 설계<br>- RESTful API 설계 |
| 6월 10일 | - Products 모델 설계<br>- Products CRUD 설계<br>- RESTful API 설계 |
| 6월 17일 | - Purchases 모델 설계<br>- 구매 로직 설계<br>- 책 재고관리 책 구매 |
| 6월 24일 | - 보완 사항 파악<br>- 인증/인가 관련 사항<br>- 주문 관리<br>- 스토어 매니저 기능 |
| 7월 1일 | - 보안 강화<br>- OAuth 도입<br>- 개인적으로 구현하고 싶은 API 도입<br>- AWS 및 Postgresql로 DB 이전 및 배포 준비 |
| 7월 2일 | - 에러 처리<br>- 최종 배포 준비 |

<br>

### 6월 3일 / 3차 미팅
#### 논의 사항
- 가상환경 설정
- 프로젝트 초기 설정
- Github 설정

#### 정리

| Live coding       | 담당자  |
|-------------------|-------|
| 가상환경 리드        | 최승현 |
| 초기설정 리드        | 김영민 |

<br>

- 모두 동일한 환경을 세팅하기 위해 가상환경 세팅
- 가상환경 세팅에 예상보다 많은 시간이 소요되었고 코드 리뷰와 피드백을 갖는 미팅 횟수를 늘리기로 결정
- 영민님의 주도하에 Secret 키 값을 env파일로 분리하는 작업을 진행
- Github 커밋 규칙과 작업별 branch를 생성하여 작업 및 Pull request를 통해 최종 main으로 merge하는 방식으로 결정
- Django를 처음 다루는 사람들이 많았기 때문에 기능들에 대해 팀별로 진행하기로 결정

#### To do list

| 할 일                          | 담당자               |
|-------------------------------|----------------------|
| 1. signup                     | 김이도, 김태은, 노희연 |
| 2. signin                     | 송주헌, 신태우, **이광호** |
| 3. Profile page               | 최승현, 전정헌, 임동성 |

- 회원가입 구현
- 로그인 구현
- 프로필 구현

<br>

### 6월 5일 / 4차미팅
#### 논의 사항
- Github 사용 미숙
- 각 팀별 기능 구현 코드 리뷰 및 피드백

#### 정리
- Github 사용에 대해 정리
- 팀별 기능 구현 코드에 대해 디스코드 화면공유를 통해 발표를 하였고 다같이 피드백 및 수정

#### 수정사항

| Done               |        PR         |담당자|
|--------------------|-------------------|----|
|Sign up, Sign in|[Signin #1](https://github.com/ESTsoft-Book-Project/bookstore/pull/1/files)|노희연, **이광호**|
|Sign up 수정|[fix(signup): Modify model&form, Include CSRF #5](https://github.com/ESTsoft-Book-Project/bookstore/pull/5/files)|김영민|
|Profile|[feat(profile): Add user update #6](https://github.com/ESTsoft-Book-Project/bookstore/pull/6/files)|전정헌,임동성|

- 회원가입 구현 (HTML Form)
- 로그인 구현 (HTML Form)
- 프로필 페이지 구현 (HTML Form)
- 미동작 되는 회원가입 페이지 수정

#### To Do list

| 할 일                               | 담당자              |
|------------------------------------|-------------------|
| 1. signup + AJAX                   | 김이도, 김태은, 노희연 |
| 2. signin + AJAX                   | 송주헌, 신태우, **이광호** |
| 3. user model custom  | 최승현 |

<br>

### 6월 7일 / 5차 미팅
#### 논의 사항
- 각 팀별 ajax적용 확인
- user model custom관련 발생 오류 브리핑

#### 정리
- signup 코드에 에러메세지 출력 추가하기
- signin 데이터 형식 json형식으로 변경필요
- username대신 email을 기본으로 하도록 user모델 커스텀

#### 수정사항

| Done               |        PR         |담당자|
|--------------------|-------------------|----|
|Sign up|[Signup #4](https://github.com/ESTsoft-Book-Project/bookstore/pull/4)| 노희연 |
|Sign up 수정|[fix(signup): Fix signup issue #11](https://github.com/ESTsoft-Book-Project/bookstore/pull/11/files)|김이도, 김태은|
|Sign in|[feat: Add signin, signout ajax request #23](https://github.com/ESTsoft-Book-Project/bookstore/pull/23/files)|**이광호**, 송주헌, 신태우|
| Resolve migration conflict | [merge: Resolve conflicts between users-model and signup #9](https://github.com/ESTsoft-Book-Project/bookstore/pull/9/files)| 최승현|
|migration 에러에 관한 해결 방안|[docs(migration): About how to resolve migration errors #13](https://github.com/ESTsoft-Book-Project/bookstore/pull/13)|최승현|

- 회원가입 구현 (RESTful API)
- 로그인 구현 (RESTful API)
- migration 에러 해결

#### 이슈 발행

|DESC | ISSUE|
|--------------------|-------------------|
| 미인증 유저 관련 버그 | [bug: 익명유저가 profile에 들어가는 것을 방지 #16](https://github.com/ESTsoft-Book-Project/bookstore/issues/16)|
|미인증 유저 관련 버그|[fix(profile): prevent unauthorized access to profile #22](https://github.com/ESTsoft-Book-Project/bookstore/pull/22/files)|
|RESTful API|[refactor(profile): Replace POST requests with PATCH and DELETE #25](https://github.com/ESTsoft-Book-Project/bookstore/pull/25/files)|

- 미인증 유저 profile 페이지 접속 버그에 대한 이슈 발행
- 프로필 페이지의 익명의 유저가 들어가는 것을 방지를 위한 로그인 인증 구현을 요청
- RESTful API를 위한 수정 요청

<br>

### 6월 13일 / 6차 미팅
#### 논의사항
- products와 purchases 기본 모델 설계
- book_list와 book_detail 페이지를 작성

#### 정리
- 영민님이 product와 purchase관련 초안 코드를 작성
- 코드를 참고하여 product관련 추가 기능 팀별 작업 분배

#### 수정사항
| Live coding      | PR | 담당자|
|------------------|---|--|
| Products model<br> Purchases model<br> book list page<br>  book detail page<br>|  [Products model #27](https://github.com/ESTsoft-Book-Project/bookstore/pull/27)| 김영민 |

- 상품 모델 생성
- 결제 모델 생성
- 상품 리스트, 상품 디테일 페이지 생성

#### To do list

| 할 일             | 담당자              |
|------------------|-------------------|
| Product Update   | 김이도, 김태은, 노희연 |
| Product Delete   | 송주헌, **이광호**, 신태우 |
| Product Create   | 최승현, 전정헌, 임동성 |

<br>

### 6월 15일 / 7차 미팅
#### 논의사항
- PR 코멘트 적극 활용하여 GitHub 코멘트와 코드를 통해 소통
- Prduct CRUD 작업 현황 브리핑

#### 정리

| Done               |        PR         |담당자|
|--------------------|-------------------|----|
|Product Create|[feat(products): Add create and read function to products app #31](https://github.com/ESTsoft-Book-Project/bookstore/pull/31)|최승현,전정헌,임동성|
|Product Delete|[Products delete #28](https://github.com/ESTsoft-Book-Project/bookstore/pull/28)|송주헌,이광호,신태우|
|Product Update| 미구현 |김이도,김태은,노희연|

- Product Create 시 인증 필요
- Product Delete 오류 수정 필요
- Product Update 미구현

#### 문제점 확인
- 짧게 정해진 기간내에 기능 구현을 하려다보니 전체적인 흐름을 이해하고 코드를 짜는것이 아닌 기능 구현에 초점에 맞춰 코드를 짜는 문제가 발생
- 다음 회의까지 기능 추가를 늦추고 전체적인 흐름을 이해하는 시간을 갖고 Product 관련 코드를 다시 수정하도록 결정
<br>

### 6월 17일 / 8차 미팅
#### 논의사항
- 지난 Product 기능 작업에 대한 재브리핑
- 결제로직 stripe 기능 추가

#### 수정사항

| Done               |        PR         |담당자|
|--------------------|-------------------|----|
|Products update|[Products update #35](https://github.com/ESTsoft-Book-Project/bookstore/pull/35)|김이도, 김태은|
|Products Create|[fix(create_product): Fix redirection in create_product #36](https://github.com/ESTsoft-Book-Project/bookstore/pull/36)| 전정헌 |
| products model에 stripe 테이블 추가<br> stripe 결제 로직 생성| [Purchases logic #43](https://github.com/ESTsoft-Book-Project/bookstore/pull/43/files)|   김영민 |

- Products Update 구현
- Products Create 리팩토링
- 결제 로직 구현
  
#### To Do list

| 할 일                                | 담당자             |
|-------------------------------------|------------------|
| 상품 이미지 도입, 배포 준비                  | 김영민      |
| product name필드 unique 해제 시 에러 핸들링 방지   | 김태은   |

<br>

### 6월 19일 / 9차 미팅
#### 수정사항

| Done               |        PR         |담당자|
|--------------------|-------------------|----|
|모델 수정|[refactor(products): Modify update time, Set timezone #38](https://github.com/ESTsoft-Book-Project/bookstore/pull/38)|김이도|
|Slug 에러 방지|[Products handle #42](https://github.com/ESTsoft-Book-Project/bookstore/pull/42)|김태은|

- Product 모델의 update field 대한 수정
- Product 모델의 name field의 unique True 해제 시 발생할 Slug(Handle) 에러 방지

<br>

### 6월 20일 / 10차 미팅
#### 논의사항
- 유저 관련 버그 수정
- Product 관련 오류 수정
- 각자 더 추가해 작업해보고 싶은 API 및 기능 정하기

#### 수정사항

| Done               |        PR         |담당자|
|--------------------|-------------------|----|
|미인가 유저 관련 버그 수정| [인가되지 않은 유저의 책 정보 수정 방지 #46](https://github.com/ESTsoft-Book-Project/bookstore/issues/46)| 김이도 |
|미인증 유저 관련 버그 수정| [fix(products): Fix update-products issue #48](https://github.com/ESTsoft-Book-Project/bookstore/pull/48)|김이도 |
|slug 최적화|[fix(handle): Create unique handle by last object's pk #54](https://github.com/ESTsoft-Book-Project/bookstore/pull/54)|최승현|
|PR #48의 에러 수정|[Handle errors and Display images #55](https://github.com/ESTsoft-Book-Project/bookstore/pull/55)|김영민|
|Product 이미지 모델링  | [Products image #44](https://github.com/ESTsoft-Book-Project/bookstore/pull/44)|김영민|

- base64를 사용하여 binary 형식 이미지 전송
- MEDIA ROOT,  MEDIA URL 세팅
- 이후 S3을 이용한 미디어 파일 관리 리팩토링 결정
- 미인가 유저 `<domain>/products/book/update<slug>` 접속 시 버그 수정
- slug 중복 방지를 위한 넘버링 시 비효율 개선 
- 미인증 유저 버그 수정 (book.user == request.user 확인)

#### To Do list
  
| 할 일               | 담당자              |
|--------------------|-------------------|
| 장바구니 및 주문 재고관리| 최승현, 김태은 |
| OAuth  			 | 김이도 |
| 카카오페이 도입 		  | **이광호** |
| DRF 도입  		    | 임동성, 전정헌 |
| 댓글 추가/삭제         | 노희연    |
| Postgresql, S3, Docker | 김영민    |
| Stripe 로직 리팩토링  | 김영민    |

<br>

### 6월 22일 / 11차 미팅
#### 논의사항
- 각자 맡았던 작업에 대한 브리핑
- 현재까지 구현된 기능들에 대한 정상동작 확인

#### 수정사항

| Done               | PR |담당자           |
|--------------------|--|-----------------|
| Static File| [chore(getCookies): Move getCookies.js into static folder. close #47 #50](https://github.com/ESTsoft-Book-Project/bookstore/pull/50)| 최승현|
| OAuth              | [feat(users): Add social signin feature #61](https://github.com/ESTsoft-Book-Project/bookstore/pull/61) | 김이도              |
| 카카오페이           | [feat(purchases): Add kakaopay API #58](https://github.com/ESTsoft-Book-Project/bookstore/pull/58)  |이광호 |
| 장바구니             | [feat(carts): Add cart function #57](https://github.com/ESTsoft-Book-Project/bookstore/pull/57)|전정헌|

- static file 설정
- 카카오, 네이버, 구글 OAuth 도입
- 카카오 페이 도입

#### 이슈 발행

|DESC | ISSUE|
|--------------------|-------------------|
|장바구니 동적 처리|[enhancement(cart_list): product list will respond with JSON object, not HTML template #60](https://github.com/ESTsoft-Book-Project/bookstore/issues/60)|

- 장바구니 수량 변경 부분에서 수량을 증감 시, 서버에 계속 요청을 보내는 문제 확인
- 수량 변경하는 부분은 프론트엔드에서 처리하도록 변경

<br>

### 6월 24일 / 12차 미팅
#### 논의사항
- 이전 댓글, DRF, 장바구니 관련 브리핑
- 다음 회의까지 AWS계정 생성, pgAdmin4, Docker의 설치

#### 수정사항

| Done               |PR| 담당자              |
|--------------------|--|----------------|
| 리뷰관리                | [Add comment section to book_detail.html](https://github.com/ESTsoft-Book-Project/bookstore/commit/488a02e85f6e851d735aaa2a3bc75431c7b18a26)|노희연 |
| DRF                | [feat(users) : users drf #68](https://github.com/ESTsoft-Book-Project/bookstore/pull/68)|임동성              |
|장바구니 <br> 주문/재고 관리| <br>[JSON response cart list #64](https://github.com/ESTsoft-Book-Project/bookstore/pull/64)<br>[feat(cart): Introduce event listeners #67](https://github.com/ESTsoft-Book-Project/bookstore/pull/67)<br>[feat(carts): Add order_detail #71](https://github.com/ESTsoft-Book-Project/bookstore/pull/71) |최승현, 김태은|

#### 정리
- 댓글 추가/삭제 대한 미구현된 부분에 대한 코드 리뷰
- DRF 코드 구현 및 에러 발생에 대한 코드리뷰
- 장바구니 API 요청 시 서버와의 통신에서의 비효율성에 대한 코드 리뷰
- 결제 로직 리팩토링 필요성

#### 이슈 발행 

|DESC | ISSUE|
|--------------------|-------------------|
|DRF 도입 후 버그|[bug(users):Error not displayed #73](https://github.com/ESTsoft-Book-Project/bookstore/issues/73)<br>[bug(users): Signout error (GET /users/signout/ HTTP/1.1") #74](https://github.com/ESTsoft-Book-Project/bookstore/issues/74)|
|결제 로직에 미로그인시 버그|[Error in payment module when not logged in #69](https://github.com/ESTsoft-Book-Project/bookstore/issues/69)|

- DRF 도입 후 버그 이슈 발행
- 결제 로직에서의 미 로그인시의 에러 및 버그 이슈 발행

<br>

### 6월 26일 / 13차 미팅
#### 논의사항
- 결제 로직 리펙토링 브리핑
- PostgreSQL 연동
- 현재까지 구현된 기능들에 대한 이슈 체크

#### 수정사항

| Done              |PR DESC | 담당자              |
|--------------------|-------------------|-------------|
| stripe 결제 로직 연동  | [Stripe from order detail](https://github.com/ESTsoft-Book-Project/bookstore/pull/75)<br>|김영민 |
|리뷰 관리 |[Comment #92](https://github.com/ESTsoft-Book-Project/bookstore/pull/92)|김영민|
| 카카오페이 결제 로직 연동 | [Kakaopay from order detail #76](https://github.com/ESTsoft-Book-Project/bookstore/pull/76)|**이광호** | 
| 장바구니 및 주문 재고관리|  [feat(cart): order-btn now send PATCH request #77](https://github.com/ESTsoft-Book-Project/bookstore/pull/77)<br>[feat(cart): Add order button #78](https://github.com/ESTsoft-Book-Project/bookstore/pull/78) |최승현, 김태은        |
| 함수명 수정  |[cart, order 함수명 리팩토링 필요 #79](https://github.com/ESTsoft-Book-Project/bookstore/issues/79) | 최승현| 
|PostgreSQL 사용|         [refactor(db): Modify db.sqlite3 to Postgresql #101](https://github.com/ESTsoft-Book-Project/bookstore/pull/101)        |김영민|

#### 정리
- purchases - products의 Many to Many 관계로의 변경 코드 리뷰
- stripe, kakaopay 결제로직 리팩토링 코드 리뷰
- 댓글 추가/삭제 API 완성 코드 리뷰
- 댓글 관련 코드는 미완성된 코드를 이어받아 급하게 구현하여 에러처리 부분에서 미흡한 부분이 많아 추후 리팩토링 하기로 결정

#### 이슈 발행 

| ISSUE          | ISSUE DESC              |
|--------------------|-------------------|
|로그아웃 에러| [bug(users): Signout error (GET /users/signout/ HTTP/1.1") #74](https://github.com/ESTsoft-Book-Project/bookstore/issues/74)       |
| 구매 버튼 버그  |[Error when clicking buy button on book_detail page #90](https://github.com/ESTsoft-Book-Project/bookstore/issues/90)  |
| 장바구니 버그 |  [Order error when there are no products in the shopping cart #91](https://github.com/ESTsoft-Book-Project/bookstore/issues/91) |
| 재고 관련 주문 버그  | [Error in ordering more quantity than stock #93](https://github.com/ESTsoft-Book-Project/bookstore/issues/93)|
| url변경으로 인한 invalid   |[When merging #82 and #83, It does not work due to changing url settings #84](https://github.com/ESTsoft-Book-Project/bookstore/issues/84) |
| 주문 취소 로직에 대한 니즈   |[Kakao Pay and Stripe payment cancellation when order canceled #85](https://github.com/ESTsoft-Book-Project/bookstore/issues/85) |
| Stripe 결제 금액 미반영  |[No price reflected when paying for stripe #88](https://github.com/ESTsoft-Book-Project/bookstore/issues/88)  |

<br>

### 6월 27일 / 14차 미팅
#### 논의사항
- 지난 이슈 사항 현황 브리핑

#### 수정사항
| DESC              |  PR              | 담당자 |
|--------------------|--------------------------|-----|
|로그아웃 이슈 해결|	[Resolve #90, #91 Issue, Handling Errors #96](https://github.com/ESTsoft-Book-Project/bookstore/pull/96)<br>[Hotfix-signout #103](https://github.com/ESTsoft-Book-Project/bookstore/pull/103)<br>[fix(cart): Resolve corner case that Cart quantity exceeds Product stock #104](https://github.com/ESTsoft-Book-Project/bookstore/pull/104)|최승현, 김태은|
|stripe 결제취소로직|[Stripe cancel #95](https://github.com/ESTsoft-Book-Project/bookstore/pull/95)|김영민|
|kakao 결제취소로직|[kakaopay cancel #97](https://github.com/ESTsoft-Book-Project/bookstore/pull/97)|**이광호**| 
|AWS S3 사용| [Storages: Implement AWS S3 storage for static and media files #102](https://github.com/ESTsoft-Book-Project/bookstore/pull/102)        |김영민|

<br>

### 6월 28일 / 15차 미팅
#### 논의사항
- 지금까지의 PR을 모두 merge한 후 마지막으로 처리해야 할 에러에 대해 논의
- 프로젝트 마무리 관련 논의

#### 이슈 발행

| DESC               |        ISSUE         |
|--------------------|-------------------|
|미인증/미인가 유저 설정 | [TODO: new problems and code cleaning #111](https://github.com/ESTsoft-Book-Project/bookstore/issues/111) |
|home 화면 설정 | [chore(name): nav bar title name change #40](https://github.com/ESTsoft-Book-Project/bookstore/issues/40) |
|가격 설정 | [Product.price DecimalField의 max_digits 변경 #32](https://github.com/ESTsoft-Book-Project/bookstore/issues/32)<br>[Updating profile have to require password input #106](https://github.com/ESTsoft-Book-Project/bookstore/issues/106)  |
|Status code| [Set response status #112](https://github.com/ESTsoft-Book-Project/bookstore/issues/112) |
|Stripe 주문명 설정| [Display order name using Stripe #113](https://github.com/ESTsoft-Book-Project/bookstore/issues/113) |
|장바구니 비우기|[Delete Cart elements on purchase success #105](https://github.com/ESTsoft-Book-Project/bookstore/issues/105)  |
| 프로필 페이지 버그 |[Updating profile have to require password input #106](https://github.com/ESTsoft-Book-Project/bookstore/issues/106) |
| 재고 관련 버그 | [Error in ordering more quantity than stock #93](https://github.com/ESTsoft-Book-Project/bookstore/issues/93) |
| 결제에 따른 재고 변경|[Stock does not change after payment success #115](https://github.com/ESTsoft-Book-Project/bookstore/issues/115)|

#### 정리
- 미로그인 유저에 대하여 버튼을 날려버릴 것이 아니라 누르면 로그인 페이지로 리다이렉트 필요
- 백엔드에서 다른 사용자가 남의 댓글 삭제하는 행위 비허용 설정 필요
- 댓글 작성,삭제 로그인 유저만 허용, 미로그인 시 코멘트는 볼 수 있게 설정 필요
- signup에서 validate하지 않은 사용자 입력에서 에러 발생
- 홈페이지를 상품리스트로 변경 필요
- 가격 제한 설정 필요
- 가격 표시 시 소수점 제거 필요
- 가격 설정 시 소수점 비허용 및 알림창 필요
- 결제 성공 시 재고가 그대로임
- 결제 성공 시 장바구니가 그대로임
- 비번 없이 계정이 삭제되고 수정 되는 버그

<br>

### 6월 29일 / 16차 미팅
#### 수정사항

| Done               								|        PR         |담당자|
|---------------------------------------------------|-------------------|-----|
|이미키 크기 제한|[Error handling when data is too big #121](https://github.com/ESTsoft-Book-Project/bookstore/pull/121)|최승현|
|프로필 페이지 DRF 리팩토링|[fix(profile): Profile page requires password input from now #119](https://github.com/ESTsoft-Book-Project/bookstore/pull/119)|최승현|
|장바구니 가격 제한 및 설정|[feat(products): Set price range and remove decimal points #118](https://github.com/ESTsoft-Book-Project/bookstore/pull/118)|김태은|
|결제 성공 시 장바구니 상품 제거<br> 상품 재고 핸들링 <br> 주문 취소 내역 표시 |[Invaild logic handling (#105, #113, #115 Issues) #117](https://github.com/ESTsoft-Book-Project/bookstore/pull/117)|김영민|
|장바구니 미인증/미인가 유저 설정|[fix(cart): Change hidden style, anonymous user redirect login page #116](https://github.com/ESTsoft-Book-Project/bookstore/pull/116)|**이광호**|
|댓글 미인증/미인가 유저 설정|[Resolve issue 108 (Comments) #114](https://github.com/ESTsoft-Book-Project/bookstore/pull/114)|**이광호**|

#### 정리
- 재고를 핸들링하기 위해 purchaseItem이란 테이블을 새로 만든 점에 대한 코드 리뷰
- 장바구니를 비우기 위한 로직 추가와 결제 상품 수량 핸들링 로직 코드 리뷰
- 결제 취소된 상품에 대한 내역 표시 코드 리뷰
- 유저관련 코드 리팩토링에 대한 리뷰(DRF, Serializer)
- 미인증/미인가 유저의 비정상 접속에 대한 BadRequest 처리 코드 리뷰
- 장바구니 가격 제한 및 설정에 대한 코드 리뷰

#### 이슈 발행

| DESC               |        ISSUE         |
|--------------------|-------------------|
|장바구니 페이지 버그|[Bug with "order" button when unchecked checkbox #122](https://github.com/ESTsoft-Book-Project/bookstore/issues/122)<br>[JS null error in cart page #123](https://github.com/ESTsoft-Book-Project/bookstore/issues/123)|

- 체크박스 선택 안하고 주문 버튼 클릭 시 알림이 뜨지만 주문 페이지로 넘어가지는 버그
- 카트상품이 0개 일때 JS null 에러 발생
- 회원가입 시리얼라이저와 로그인/프로필 시리얼라이저의 유효성 검사 동기화가 필요

<br>

### 6월 30일 / 17차 미팅
#### 논의사항
- 배포과정 진행

#### 수정사항

| Done               								|        PR         |담당자 |
|---------------------------------------------------|-------------------|--|
|Dockerfile 작성<br>Nginx 설정<br>Gunicorn 설정<br>Docker container를 사용한 서버 실행|[Build image (Docker / Nginx/ gunicorn / Host and Debug settings) #124](https://github.com/ESTsoft-Book-Project/bookstore/pull/124) |김영민|
|회원가입 시 버그 및 이슈 해결|[Resolve Issue #73. Handle errors for invalid user input #127](https://github.com/ESTsoft-Book-Project/bookstore/pull/127) |김영민|
|OAuth 리팩토링|[fix(users): Fix signup issue with social-login #125](https://github.com/ESTsoft-Book-Project/bookstore/pull/125)<br> [fix(social-signup): Handle errors for invalid user input #128](https://github.com/ESTsoft-Book-Project/bookstore/pull/128)|김이도|
|카카오 결제 재고 핸들링 및 재고 핸들링 로직 리팩토링|[feat(purchases): when making payment, update product stock / refactor: stripe payment #126](https://github.com/ESTsoft-Book-Project/bookstore/pull/126)|**이광호**|

- 회원가입 시리얼라이저와 로그인/프로필 시리얼라이저의 유효성 검사 동기화
- 회원가입 실패 시 에러 출력
- 프로필 페이지 리팩토링으로 인한 OAuth 회원가입 페이지 생성 및 유효성 검사 및 에러출력
- 재고 핸들링 카카오 로직 추가 및 핸들링 로직 리팩토링

#### 이슈 발행

|DESC| ISSUE|
|----|----|
|회원가입 이메일 검증 로직 없음|[Email unique validation check required #134](https://github.com/ESTsoft-Book-Project/bookstore/issues/134)|

<br>

### 7월 1일 / 18차 미팅 - 최종
#### 수정사항

|Done|PR|담당자|
|-----|--|---|
|이미지만료 해결<br>cors 설정|[Set cors and Fix expiration issue with pre-signed URLs #130](https://github.com/ESTsoft-Book-Project/bookstore/pull/130)|김영민|
|AuthorizationQueryParametersError 해결|[Fix build error AuthorizationQueryParametersError(s3) #132](https://github.com/ESTsoft-Book-Project/bookstore/pull/132)<br>[build(static): Fix AuthorizationQueryParametersError #133](https://github.com/ESTsoft-Book-Project/bookstore/pull/133)|김영민|
|이메일 유효성 검사|[fix(users): Add validation for email #135](https://github.com/ESTsoft-Book-Project/bookstore/pull/135)|김영민|
|Static URL 설정|[fix(s3): static urls are now s3 url #136](https://github.com/ESTsoft-Book-Project/bookstore/pull/136)|최승현|
|cors 미들웨어|[fix(CORS): Add middleware that appends response header](https://github.com/ESTsoft-Book-Project/bookstore/pull/137)<br>[fix(cart): Change hard-coded static js file #138](https://github.com/ESTsoft-Book-Project/bookstore/pull/138)|최승현|

<br>

## 힘들었던 점
1. GitHub
2. 추가 기능에 대한 사이드 이슈 발생
