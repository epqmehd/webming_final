# 코인게코 전체 코인목록 페이지의 데이터를 크롤링
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 행이름 리스트
columns=['Rank', 'Name', 'Price', 'Volume (24h)','Market Cap']

# 리스트가 저장된 리스트 선언
total_data = []

# 원하는페이지 수만큼 반복 ,1페이지에 100개의 데이터 존재
for i in range(1, 3):
    url = f"https://www.coingecko.com/ko?page={i}"

    # 요청
    response = requests.get(url)
    response.raise_for_status()  

    # 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 테이블 찾기
    table = soup.find('tbody')

    # 테이블에서 데이터 추출
    cleaned_data = []
    for row in table.find_all('tr'):
        cells = [td.text for td in row.find_all('td') if td.text]
        try:
            cleaned_cells = [cell.replace('\n', '') for cell in cells]  #'\n' 공백 삭제
            cleaned_data.append([cleaned_cells[i] for i in [1, 2, 3, 7, 8]])
        except IndexError:
            print(f"Error: {cells}")
            continue

    total_data.extend(cleaned_data)  # 한페이지에서 추출한 데이터를 total_data에 삽입

# 데이터 프레임화 
df = pd.DataFrame(total_data, columns=columns)

# 확인용 데이터 프레임 출력
print(df)

# 엑셀파일로 저장
df.to_excel("webmining_final/coingecko_200.xlsx", index=False, sheet_name='Sheet1')

print("finish")