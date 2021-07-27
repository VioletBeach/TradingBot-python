# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb
import time
from datetime import datetime

con_key = "7199975e6406baa3e3bce7de2f77d2b9"
sec_key = "146f48bd8e829c0d460f8a8faa45f710"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 코인 정보 딕셔너리 담을 리스트 생성
coins = []

# 코인 별 가격 설정
inputs=[{'key':'SOC',
         'buys_price': 10.88},

        {'key':'CON',
         'buys_price': 3.578},

        {'key':'LAMB',
         'buys_price': 15.64},

        {'key':'WOZX',
         'buys_price': 1144},

        {'key':'QBZ',
         'buys_price': 5.723},

        {'key':'RINGX',
         'buys_price': 33.04},

        {'key':'XPR',
         'buys_price': 4.233},

        {'key':'VSYS',
         'buys_price': 14.32},

        {'key':'GOM2',
         'buys_price': 11.04},

        {'key':'AE',
         'buys_price': 106.8},

        {'key':'CENNZ',
         'buys_price': 29.32},

        {'key':'MBL',
         'buys_price': 1.531},

        {'key':'WEMIX',
         'buys_price': 173.4},

        {'key':'EOS',
         'buys_price': 2745},

        {'key':'IPX',
         'buys_price': 39.64},

        {'key':'FLETA',
         'buys_price': 4.574},

        {'key':'EGG',
         'buys_price': 4.661},

        {'key':'DAD',
         'buys_price': 155.6},

        {'key':'EVZ',
         'buys_price': 9.582},

        {'key':'AOA',
         'buys_price': 1.664},

        {'key':'ADP',
         'buys_price': 11.23},

        {'key':'MLK',
         'buys_price': 155.4},

        {'key':'TMTG',
         'buys_price': 4.314},

        {'key':'EM',
         'buys_price': 3.947},

        {'key':'RNT',
         'buys_price': 11.14},

        {'key':'GXC',
         'buys_price': 340.1},

        {'key':'XSR',
         'buys_price': 3.422},

        {'key':'META',
         'buys_price': 8.512},

        {'key':'APM',
         'buys_price': 11.64},

        {'key':'MIX',
         'buys_price': 1.941},
        
        {'key':'OBSR',
         'buys_price': 3.641},

        {'key':'DVC',
         'buys_price': 39.46},

        {'key':'AION',
         'buys_price': 71.24},

        {'key':'BASIC',
         'buys_price': 5.868},

        {'key':'WET',
         'buys_price': 4.214},

        {'key':'APIX',
         'buys_price': 54.47},

        {'key':'TRUE',
         'buys_price': 173.7},

        {'key':'QTCON',
         'buys_price': 15.04},
        
        {'key':'XNO',
         'buys_price':141.7},
        
        {'key':'PCM',
         'buys_price':6.841},
        
        {'key':'ANW',
         'buys_price':98.4},
        
        {'key':'FIT',
         'buys_price':2.433},
        
        {'key':'WOM',
         'buys_price':182.4},

        {'key':'POLA',
         'buys_price':258.5},

        {'key':'EL',
         'buys_price':2.734}

        #temp
        ,

        {'key':'HDAC',
         'buys_price':16.08}

        ]

# 리스트에 딕셔너리 하나씩 삽입
for i in inputs :
    coins.append({
              'inputs'     :       i,
              'order'      :       [0, 0, 0]
              })


# 2000번 반복마다 로그인 하기 위한 변수
repeat_count=0

# 수익률
yeild1 = 102/100 
yeild2 = 102.5/100
yeild3 = 103/100

# 시작 알림
start_count=0

# 매매 수량
buy_amount1=88971
buy_amount2=172365
buy_amount3=273451

# 거래 금액 소숫점 맞추는 함수
def round_price(a):
    if(a>=1000) :
        return int(a)
    elif(a>=100) :
        return round(a,1)
    elif(a>=10) :
        return round(a,2)
    elif(a>=1) :
        return round(a,3)
    elif(a>=0) :
        return round(a,4)

min_per=1
min_key=0
min_price=0
    
# 자동 매매 시작
while(1) :
    try :

        # 현재 시간 구하기
        now=datetime.now()
        now=now.strftime('%Y-%m-%d %H:%M:%S')
        
        # 일정 텀을 두고 로그인
        if(repeat_count==2000) :
            bithumb = pybithumb.Bithumb(con_key, sec_key)
            if bithumb is None : 
                bithumb = pybithumb.Bithumb(con_key, sec_key)
                if bithumb is None :
                    bithumb = pybithumb.Bithumb(con_key, sec_key)
            repeat_count=-1
        repeat_count+=1

        # 호가 불러오기
        all = pybithumb.get_orderbook("ALL")
        if all is None :
            all = pybithumb.get_orderbook("ALL")
            if all is None :
                all = pybithumb.get_orderbook("ALL")

        # 코인 하나씩 반복
        for i in coins :
            bids_price = float(all['data'][i['inputs']['key']]['bids'][0]['price'])

            
            # 매수
            if(i['order'][0]==0 and bids_price<=i['inputs']['buys_price']*1.005) :
                 try:
                    i['order'][0]=bithumb.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']), buy_amount1/i['inputs']['buys_price'])
                 finally:
                    print(i['inputs']['key'],'\t',i['order'][0],'priceNum:1','\t'+now)
            if(i['order'][1]==0 and bids_price<=i['inputs']['buys_price']*1.001) :
                try: 
                    i['order'][1]=bithumb.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*0.996), buy_amount2/(i['inputs']['buys_price']*0.996))
                finally:
                    print(i['inputs']['key'],'\t',i['order'][1],'priceNum:2','\t'+now)
            if(i['order'][2]==0 and bids_price<=i['inputs']['buys_price']*0.998) :
                try: 
                    i['order'][2]=bithumb.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*0.993), buy_amount3/(i['inputs']['buys_price']*0.993))     
                finally:
                    print(i['inputs']['key'],'\t',i['order'][2],'priceNum:3','\t'+now)
           
            # 매도
            if(bids_price<i['inputs']['buys_price']) :
                bithumb.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*yeild1) ,
                                         (bithumb.get_balance(i['inputs']['key'])[0]-bithumb.get_balance(i['inputs']['key'])[1])*0.3)
                bithumb.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*yeild2) ,
                                         (bithumb.get_balance(i['inputs']['key'])[0]-bithumb.get_balance(i['inputs']['key'])[1])*0.6)
                bithumb.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*yeild3) ,
                                         (bithumb.get_balance(i['inputs']['key'])[0]-bithumb.get_balance(i['inputs']['key'])[1])*1)
                
                
            
            # 매수 미체결 주문 취소 (저점 달성 실패 시)
            if(i['order'][0]!=0 and bids_price>=i['inputs']['buys_price']*1.012) :
                try :
                    print(i['inputs']['key'],'\t',bithumb.cancel_order(i['order'][0]),'cancel, priceNum:1','\t'+now)
                finally:
                    i['order'][0]=0
            if(i['order'][1]!=0 and bids_price>=i['inputs']['buys_price']*1.008) :
                try :
                    print(i['inputs']['key'],'\t',bithumb.cancel_order(i['order'][1]),'cancel, priceNum:2','\t'+now)
                finally:
                    i['order'][1]=0
            if(i['order'][2]!=0 and bids_price>=i['inputs']['buys_price']*1.005) :
                try :
                    print(i['inputs']['key'],'\t',bithumb.cancel_order(i['order'][2]),'cancel, priceNum:3','\t'+now)
                finally:
                    i['order'][2]=0
                    
            # 매도 체결시 해당 종목 다시 매수모드
            asks_price = float(all['data'][i['inputs']['key']]['asks'][0]['price'])
            if(asks_price>=i['inputs']['buys_price']*yeild1) :
                i['order'][0]=0
            if(asks_price>=i['inputs']['buys_price']*yeild2) :
                i['order'][1]=0
            if(asks_price>=i['inputs']['buys_price']*yeild3) :
                i['order'][2]=0
            
        '''
            df = pybithumb.get_candlestick(i['inputs']['key'])
            yesterday = df.iloc[-2]
            volume = yesterday['volume']
            print(volume)

        '''

        '''
        if((i['inputs']['buys_price']-bids_price)/i['inputs']['buys_price']<min_per) :
            min_per=(i['inputs']['buys_price']-bids_price)/i['inputs']['buys_price']
            min_price=i['inputs']['buys_price']
            min_key=i['inputs']['key']
        print(min_key, min_price)
        '''
        if(start_count==0) :
            print("문제없이 실행중")
            start_count=1

        
        time.sleep(0.3)

    except :
        print("에러 발생")
        continue
