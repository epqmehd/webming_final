# 시총상위 200위까지  엑셀파일 불러와서 인덱스 산출
# 시총 합  / 100억
# coingecko200.py 연계파일
import pandas as pd

# 데이터 전처리 
#  달러 표시,쉼표 변환,float화 함수
def convert_to_float(value):
    if isinstance(value, str):
        return float(value.replace('$', '').replace(',', '').replace('-','0')) # - 값의 경우 0변환
    return value

max_rank = 200
# 엑셀 불러오기
df = pd.read_excel("webmining_final/coingecko_200.xlsx")

# 문자열로된 숫자 값 변환
df['Price'] = df['Price'].apply(convert_to_float)
df['Volume (24h)'] = df['Volume (24h)'].apply(convert_to_float)
df['Market Cap'] = df['Market Cap'].apply(convert_to_float)

df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce')

# max_rank 순위 이내 데이터만을 위한 제한
filtered_df = df[df['Rank'] <= max_rank]

# 인덱스 값 산출을 위한 시가총액 합
total_marketcap = filtered_df['Market Cap'].sum()

# 인덱스 값
Crypto_200 = total_marketcap/10000000000

print(f"상위 200개 시가총액의 합 :${total_marketcap}")
print(f"Crypto 200 :{Crypto_200}")