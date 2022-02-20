from selenium import webdriver

# 브라우저 옵션
option = webdriver.ChromeOptions()
option.add_argument('window-size=960,1080')

# chromedriver의 위치 경로 입력
driver = webdriver.Chrome('chromedriver.exe',options=option)

# 열려는 페이지의 URL 입력
driver.get("https://www.naver.com/")

# 페이지 로딩에 걸리는 시간을 최대 10초로 설정
driver.implicitly_wait(time_to_wait=10)

# X Path의 이름으로 웹 페이지의 요소 찾기
element1 = driver.find_element_by_id('query')

# 선택한 웹 페이지의 요소에 text 입력
element1.send_keys("문장을 입력해보자")

# X Path로 버튼을 찾아 클릭
driver.find_element_by_id("search_btn").click()

# 탭에 있는 text 가져와서 출력하기
print(driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[3]/a').text)

# 웹페이지 끄기
driver.quit()

"""
페이지 뒤로가기
driver.back()

페이지 앞으로가기
driver.forward()

input 창에 있는 입력한 text 지우기
element1.clear()

"""