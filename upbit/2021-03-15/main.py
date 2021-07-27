import pyupbit
import time
from datetime import datetime

access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"

# 코인 정보 딕셔너리 담을 리스트 생성
coins = []

# 코인 종목 삽입
inputs=[
        'KRW-ETH',
        'KRW-BTC',
        'KRW-NPXS',
        'KRW-BTT',
        'KRW-ANKR',
        'KRW-BORA',
        'KRW-DOGE',
        'KRW-CRO',
        'KRW-ADA',
        'KRW-AQT',
        'KRW-SXP',
        'KRW-BCH',
        'KRW-GAS',
        'KRW-ONG',
        'KRW-MFT',
        'KRW-IOST',
        'KRW-GLM',
        'KRW-EMC2',
        'KRW-LTC',
        'KRW-BSV',
        'KRW-LSK',
        'KRW-TSHP',
        'KRW-SRM',
        'KRW-POWR',
        'KRW-SBD',
        'KRW-XTZ',
        'KRW-ICX',
        'KRW-BTG',
        'KRW-SC',
        'KRW-SNT',
        'KRW-XEM',
        'KRW-EOS',
        'KRW-TRX',
        'KRW-OBSR',
        'KRW-DOT',
        'KRW-ATOM',
        'KRW-OMG',
        'KRW-ELF',
        'KRW-ONT',
        'KRW-ETC',
        'KRW-NEO',
        'KRW-GRS',
        'KRW-STEEM',
        'KRW-QTUM',
        'KRW-ZRX',
        'KRW-LINK',
        'KRW-ARK',
        'KRW-STRAX',
        'KRW-KMD',
        'KRW-REP',
        'KRW-BCHA',
        'KRW-WAVES',
        'KRW-KNC',
        'KRW-IOTA'

        ]

# 리스트에 딕셔너리 하나씩 삽입
for i in inputs :
    coins.append({
              'key'     :       i,
              'order'      :       0,
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
buy_amount=7000

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
                    history_high=round_price(history_high*0.988)
                    i['price']=history_high
                    time.sleep(0.5)
                repeat_count=1
        repeat_count+=1

        # 거래 종목들 호가 불러오기
        orderbook = pyupbit.get_orderbook(inputs)
        
        # 코인 하나씩 반복
        index=0;
        for i in coins :
            bids_price=float(orderbook[index]['orderbook_units'][0]['bid_price'])
            asks_price=float(orderbook[index]['orderbook_units'][0]['ask_price'])
            index+=1
            
            # 매수
            if i['order']==0 and bids_price<=i['price']*1.005 :
                try:
                    i['order']=upbit.buy_limit_order(i['key'], i['price'], buy_amount/i['price'])
                finally:
                    print(i['order'], '\n')
                    
            # 매도
            if bids_price<i['price'] and i['sell']==0 :
                upbit.sell_limit_order(i['key'], round_price(i['price']*yeild), upbit.get_balance(i['key']))
                i['sell']=1

            # 매수 미체결 주문 취소 (저점 달성 실패 시)
            if i['order']!=0 and bids_price>=i['price']*1.010 :
                try :
                    print(i['key'],'\t',upbit.cancel_order(i['order']['uuid']),'cancel \t'+now)
                finally:
                    i['order']=0
                    
            # 매도 체결시 해당 종목 다시 매수모드
            if asks_price>=i['price']*yeild :
                i['order']=0
                i['sell']=0
            

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
            
