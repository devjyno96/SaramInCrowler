# NaverShoppingCrowler

  한 개의 사람인 공고 페이지 내 정보를 크롤링 하는 라이브러리 입니다.

## __1. 필요 라이브러리 목록__


      1. selenium
      2. beautifulsoup4
      3. lxml

##  __2. 필요 프로그램__

      1. chromedriver

## __3. 사용 간 유의점__

      1. chromedriver 실행에는 chrome이 필요합니다.
      2. chromedriver버전과 chrome버전을 맞춰주십시오.
      3. chromedriver는 라이브러리와 동일 폴더 내에 있어야만 합니다.

## __4. 사용 방법__

>1. 클래스를 생성합니다

      crowler = SaramInCrowler()
>2. 크롤링 하길 원하는 페이지의 URL을 crowlling 함수에 삽입합니다

      crowler.crowlling(URL)
>3. 크롤링 결과가 txt 파일로 생성 됩니다 (이름은 rec_idx  값으로 생성됩니다)


## __5. 함수별 역활__

> 추후 작성