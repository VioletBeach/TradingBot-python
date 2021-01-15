# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb

f = open('C:\\Users\\ti641\\OneDrive\\바탕 화면\\sec_dir\\secret_key.txt', 'r')

con_key = "f86f6593322bceaf389748e714ba14d9"
sec_key = f.readline()
f.close()

bithumb = pybithumb.Bithumb(con_key, sec_key)

while(1) :

    
    # 원화 자산 조회
    krw = bithumb.get_balance("BTC")[2]
    print("현재 잔고는", int(krw), "원입니다.\n")

    print("===================================")

        
