# 카테고리별 저장된 엑셀파일 불러와서 인덱스 산출
# 사용자에게 최대 인덱스값 입력 받음 기본 200
# 카테고리 내 시총 합  / 100억
import pandas as pd

# 데이터 전처리 
#  달러 표시,쉼표 변환,float화 함수
def convert_to_float(value):
    if isinstance(value, str):
        return float(value.replace('$', '').replace(',', '').replace('-','0')) # - 값의 경우 0변환
    return value

# 카테고리 리스트
categories = ["layer-1",
              "smart-contract-platform",
              "exchange-based-tokens","centralized-exchange-token-cex","decentralized-finance-defi",
              "liquid-staking-tokens","meme-token","eth-2-0-staking","non-fungible-tokens-nft"]
# 수집할 데이터의 순위제한
max_rank = 200 
# 카테고리별 인덱스 저장을 위한 딕셔너리
total_index = {}
for category in categories:
    # 엑셀파일 불러오기
    df = pd.read_excel(f"webmining_final/data_{category}.xlsx")

    # 문자열로된 숫자 값 변환
    df['Price'] = df['Price'].apply(convert_to_float)
    df['Volume (24h)'] = df['Volume (24h)'].apply(convert_to_float)
    df['Market Cap'] = df['Market Cap'].apply(convert_to_float)

    df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce')

    # max_rank 순위 이내 데이터만을 위한 제한
    filtered_df = df[df['Rank'] <= max_rank]

    # 정제된 데이터의 시가총액 합
    total_marketcap = filtered_df['Market Cap'].sum()

    index_categories = total_marketcap/10000000000
    print(filtered_df)
    print(total_marketcap)
    # 확인용 인덱스 값 산출
    print(f"{category}의 인덱스 :{index_categories}")
    # 딕셔너리에 인덱스명과 인덱스값 삽입
    total_index[category]=index_categories
    
# 정리된 모든 인덱스 출력
print(f"인덱스 딕셔너리 :{total_index}")