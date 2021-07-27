import pyupbit
import time
from datetime import datetime

import twitter
import math

# 업비트
access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"
secret = "dVJ0KAuoCmOfjyHNk42CgqMMvkTq1LotxSFOqvNQ"

# 트위터
twitter_consumer_key = "56hFLhYoEXsiOPagcbwOgsqgz"
twitter_consumer_secret = "XHOzX0qCl8UXmxW3yb56fFUAGlBfE5xTGBkN3C2nAY4ttQb1q0"  
twitter_access_token = "1383051723262988290-UHTon7rS9ncgZpqCYTLCvijFOSZojj"
twitter_access_secret = "1fnUyhZ3IU5LseAcLeT6wxiXSNii8PIQT4zOQXfPCawry"
account = "@elonmusk"

# 갱신을 위한 변수
repeat_count=21600

# 시작 알림
start_count=0

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
        repeat_count+=1

        # 거래 종목들 호가 불러오기
        orderbook = pyupbit.get_orderbook(inputs)

        # 잔고 불러오기
        balance=upbit.get_balances()
        #balance_krw=float(balance[0]['balance'])

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
            
