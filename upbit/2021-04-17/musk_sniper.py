import pyupbit
import time
from datetime import datetime

import twitter
import math

# 업비트
access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"

# 트위터
twitter_consumer_key = "56hFLhYoEXsiOPagcbwOgsqgz"
twitter_consumer_secret = "XHOzX0qCl8UXmxW3yb56fFUAGlBfE5xTGBkN3C2nAY4ttQb1q0"  
twitter_access_token = "1383051723262988290-UHTon7rS9ncgZpqCYTLCvijFOSZojj"
twitter_access_secret = "1fnUyhZ3IU5LseAcLeT6wxiXSNii8PIQT4zOQXfPCawry"
account = "@elonmusk"

# 코인 정보 딕셔너리 담을 리스트 
coins = []

# 코인 종목 삽입
inputs=['KRW-NEO', 'KRW-MTL', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
        'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-KMD', 'KRW-ARK', 'KRW-STORJ',
        'KRW-GRS', 'KRW-REP', 'KRW-EMC2', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX',
        'KRW-TRX', 'KRW-SC', 'KRW-IGNIS', 'KRW-ONT', 'KRW-ZIL', 'KRW-ZRX', 'KRW-LOOM',
        'KRW-BCH', 'KRW-ADX', 'KRW-BAT', 'KRW-IOST', 'KRW-DMT', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA',
        'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-BTT',
        'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT',
        'KRW-SOLVE', 'KRW-MBL', 'KRW-TSHP', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MLK', 'KRW-STPT',
        'KRW-VET', 'KRW-CHZ', 'KRW-PXL', 'KRW-STMX', 'KRW-DKA', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK',
        'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-LAMB', 'KRW-HUNT', 'KRW-MARO',
        'KRW-PLA', 'KRW-SRM', 'KRW-PCI', 'KRW-STRAX', 'KRW-AQT', 'KRW-BCHA', 'KRW-GLM',
        'KRW-SSX', 'KRW-OBSR', 'KRW-FCT2', 'KRW-LBC', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM']

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
buy_amount=248720

# 저점 탐색 일수
nday=26

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
            twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)
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
        #balance_krw=float(balance[0]['balance'])
        
        # 코인 하나씩 반복
        index=0;
        for i in coins :
            print(i['key'])
            bids_price=float(orderbook[index]['orderbook_units'][0]['bid_price'])
            asks_price=float(orderbook[index]['orderbook_units'][0]['ask_price'])
            index+=1

            ret = next((item for item in balance if item['currency'] == i['key'].replace('KRW-','')), None)

            # 매수
            if not("uuid" in i['order']) and bids_price<=i['price']*1.008 :
                if ret is None :
                    try:
                        i['order']=upbit.buy_limit_order(i['key'], i['price'], buy_amount/i['price'])
                        time.sleep(0.3)
                    finally:
                        print(i['key'],'\t', i['order'], '\n')
                    
            # 매도
            if ret is not None :
                if float(ret['balance'])>0 :
                    print(upbit.sell_limit_order(i['key'], round_price(i['price']*yeild), upbit.get_balance(i['key'])),'\n')

            # 매수 미체결 주문 취소 (저점 달성 실패 시)
            if ("uuid" in i['order']) and bids_price>=i['price']*1.013 and ret is None :
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

        current_tweet = twitter_api.GetUserTimeline(screen_name=account, count=1, include_rts=True, exclude_replies=False)[0].text.lower()
        if('doge' in current_tweet) :
            krw_balance=upbit.get_balance("KRW")
            upbit.buy_market_order("KRW-DOGE", krw_balance)
            print("도지 코인 구매")
            break
        
        if('btc' in current_tweet or 'bitcoin' in current_tweet or 'bit coin' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-BTC", krw_balance)
            print("비트 코인 구매")
            break

        if('defi' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-LINK", krw_balance)
            print("폴카닷 구매")
            break

        if('eth' in current_tweet or 'ethereum' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-ETH", krw_balance)
            print("이더리움 구매")
            break

        if('ada' in current_tweet or 'cardano' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-ADA", krw_balance)
            print("에이다 구매")
            break

        if('dot' in current_tweet or 'polkadot' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-DOT", krw_balance)
            print("폴카닷 구매")
            break

        if('ltc' in current_tweet or 'litecoin' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-LTC", krw_balance)
            print("라이트 코인 구매")
            break

        if('eos' in current_tweet or 'eos' in current_tweet) :
            krw_balance=math.ceil(upbit.get_balance("KRW"))
            upbit.buy_market_order("KRW-EOS", krw_balance)
            print("이오스 코인 구매")
            break
        
    except :
        print("에러 발생")
        continue
            
