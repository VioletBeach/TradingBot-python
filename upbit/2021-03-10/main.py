import pyupbit
import time
from datetime import datetime

access = "8lbeuGzMvUbft2zy5p4vRNWOdlwC8pi73GFTqbfA"
upbit = pyupbit.Upbit(access,secret)

# 코인 정보 딕셔너리 담을 리스트 생성
coins = []

# 코인 별 가격 설정
inputs=[{'key':'KRW-XRP',
         'buy_price': 542},

        {'key':'KRW-ETH',
         'buy_price': 2080000}

        ]

# 키 리스트
keyList=[]
for a in inputs :
    keyList.append(a['key'])
print(keyList)

# 리스트에 딕셔너리 하나씩 삽입
for i in inputs :
    coins.append({
              'inputs'     :       i,
              'order'      :       0
              })


# 2000번 반복마다 로그인 하기 위한 변수
repeat_count=0

# 수익률
yeild = 103/100 

# 시작 알림
start_count=0

# 매매 수량
buy_amount=927100

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

min_count=0
min_list=[]
list_result=[]
    
# 자동 매매 시작
while(1) :
    try :

        # 현재 시간 구하기
        now=datetime.now()
        now=now.strftime('%Y-%m-%d %H:%M:%S')
        
        # 일정 텀을 두고 로그인
        if(repeat_count==2000) :
            upbit = pyupbit.Upbit(access,secret)
            repeat_count=-1
        repeat_count+=1

        # 호가 불러오기

        

        
        # 코인 하나씩 반복
        index=0;
        print(keyList)
        for i in coins :
            orderbook = pyupbit.get_orderbook(keyList)
            bids_price=float(orderbook[index]['orderbook_units'][0]['bid_price'])
            asks_price=float(orderbook[index]['orderbook_units'][0]['ask_price'])
            index+=1

            
            # 매수
            if i['order']==0 and bids_price<=i['inputs']['buy_price']*1.005 :
                try:
                    i['order']=upbit.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buy_price']), buy_amount/i['inputs']['buy_price'])
                finally:
                    print(i['inputs']['key'], '\t', i['order'], '\t' + now)
                    
            # 매도
            if(bids_price<i['inputs']['buy_price']) :
                upbit.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buy_price']*yeild), upbit.get_balance(i['inputs']['key']))
            
            # 매수 미체결 주문 취소 (저점 달성 실패 시)
            if i['order']!=0 and bids_price>=i['inputs']['buy_price']*1.010 :
                try :
                    print(i['inputs']['key'],'\t',upbit.cancel_order(i['order']['uuid']),'cancel \t'+now)
                finally:
                    i['order']=0
                    
            # 매도 체결시 해당 종목 다시 매수모드
            if asks_price>=i['inputs']['buy_price']*yeild 
                i['order']=0
            

            # 종목별 거품 검색
            if min_count==0 :
                min_list.append({
                    'min_per' : (bids_price-i['inputs']['buy_price'])/i['inputs']['buy_price'],
                    'min_price' : i['inputs']['buy_price'],
                    'min_key' : i['inputs']['key']})

        # 종목 거품 없는 순 정렬
        if min_count==0 :
            list_result=sorted(min_list, key=lambda x:x['min_per'], reverse=False)
            for j in list_result :
                print(j['min_key'])
            min_count=1

        if start_count==0 :
            print("문제없이 실행중")
            start_count=1

        time.sleep(0.5)

    except :
        print("에러 발생")
        continue
            
