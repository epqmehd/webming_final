# 라이브 러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URl조작을 위한 카테고리 리스트
categories = ["layer-1",
              "smart-contract-platform",
              "exchange-based-tokens","centralized-exchange-token-cex","decentralized-finance-defi",
              "liquid-staking-tokens","meme-token","eth-2-0-staking","non-fungible-tokens-nft"]


total_data = []
for i in range(len(categories)): 
    url = f"https://www.coingecko.com/ko/categories/{categories[i]}" # 카테고리 순서대로 url 접근

    # 페이지 요청
    response = requests.get(url)
    response.raise_for_status()  # 요청/응답 코드가 200이 아니면 예외를 발생

    # 페이지 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 데이터 테이블 찾기
    table = soup.find('tbody')

    # 행 레이블 정리
    columns=['Rank', 'Name', 'Price', 'Volume (24h)','Market Cap']

    # 테이블 행 찾은후 데이터 추출
    cleaned_data = []
    for row in table.find_all('tr'):
        cells = [td.text for td in row.find_all('td') if td.text]
        try:
            cleaned_cells = [cell.replace('\n', '') for cell in cells]  #'\n' 공백 삭제
            cleaned_data.append([cleaned_cells[i] for i in [1, 2, 3, 7, 8]]) # 행 레이블 리스트 삽입
            print(cleaned_cells)  # 확인용 각 행의 데이터 전부 출력
        except IndexError:
            print(f"Error: {cells}")
            continue

    total_data.extend(cleaned_data)  # 추출한 데이터 삽입

# 데이터 프레임 생성과 데이터 삽입
    df = pd.DataFrame(total_data, columns=columns)

    # 확인용 데이터 프레임 출력
    print(df)

    # 카데고리별 엑셀파일로 저장
    df.to_excel(f"webmining_final/data_{categories[i]}.xlsx", index=False, sheet_name='Sheet1')
    # total_data 리스트 비우기
    total_data = []

print("finish")