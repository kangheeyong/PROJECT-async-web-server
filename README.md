# PROJECT-async-web-server




- 본 프로젝트는 async web server 개발하는 것입니다. 이 웹서버는 unicode 이름을 검색하면 unicode 값을 web을 통하여 보여주는 것이 목적입니다.(toy project라서 서버의 목적 자체는 의미 없습니다.) 백엔드에서 유니코드 이름 검색을 위한 인덱스를 만들고 웹에서 검색을 하면 이 인덱스를 통하여 값을 반환합니다. 마지막으로 이 서버는 도커를 통하여 배포할 수 있게 만들었습니다.

- 이 프로젝트의 목적은 [웹 풀스택 개발 과제]를 만들고 모범 답안을 만드는 것입니다. 막연하게 공부하는 것보다 특정 요구사항이 주어지면 그 요구사항에 맞춰서 개발하는 것이 개발자로서 성장에 많은 도움이 된다고 생각합니다. 하지만 초보 개발자가 어떤 toy project를 어떻게 시작하느냐를 생각하는 것은 개인적으로 초보가 할 수 있는 것이 아니라고 생각했습니다. 이러한 문제는 어느정도 경험이 있는 사람이 만드는 것이 맞다고 생각합니다. 저도 초보자지만 저의 경험을 참고하여 toy project 문제를 만들어 봤습니다.

- 제가 만든 toy project에서는 처음부터 코드를 작성하는 것이아니라 몇몇 기능이 구현된 코드를 제공하고, 이를 분석하여 요구사항에 맞춰서 개발하는 것입니다. 이렇게 한 이유는 이러한 조건이 있어야 효율적으로 공부하고 성장할 수 있다고 생각하기 때문입니다.

- 문제는 [전문가를 위한 파이썬](http://www.yes24.com/Product/Goods/30231768)을 참고했습니다.

---
### 요구사항
  - requirement에 있는 코드를 참고하여 만들 것.[(link)](https://github.com/kangheeyong/PROJECT-async-web-server/tree/master/sample)
    - 만약 사용한다면 그대로 사용하지 말고 코드 리팩토링해서 사용할 것
  - unicodedata 모듈을 사용하여 검색 인덱스를 만들 것.
    - sample에 있는 코드를 참고하면 됨.
  - 버전 관리는 git으로 환경 관리는 docker를 이용할 것.
    - dockerfile을 만들어 바로 배포할 수 있게 할 것.
### 추가 요구사항
  - 비동기 처리 구현
    - 파이썬 비동기 프로그래밍(asyncio)을 사용해주세요.
  - 로컬 캐싱 구현
    - 같은 검색 query가 있아면 cache에서 그 값을 바로 반환 해주세요.
    - 검색 시 임의로 딜레이를 주어서 검색 딜레이를 줘서 캐싱 기능의 효과를 확인하세요.
  - 테스트 코드 작성
    - pytest를 사용하여 unicode 검색이 잘되는지 검증해주세요.
    - tox를 이용하여 다양한 파이썬 버전에서 패키지가 제대로 설치되는지 확인 해주세요.
  - 웹소켓을 이용한 스크롤 구현
    - 모든 검색결과를 html 문서를 통해 보낼 경우 html 문서 파일 크기가 너무 크기 때문에(실제로는 아니지만...) 웹소켓을 이용하여 점진적 내려받기를 구현해주세요.
   


## 1. 실행 방법
### 1.1 설치 및 실행
```
  make docker_run
```

### 1.2 접속
  `http://127.0.0.1:8080`

## 2. 실행 화면
<img width="926" alt="스크린샷 2020-05-22 오후 8 10 20" src="https://user-images.githubusercontent.com/18637774/82662125-45373800-9c68-11ea-8ad3-fad4418e7697.png">


## 3. Jenkins를 이용한 빌드 테스트 
  - https://github.com/kangheeyong/TEST-jenkins
  - test

