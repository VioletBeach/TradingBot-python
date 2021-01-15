# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb

f = open('C:\\Users\\ti641\\OneDrive\\바탕 화면\\sec_dir\\secret_key.txt', 'r')

con_key = "f86f6593322bceaf389748e714ba14d9"
sec_key = f.readline()
f.close()

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 코인별 구매 여부
is_buy_soda = 0
is_buy_con = 0
is_buy_lamba = 0
is_buy_eforce = 0
is_buy_queenB = 0
is_buy_ringX = 0

while(1) :

    # 원화 자산 조회
    krw = bithumb.get_balance("BTC")[2]
    print("현재 잔고는", int(krw), "원입니다.\n")

    # 저점 달성시 매수 [저점을 변수로 설정할까 고민중]
    soda_price = pybithumb.get_current_price("SOC")
    if soda_price is not None:
        print("소다코인의 현재 가격 : ", soda_price)
        if(soda_price<=12.05) :
            bithumb.buy_market_order("SOC", (krw/soda_price)*0.25)
            is_buy_soda=1
        
    con_price = pybithumb.get_current_price("CON")
    print("코넌의 현재 가격 : ", con_price)
    if con_price is not None:
        if(con_price<=3.915) :
            bithumb.buy_market_order("CON", (krw/con_price)*0.25)
            is_buy_con=1

    lamba_price = pybithumb.get_current_price("LAMB")
    print("람바의 현재 가격 : ", lamba_price)
    if lamba_price is not None:
        if(lamba_price<=16.62) :
            bithumb.buy_market_order("LAMB", (krw/lamba_price)*0.25)
            is_buy_lamba=1
        
    eforce_price = pybithumb.get_current_price("WOZX")
    print("이포스의 현재 가격 : ", eforce_price)
    if eforce_price is not None:
        if(eforce_price<=1326) :
            bithumb.buy_market_order("WOZX", (krw/eforce_price)*0.25)
            is_buy_eforce=1

    queenB_price = pybithumb.get_current_price("QBZ")
    print("퀸비의 현재 가격 : ", queenB_price)
    if queenB_price is not None:
        if(queenB_price<=5.102) :
            bithumb.buy_market_order("QBZ", (krw/queenB_price)*0.25)
            is_buy_queenB=1
        
    ringX_price = pybithumb.get_current_price("RINGX")
    print("링엑스의 현재 가격 : ", ringX_price)
    if ringX_price is not None:
        if(ringX_price<=32.22) :
            bithumb.buy_market_order("RINGX", (krw/ringX_price)*0.25)
            is_buy_ringX=1

    # 매수한 코인들 모두 지정가 매수
    if(is_buy_soda==1) :
        bithumb.sell_limit_order("SOC", 12.72 , bithumb.get_balance("SOC")[0]-bithumb.get_balance("SOC")[1])
        is_buy_soda=0

    if(is_buy_con==1) :
        bithumb.sell_limit_order("CON", 4.114 , bithumb.get_balance("CON")[0]-bithumb.get_balance("CON")[1])
        is_buy_con=0

    if(is_buy_lamba==1) :
        bithumb.sell_limit_order("LAMB", 17.43 , bithumb.get_balance("LAMB")[0]-bithumb.get_balance("LAMB")[1])
        is_buy_lamba=0

    if(is_buy_eforce==1) :
        bithumb.sell_limit_order("WOZX", 1392 , bithumb.get_balance("WOZX")[0]-bithumb.get_balance("WOZX")[1])
        is_buy_eforce=0

    if(is_buy_queenB==1) :
        bithumb.sell_limit_order("QBZ", 5.357 , bithumb.get_balance("QBZ")[0]-bithumb.get_balance("QBZ")[1])
        is_buy_queenB=0

    if(is_buy_ringX==1) :
        bithumb.sell_limit_order("RINGX", 33.83 , bithumb.get_balance("SOC")[0]-bithumb.get_balance("SOC")[1])
        is_buy_ringX=0
    

    print("\n===================================\n")

        
