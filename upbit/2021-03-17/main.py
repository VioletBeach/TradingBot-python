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
              'price' : None
              })


# 갱신을 위한 변수
repeat_count=21600

# 수익률
yeild = 102.3/100 

# 시작 알림
start_count=0

# 매매 수량
buy_amount=138720

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
            
# 거품 빠진 코인 찾기 위한 변수
min_count=0
min_list=[]
list_result=[]

# 자동 매매 시작
while(1) :
    try :

        # 현재 시간 구하기
        now=datetime.now()
        now=now.strftime('%Y-%m-%d %H:%M:%S')

        # 30분 마다 재로그인
        if repeat_count % 1800 == 0 :
            upbit = pyupbit.Upbit(access,secret)
            # 최근 nday일간 24시간 고가 중 최저가 찾기
            if repeat_count == 21600 :
                for i in coins :
                    history = pyupbit.get_ohlcv(i['key'], interval="day", count=nday)['high']
                    history_high = float(history[0])
                    for a in history :
                        if history_high > float(a) :
                            history_high = float(a)
                    history_high=round_price(history_high*0.9805)
                    i['price']=history_high
                    time.sleep(0.5)
                repeat_count=1
                print("refresh price")
        repeat_count+=1

        # 거래 종목들 호가 불러오기
        orderbook = pyupbit.get_orderbook(inputs)

        # 잔고 불러오기
        balance=upbit.get_balances()
        balance_krw=float(balance[0]['balance'])
        
        # 코인 하나씩 반복
        index=0;
        for i in coins :
            bids_price=float(orderbook[index]['orderbook_units'][0]['bid_price'])
            asks_price=float(orderbook[index]['orderbook_units'][0]['ask_price'])
            index+=1

            ret = next((item for item in balance if item['currency'] == i['key'].replace('KRW-','')), None)

            # 매수
            if not("uuid" in i['order']) and bids_price<=i['price']*1.005 :
                if ret is None and balance_krw>360000 :
                    try:
                        i['order']=upbit.buy_limit_order(i['key'], i['price'], buy_amount/i['price'])
                        time.sleep(0.3)
                    finally:
                        print(i['order'], '\n')
                    
            # 매도
            if ret is not None :
                if float(ret['balance'])>0 :
                    print(upbit.sell_limit_order(i['key'], round_price(i['price']*yeild), upbit.get_balance(i['key'])),'\n')

            # 매수 미체결 주문 취소 (저점 달성 실패 시)
            if ("uuid" in i['order']) and bids_price>=i['price']*1.010 and ret is None :
                try :
                    print(i['key'],'\tcancel',upbit.cancel_order(i['order']['uuid']),'\n')
                finally:
                    i['order']={}
            

            # 종목별 거품 검색
            if min_count==0 :
                min_list.append({
                    'min_per' : (bids_price-i['price'])/i['price'],
                    'min_price' : i['price'],
                    'min_key' : i['key']})

        # 종목 거품 없는 순 정렬
        if min_count==0 :
            list_result=sorted(min_list, key=lambda x:x['min_per'], reverse=False)
            for j in list_result :
                print(j['min_key'],'\t목표가:', j['min_price'])
            min_count=1

        if start_count==0 :
            print("문제없이 실행중")
            start_count=1

        time.sleep(1)
        
    except :
        print("에러 발생")
        continue
            
