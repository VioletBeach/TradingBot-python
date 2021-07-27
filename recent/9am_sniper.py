import pyupbit
import time
from datetime import datetime

# 업비트
access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"
secret = "dVJ0KAuoCmOfjyHNk42CgqMMvkTq1LotxSFOqvNQ"

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
              'sell'        :       {},
              'price' : None
              })


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

        # 30분 마다 재로그인
        if repeat_count % 1800 == 0 :
            upbit = pyupbit.Upbit(access,secret)

            # 최근 nday일간 24시간 고가 중 최저가 찾기
            if repeat_count == 21600 :
                for i in coins :
                    history = pyupbit.get_ohlcv(i['key'], interval="minute240", count=nday)['high']
                    history_high = float(history[0])
                    for a in history :
                        if history_high > float(a) :
                            history_high = float(a)
                    i['price']=history_high
                    time.sleep(0.5)
                repeat_count=1
                print("refresh price")
        repeat_count+=1

        # 거래 종목들 호가 불러오기
        orderbook = pyupbit.get_orderbook(inputs)

        # 잔고 불러오기
        balance=upbit.get_balances()
        
        # 코인 하나씩 반복
        index=0;
        # 거품 빠진 코인 찾기 위한 변수
        min_list=[]
        list_result=[]
        for i in coins :
            bids_price=float(orderbook[index]['orderbook_units'][0]['bid_price'])
            asks_price=float(orderbook[index]['orderbook_units'][0]['ask_price'])
            index+=1

            min_list.append({
                    'min_per' : (bids_price-i['price'])/i['price'],
                    'min_price' : bids_price,
                    'min_key' : i['key']})

        # 종목 거품 없는 순 정렬
        list_result=sorted(min_list, key=lambda x:x['min_per'], reverse=False)
        print(list_result)
        
        now = datetime.today()
        if len(upbit.get_balances())==1 and now.hour==8 and now.minute==52 :
            
            print(upbit.buy_market_order(list_result[0]['min_key'], 11000))
            print(upbit.buy_market_order(list_result[1]['min_key'], 11000))
            print(upbit.buy_market_order(list_result[2]['min_key'], 11000))
            print(upbit.buy_market_order(list_result[3]['min_key'], 11000))
            print(upbit.buy_market_order(list_result[4]['min_key'], 11000))

            sell1=upbit.sell_limit_order(list_result[0]['min_key'], round_price(list_result[0]['min_price']*1.08), upbit.get_balance(list_result[0]['min_key']))
            sell2=upbit.sell_limit_order(list_result[1]['min_key'], round_price(list_result[1]['min_price']*1.08), upbit.get_balance(list_result[1]['min_key']))
            sell3=upbit.sell_limit_order(list_result[2]['min_key'], round_price(list_result[2]['min_price']*1.08), upbit.get_balance(list_result[2]['min_key']))
            sell4=upbit.sell_limit_order(list_result[3]['min_key'], round_price(list_result[3]['min_price']*1.08), upbit.get_balance(list_result[3]['min_key']))
            sell5=upbit.sell_limit_order(list_result[4]['min_key'], round_price(list_result[4]['min_price']*1.08), upbit.get_balance(list_result[4]['min_key']))

        if now.hour==9 and now.minute==26 :
            
            upbit.cancel_order(sell1['uuid'])
            upbit.cancel_order(sell2['uuid'])
            upbit.cancel_order(sell3['uuid'])
            upbit.cancel_order(sell4['uuid'])
            upbit.cancel_order(sell5['uuid'])
            
            print(upbit.sell_market_order(list_result[0]['min_key'], upbit.get_balance(list_result[0]['min_key'])))
            print(upbit.sell_market_order(list_result[1]['min_key'], upbit.get_balance(list_result[1]['min_key'])))
            print(upbit.sell_market_order(list_result[2]['min_key'], upbit.get_balance(list_result[2]['min_key'])))
            print(upbit.sell_market_order(list_result[3]['min_key'], upbit.get_balance(list_result[3]['min_key'])))
            print(upbit.sell_market_order(list_result[4]['min_key'], upbit.get_balance(list_result[4]['min_key'])))
            
        if start_count==0 :
            print("문제없이 실행중")
            start_count=1

        time.sleep(1)
        
    except :
        print("에러 발생")
        continue
            
