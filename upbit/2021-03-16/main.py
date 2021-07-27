import pyupbit
import time
from datetime import datetime

access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"

# 코인 정보 딕셔너리 담을 리스트 생성
coins = []

# 코인 종목 삽입
inputs=['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
        'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-KMD', 'KRW-ARK', 'KRW-STORJ',
        'KRW-GRS', 'KRW-REP', 'KRW-EMC2', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS',
        'KRW-TRX', 'KRW-SC', 'KRW-IGNIS', 'KRW-ONT', 'KRW-ZIL', 'KRW-ZRX', 'KRW-SRN', 'KRW-LOOM',
        'KRW-BCH', 'KRW-ADX', 'KRW-BAT', 'KRW-IOST', 'KRW-DMT', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA',
        'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-BTT',
        'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-ANKR', 'KRW-NPXS', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT',
        'KRW-SOLVE', 'KRW-MBL', 'KRW-TSHP', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MLK', 'KRW-STPT',
        'KRW-VET', 'KRW-CHZ', 'KRW-PXL', 'KRW-STMX', 'KRW-DKA', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK',
        'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-LAMB', 'KRW-HUNT', 'KRW-MARO',
        'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-PCI', 'KRW-STRAX', 'KRW-AQT', 'KRW-BCHA', 'KRW-GLM',
        'KRW-SSX', 'KRW-OBSR', 'KRW-FCT2', 'KRW-LBC', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE']

# 리스트에 딕셔너리 하나씩 삽입
for i in inputs :
    coins.append({
              'key'     :       i,
              'order'      :       {},
              'price' : None,
              'sell' : 0
              })


# 갱신을 위한 변수
repeat_count=21600

# 수익률
yeild = 102.3/100 

# 시작 알림
start_count=0

# 매매 수량
buy_amount=8000

# 저점 탐색 일수
nday=24

# 거래 금액 소숫점 맞추는 함수
def round_price(a):
    if(a>=10000000) :
        return round(a,-4)
    elif(a>=1000000) :
        return round(a, -3)
    elif(a>=100000) :
        return round(a, -2)
    elif(a>=10000) :
        return round(a, -1)
    elif(a>=1000) :
        return round(a, -1)
    elif(a>=100) :
        return int(a)
    elif(a>=10) :
        return round(a, 1)
    elif(a>=1) :
        return round(a, 2)
    elif(a>=0) :
        return round(a, 3)
            
upbit = pyupbit.Upbit(access,secret)


# 잔고 불러오기
balance=upbit.get_balances()
print(balance[0]['balance'])
            
