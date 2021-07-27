import pyupbit
import time
from datetime import datetime

# 업비트
access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"

# 코인 정보 딕셔너리 담을 리스트 
coins = []

# 코인 종목 삽입
inputs=['KRW-NEO', 'KRW-MTL', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES', 'KRW-PXL', 'KRW-HIVE', 
        'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-KMD', 'KRW-ARK', 'KRW-STORJ',
        'KRW-GRS', 'KRW-REP', 'KRW-EMC2', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-FLOW',
        'KRW-SC', 'KRW-IGNIS', 'KRW-ONT', 'KRW-ZIL', 'KRW-ZRX', 'KRW-LOOM', 'KRW-AXS', 'KRW-STX',
        'KRW-BCH', 'KRW-ADX', 'KRW-BAT', 'KRW-IOST', 'KRW-DMT', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA',
        'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-BTT',
        'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-FLOW', 
        'KRW-SOLVE', 'KRW-MBL', 'KRW-TSHP', 'KRW-WAXP', 'KRW-HBAR', 'KRW-MLK', 'KRW-STPT', 'KRW-DAWN',
        'KRW-VET', 'KRW-CHZ', 'KRW-PXL', 'KRW-STMX', 'KRW-DKA', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK',
        'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-LAMB', 'KRW-HUNT', 'KRW-MARO',
        'KRW-PLA', 'KRW-SRM', 'KRW-PCI', 'KRW-STRAX', 'KRW-AQT', 'KRW-BCHA', 'KRW-GLM',
        'KRW-SSX', 'KRW-OBSR', 'KRW-FCT2', 'KRW-LBC', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM']

# 리스트에 딕셔너리 하나씩 삽입
for i in inputs :
    coins.append({
              'key'     :       i,
              'price' : None
              })

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

# 초기 테스트
upbit = pyupbit.Upbit(access,secret)
krw=upbit.get_balance()-10000
amount=int(krw/5)

for i in coins :
    history = pyupbit.get_ohlcv(i['key'], interval="day", count=nday)['high']
    history_high = float(history[0])
    for a in history :
        if history_high > float(a) :
            history_high = float(a)
    i['price']=history_high
    time.sleep(0.3)
print("refresh price")

# 자동 매매 시작
while(1) :
    try :

        now = datetime.today()
        
        if now.hour==8 and now.minute==45 :
            upbit = pyupbit.Upbit(access,secret)
            krw=upbit.get_balance()-10000
            amount=int(krw/5)

            for i in coins :
                history = pyupbit.get_ohlcv(i['key'], interval="day", count=nday)['high']
                history_high = float(history[0])
                for a in history :
                    if history_high > float(a) :
                        history_high = float(a)
                i['price']=history_high
                time.sleep(0.3)
            print("refresh price")
        
        if len(upbit.get_balances())==1 and now.hour==8 and now.minute==52 :

            min_list=[]
            list_result=[]

            for i in coins :
                bids_price=pyupbit.get_current_price(i['key'])
                min_list.append({
                    'min_per' : (bids_price-i['price'])/i['price'],
                    'min_price' : bids_price,
                    'min_key' : i['key']})

            list_result=sorted(min_list, key=lambda x:x['min_per'], reverse=False)
            
            print(upbit.buy_market_order(list_result[0]['min_key'], amount))
            print(upbit.buy_market_order(list_result[1]['min_key'], amount))
            print(upbit.buy_market_order(list_result[2]['min_key'], amount))
            print(upbit.buy_market_order(list_result[3]['min_key'], amount))
            print(upbit.buy_market_order(list_result[4]['min_key'], amount))

            sell1=upbit.sell_limit_order(list_result[0]['min_key'], round_price(list_result[0]['min_price']*1.016), upbit.get_balance(list_result[0]['min_key']))
            sell2=upbit.sell_limit_order(list_result[1]['min_key'], round_price(list_result[1]['min_price']*1.016), upbit.get_balance(list_result[1]['min_key']))
            sell3=upbit.sell_limit_order(list_result[2]['min_key'], round_price(list_result[2]['min_price']*1.016), upbit.get_balance(list_result[2]['min_key']))
            sell4=upbit.sell_limit_order(list_result[3]['min_key'], round_price(list_result[3]['min_price']*1.016), upbit.get_balance(list_result[3]['min_key']))
            sell5=upbit.sell_limit_order(list_result[4]['min_key'], round_price(list_result[4]['min_price']*1.016), upbit.get_balance(list_result[4]['min_key']))

        if now.hour==9 and now.minute==26 and len(upbit.get_balance())!=1 :
            
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

        time.sleep(10)
        
    except :
        print("에러 발생")
        continue
            
