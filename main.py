# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb

f = open('C:\\Users\\ti641\\OneDrive\\바탕 화면\\sec_dir\\secret_key.txt', 'r')

con_key = "f86f6593322bceaf389748e714ba14d9"
sec_key = f.readline()
f.close()

bithumb = pybithumb.Bithumb(con_key, sec_key)

### 코인별 구매 가격 설정
buy_soda_price=12.05
buy_con_price=3.915
buy_lamba_price=16.62
buy_eforce_price=1326
buy_queenB_price=5.102
buy_ringX_price=32.22
buy_proton_price=4.233


# 코인별 구매 여부 - 매수한 후에 판매하기 위해서
is_buy_soda = 0
is_buy_con = 0
is_buy_lamba = 0
is_buy_eforce = 0
is_buy_queenB = 0
is_buy_ringX = 0
is_buy_proton = 0

# 수익률
yeild = 105/100

while(1) :
    
    # 원화 자산 조회
    krw = bithumb.get_balance("BTC")[2]
    print("현재 잔고는", int(krw), "원입니다.\n")

    # 호가 불러오기
    all = pybithumb.get_orderbook("ALL")

    # 저점 달성시 매수 [저점을 변수로 설정할까 고민중]
    soda_price = float(all['data']['SOC']['asks'][0]['price'])
    if soda_price is not None:
        print("소다코인의 현재 가격 : ", soda_price)
        if(soda_price<=buy_soda_price) :
            bithumb.buy_market_order("SOC", (krw/soda_price)*0.25)
            is_buy_soda=1
        
    con_price = float(all['data']['CON']['asks'][0]['price'])
    print("코넌의 현재 가격 : ", con_price)
    if con_price is not None:
        if(con_price<=buy_con_price) :
            bithumb.buy_market_order("CON", (krw/con_price)*0.25)
            is_buy_con=1

    lamba_price = float(all['data']['LAMB']['asks'][0]['price'])
    print("람바의 현재 가격 : ", lamba_price)
    if lamba_price is not None:
        if(lamba_price<=buy_lamba_price) :
            bithumb.buy_market_order("LAMB", (krw/lamba_price)*0.25)
            is_buy_lamba=1
        
    eforce_price = float(all['data']['WOZX']['asks'][0]['price'])
    print("이포스의 현재 가격 : ", eforce_price)
    if eforce_price is not None:
        if(eforce_price<=buy_eforce_price) :
            bithumb.buy_market_order("WOZX", (krw/eforce_price)*0.25)
            is_buy_eforce=1

    queenB_price = float(all['data']['QBZ']['asks'][0]['price'])
    print("퀸비의 현재 가격 : ", queenB_price)
    if queenB_price is not None:
        if(queenB_price<=buy_queenB_price) :
            bithumb.buy_market_order("QBZ", (krw/queenB_price)*0.25)
            is_buy_queenB=1
        
    ringX_price = float(all['data']['RINGX']['asks'][0]['price'])
    print("링엑스의 현재 가격 : ", ringX_price)
    if ringX_price is not None:
        if(ringX_price<=buy_ringX_price) :
            bithumb.buy_market_order("RINGX", (krw/ringX_price)*0.25)
            is_buy_ringX=1

    proton_price = float(all['data']['XPR']['asks'][0]['price'])
    print("프로톤의 현재 가격 : ", proton_price)
    if proton_price is not None:
        if(proton_price<=buy_proton_price) :
            bithumb.buy_market_order("XPR", (krw/proton_price)*0.25)
            is_buy_proton=1

    # 매수한 코인들 모두 지정가 매수
    if(is_buy_soda==1) :
        bithumb.sell_limit_order("SOC", round(buy_soda_price*yeild,2) , bithumb.get_balance("SOC")[0]-bithumb.get_balance("SOC")[1])
        is_buy_soda=0

    if(is_buy_con==1) :
        bithumb.sell_limit_order("CON", round(buy_con_price*yeild,3) , bithumb.get_balance("CON")[0]-bithumb.get_balance("CON")[1])
        is_buy_con=0

    if(is_buy_lamba==1) :
        bithumb.sell_limit_order("LAMB", round(buy_lamba_price*yeild,2) , bithumb.get_balance("LAMB")[0]-bithumb.get_balance("LAMB")[1])
        is_buy_lamba=0

    if(is_buy_eforce==1) :
        bithumb.sell_limit_order("WOZX", int(buy_eforce_price*yeild) , bithumb.get_balance("WOZX")[0]-bithumb.get_balance("WOZX")[1])
        is_buy_eforce=0

    if(is_buy_queenB==1) :
        bithumb.sell_limit_order("QBZ", round(buy_queenB_price*yeild,3) , bithumb.get_balance("QBZ")[0]-bithumb.get_balance("QBZ")[1])
        is_buy_queenB=0

    if(is_buy_ringX==1) :
        bithumb.sell_limit_order("RINGX", round(buy_ringX_price*yeild,2) , bithumb.get_balance("RINGX")[0]-bithumb.get_balance("RINGX")[1])
        is_buy_ringX=0

    if(is_buy_proton==1) :
        bithumb.sell_limit_order("XPR", round(buy_proton_price*yeild,3) , bithumb.get_balance("XPR")[0]-bithumb.get_balance("XPR")[1])
        is_buy_proton=0
    

    print("\n===================================\n")

        
