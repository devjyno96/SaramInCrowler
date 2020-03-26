from selenium import webdriver
from bs4 import BeautifulSoup
import time


class SaramInCrowler :
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(1)

    def __del__(self):
        self.driver.close()

    def getHeader(self, soup):  # 공고 제목 크롤링
        return soup.find(class_='tit_job').text

    # 공고 복리 후생 크롤링 , 항목 제목과 내용 2개 반환
    def getBenefit(self, soup):  # 공고 복리 후생 크롤링 , 항목 제목과 내용 2개 반환
        textTitle = []  # 파싱된 결과 저장할 리스트 # 항목들
        textDetail = []  # 파싱된 결과 저장할 리스트 # 항목 상세 내역

        resultString = '복리 후생'

        try :
            resultTitle = soup.find(class_="jv_cont jv_benefit").findAll('dt')
            resultDetail = soup.find(class_="jv_cont jv_benefit").findAll('dd')
        except AttributeError :
            return ''

        for resultText in resultTitle:
           textTitle.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거
        for resultText in resultDetail:
            textDetail.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거

        for resultT, resultD in zip(textTitle, textDetail):
           resultString += (resultT + " : " + resultD + " \n")

        return resultString + "\n"

        # 공고 핵심 정보 크롤링 , 항목 제목과 내용 2개 반환
    def getSummary(self, soup):  # 공고 핵심 정보
        resultTitle = soup.find(class_="jv_cont jv_summary").findAll('dt')
        resultDetail = soup.find(class_="jv_cont jv_summary").findAll('dd')
        textTitle = []  # 파싱된 결과 저장할 리스트
        textDetail = []  # 파싱된 결과 저장할 리스트

        resultString =  '핵심 정보 \n'
        for resultText in resultTitle:
            textTitle.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거
        for resultText in resultDetail:
            textDetail.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거

        for resultT, resultD in zip(textTitle, textDetail):
            resultString += (resultT + " : " + resultD + " \n")

        return resultString + "\n"

        # 공고 지원 방법, 항목 제목과 내용 2개 반환
    def getHowto(self, soup):  # 공고 지원 방법
        resultTitle = soup.find(class_="jv_cont jv_howto").find(class_="guide").findAll('dt')
        resultDetail = soup.find(class_="jv_cont jv_howto").find(class_="guide").findAll('dd')
        textTitle = []  # 파싱된 결과 저장할 리스트 # 항목들
        textDetail = []  # 파싱된 결과 저장할 리스트 # 항목 상세 내역

        resultString = '지원 방법 \n'

        for resultText in resultTitle:
            textTitle.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거
        for resultText in resultDetail:
            textDetail.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거

        for resultT, resultD in zip(textTitle, textDetail):
            resultString += (resultT + " : " + resultD + " \n")
        return resultString + "\n"


        # 기업 이름, 기업 항목 제목들, 기업 항목 내용들, 3개 반환
    def getCompany(self, soup):  # 공고 기업 정보
        companyName = soup.find(class_="jv_cont jv_company").find(class_="company_name")
        resultTitle = soup.find(class_="jv_cont jv_company").find(class_="info").findAll('dt')
        resultDetail = soup.find(class_="jv_cont jv_company").find(class_="info").findAll('dd')

        textTitle = []  # 파싱된 결과 저장할 리스트 # 항목들
        textDetail = []  # 파싱된 결과 저장할 리스트 # 항목 상세 내역

        resultString = '공고 기업 정보'

        for resultText in resultTitle:
            textTitle.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거
        for resultText in resultDetail:
            textDetail.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거

        resultString += companyName.text

        for resultT, resultD in zip(textTitle, textDetail):
            resultString += (resultT + " : " + resultD + " \n")
        return resultString + '\n'

    # 공고와 관련된 태그 목록, 1개 반환
    def getFooter(self, soup):  # 공고와 관련된 태그 목록

        result = soup.find(class_="jv_cont jv_footer").find(class_="scroll").find_all('li')

        text = []  # 파싱된 결과 저장할 리스트 # 항목들

        resultString = '공고 관련 태그들 \n'

        for resultText in result:
            text.append(resultText.text.strip())  # strip사용 이유 : '면접 후 결정', '지역' 앞에 공백 제거

        for result in text :
            resultString += (result + " ")
        return resultString + '\n'

    # 공고 상세 내용 그냥 가져옴
    def getDetail(self, soup):

        addURL = soup.find(class_="jv_cont jv_detail").find('iframe').get('src') # detail로 들어가는 URL
        fullURL = "http://www.saramin.co.kr" + addURL

        self.driver.get(fullURL)
        time.sleep(0.1)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        resultString = '공고 상세 내용 \n'

        resultString += soup.find(class_="user_content").text

        return resultString


    def getContText(self, targetURL):
        self.driver.get(targetURL)
        time.sleep(0.5)  # 왜 대기 하는가? 값을 서버로 부터 받아오기 전에 값을 사용하려 하기 때문
        # https://selenium-python.readthedocs.io/waits.html : 값이 존재하는지 확인하는 함수 도큐먼트 : 추후 수정예정
        html = self.driver.page_source

        soup = BeautifulSoup(html, 'lxml')

        resultSring = ''

        # html.parser 보다 빠른 parser 이다 lxml install 필요
        resultSring += self.getHeader(soup)
        resultSring += self.getSummary(soup)
        resultSring += self.getDetail(soup)
        resultSring += self.getHowto(soup)
        resultSring += self.getCompany(soup)
        resultSring += self.getBenefit(soup)
        resultSring += self.getFooter(soup)

        return resultSring


    def makeTextFile(self, fileName, resultString):
        txt = fileName + ".txt"
        f = open(txt, 'w', encoding='utf-8')

        f.write(resultString)

        f.close()

        print("파일 저장 완료 : " + txt)
        # test


    def crowling(self, URL):
        fileName = URL.split("/")[6].split("&")[1].split("=")[1]  # rec_idx=게시판 번호 를 추출하는 split
        resultString = self.getContText(URL)
        self.makeTextFile(fileName, resultString)

        print("크롤링 완료 파일 이름 : " + fileName)


if __name__ == "__main__":
    crowler = SaramInCrowler()
    TestURL = []
    TestURL.append(
        "http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=37509044&recommend_ids=eJwzNjc1MTMyN4g3tbSoMQZxDC3NoBwTS3NLC%2BN4cxMzAK2ACQA%3D&view_type=list&rec_scn_id=598&referPage=y&refDpId=SRI_050_VIEW_MTRX_RCT_NOINFO&gz=1&t_ref_scnid=598&refer=y&inner_source=saramin&inner_medium=pattern&inner_campaign=relay_view_1&inner_term=list&dpId=SRI_050_VIEW_MTRX_RCT_NOINFO#seq=0")
    TestURL.append(
        "http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=37529923&recommend_ids=eJxtkLkRAzEMA6txzgfgE7uQ678Ln8cniYHD1QqkBE86M%2BNi1yvfnkQ0D%2FqNZsfSlfoHL%2FwOrEhMn1J%2FcF2nYyw7uLy0YIzbuLy2hRy%2F8fFIFRt5o%2BKsA2470i4BHntnVa9EPL1kcXxl43oKwlJmjdpjVWeX72GQ6oqN3mr%2BLTk%2B26dYFQ%3D%3D&view_type=list&gz=1&t_ref_content=grand&t_ref=area_recruit&t_ref_area=101#seq=0")
    TestURL.append(
        "http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=37553151&recommend_ids=eJxFx8ENACAIA8CVUAql07CIwxujifc7Z4TTqkPVWM4wGfCLnLTTm6F8gajyJnIDNUoQbg%3D%3D&view_type=list&rec_scn_id=598&referPage=y&refDpId=SRI_050_VIEW_MTRX_RCT_NOINFO&gz=1&t_ref_scnid=598&refer=y&inner_source=saramin&inner_medium=pattern&inner_campaign=relay_view_0&inner_term=list&dpId=SRI_050_VIEW_MTRX_RCT_NOINFO#seq=0")
    TestURL.append(
        "http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=37346922&recommend_ids=eJxFx8ENADEIA7CV4AiETMMiHb6qrlL9czAzPH1SPVhxSutXkwGvqI92%2BsdVNxDVMURtSzEUIA%3D%3D&view_type=list&rec_scn_id=598&referPage=y&refDpId=SRI_050_END-VIEW_PRE_RCT&gz=1&t_ref_scnid=598&refer=y&inner_source=saramin&inner_medium=pattern&inner_campaign=relay_view_0&inner_term=list&dpId=SRI_050_END-VIEW_PRE_RCT")

    for URL in TestURL:
        crowler.crowling(str(URL))

# 설치한 라이브러리
# 1. beautifulsoup4
# 2. selenium
# 3. lxml
