# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb

f = open('C:\\Users\\ti641\\OneDrive\\바탕 화면\\sec_dir\\secret_key.txt', 'r')

con_key = "7199975e6406baa3e3bce7de2f77d2b9"
sec_key = f.readline()
f.close()

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 코인 정보 딕셔너리 담을 리스트 생성
coins = []

# 코인 별 가격 설정
inputs=[{'key':'BTC',
         'buys_price': 52415000},

        {'key':'ETH',
         'buys_price': 1975000}]

# 리스트에 딕셔너리 하나씩 삽입
for i in inputs :
    coins.append({
              'inputs'     :       i,
              'order'      :       [0, 0, 0],
              'is_buy'     :       0,
              'is_sell'    :       0
              })


# 2000번 반복마다 로그인 하기 위한 변수
repeat_count=0

# 수익률
yeild1 = 102.2/100
yeild2 = 102.5/100
yeild3 = 103/100

# 시작 알림
start_count=0

# 매매 수량
buy_amount1=1000
buy_amount2=1000
buy_amount3=1000

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
    
# 자동 매매 시작
while(1) :
    try :
        
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
            if(i['is_sell']==0 and i['order'][0]==0 and bids_price<=i['inputs']['buys_price']*1.005) :
                 i['order'][0]=bithumb.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']), buy_amount1/i['inputs']['buys_price'])
                 print(i['order'][0])
            if(i['is_sell']==0 and i['order'][1]==0 and bids_price<=i['inputs']['buys_price']*1.001) :
                 i['order'][1]=bithumb.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*0.996), buy_amount2/(i['inputs']['buys_price']*0.996))
                 print(i['order'][1])
            if(i['is_sell']==0 and i['order'][2]==0 and bids_price<=i['inputs']['buys_price']*0.998) :
                 i['order'][2]=bithumb.buy_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*0.993), buy_amount3/(i['inputs']['buys_price']*0.993))     
                 print(i['order'][2])
           
            # 매도
            if(bids_price<i['inputs']['buys_price']) :
                bithumb.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*yeild1) ,
                                         (bithumb.get_balance(i['inputs']['key'])[0]-bithumb.get_balance(i['inputs']['key'])[1])*0.3)
                bithumb.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*yeild2) ,
                                         (bithumb.get_balance(i['inputs']['key'])[0]-bithumb.get_balance(i['inputs']['key'])[1])*0.6)
                bithumb.sell_limit_order(i['inputs']['key'], round_price(i['inputs']['buys_price']*yeild3) ,
                                         (bithumb.get_balance(i['inputs']['key'])[0]-bithumb.get_balance(i['inputs']['key'])[1])*1)
                i['is_sell']=1
                
                
            
            # 매수 미체결 주문 취소 (저점 달성 실패 시)
            if(i['order'][0]!=0 and bids_price>=i['inputs']['buys_price']*1.012) :
                bithumb.cancel_order(i['order'][0])
                i['order'][0]=0
            if(i['order'][1]!=0 and bids_price>=i['inputs']['buys_price']*1.008) :
                bithumb.cancel_order(i['order'][1])
                i['order'][1]=0
            if(i['order'][2]!=0 and bids_price>=i['inputs']['buys_price']*1.005) :
                bithumb.cancel_order(i['order'][2])
                i['order'][2]=0
            
            # 매도 체결시 해당 종목 다시 매수모드
            if(i['is_sell']==1) :
                asks_price = float(all['data'][i['inputs']['key']]['asks'][0]['price'])
                if(asks_price>=i['inputs']['buys_price']*yeild1) :
                    i['is_sell']=0
                    i['order'][0]=0
                    i['order'][1]=0
                    i['order'][2]=0

    
        if(start_count==0) :
            print("문제없이 실행중")
            start_count=1

        
        time.sleep(0.5)

    except :
        print("에러 발생")
        continue
