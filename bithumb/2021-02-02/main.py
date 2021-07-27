# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb
import time

con_key = "7199975e6406baa3e3bce7de2f77d2b9"
sec_key = "146f48bd8e829c0d460f8a8faa45f710"

bithumb = pybithumb.Bithumb(con_key, sec_key)

### 코인별 구매 가격 설정
buy_soda_price=9.477
buy_con_price=3.378
buy_lamba_price=15.64
buy_eforce_price=1204
buy_queenB_price=5.023
buy_ringX_price=33.04
buy_proton_price=4.233
buy_vsys_price=14.32
buy_gom2_price=11.04
buy_ae_price=106.8
buy_cennz_price=29.32
buy_mbl_price=1.531
buy_wemix_price=168.4
buy_eos_price=2745
buy_ipx_price=39.64
buy_fleta_price=4.574
buy_egg_price=4.461
buy_dad_price=155.6
buy_evz_price=9.582
buy_aoa_price=1.664
buy_adp_price=11.23
buy_mlk_price=154.4
buy_tmtg_price=4.314
buy_em_price=3.947
buy_rnt_price=11.14
buy_gxc_price=340.1
buy_xsr_price=3.422
buy_meta_price=8.512
buy_apm_price=11.64
buy_mix_price=1.941
buy_obsr_price=3.641
buy_dvc_price=37.16
buy_aion_price=71.24
buy_basic_price=6.038
buy_wet_price=4.214
buy_apix_price=52.47
buy_true_price=173.7

"""
소다코인 : 12.39
코넌 : 3.915
람바 : 13.62
이포스 : 1326
퀸비 : 5.102
링엑스 : 32.22
프로톤 4.233
브이시스템즈 : 14.11
고머니2 : 10.62
애터니티 : 102.6
센트럴리티 : 28.29
무비블록 : 1.471
위믹스 : 186.2
이오스 : 2645
타키온프로토콜 : 37.62
플레타 : 4.642

이브이지 : 10.48
오로라 : 1.662
어댑터 토큰 : 11.05

더마이다스터치골드=5.002
이마이너=3.824

"""

count = 0

# 코인별 구매 여부 - 매수한 후에 판매하기 위해서
is_buy_soda = 0
is_buy_con = 0
is_buy_lamba = 0
is_buy_eforce = 0
is_buy_queenB = 0
is_buy_ringX = 0
is_buy_proton = 0
is_buy_ae = 0
is_buy_cennz = 0
is_buy_vsys = 0
is_buy_mbl = 0
is_buy_gom2 = 0
is_buy_wemix = 0
is_buy_eos = 0
is_buy_ipx = 0
is_buy_fleta = 0
is_buy_tmtg = 0
is_buy_em = 0
is_buy_evz = 0
is_buy_aoa = 0
is_buy_adp = 0
is_buy_gxc = 0
is_buy_xsr = 0
is_buy_meta = 0
is_buy_apm = 0
is_buy_mix = 0
is_buy_obsr = 0
is_buy_dvc = 0
is_buy_aion = 0
is_buy_mlk = 0
is_buy_basic = 0
is_buy_egg = 0
is_buy_rnt = 0
is_buy_dad = 0
is_buy_wet = 0
is_buy_apix = 0
is_buy_ture = 0

# 코인별 판매 여부
is_sell_soda = 0
is_sell_con = 0
is_sell_lamba = 0
is_sell_eforce = 0
is_sell_queenB = 0
is_sell_ringX = 0
is_sell_proton = 0
is_sell_ae = 0
is_sell_cennz = 0
is_sell_vsys = 0
is_sell_mbl = 0
is_sell_gom2 = 0
is_sell_wemix = 0
is_sell_eos = 0
is_sell_ipx = 0
is_sell_fleta = 0
is_sell_tmtg = 0
is_sell_em = 0
is_sell_evz = 0
is_sell_aoa = 0
is_sell_adp = 0
is_sell_gxc = 0
is_sell_xsr = 0
is_sell_meta = 0
is_sell_apm = 0
is_sell_mix = 0
is_sell_obsr = 0
is_sell_dvc = 0
is_sell_aion = 0
is_sell_mlk = 0
is_sell_basic = 0
is_sell_egg = 0
is_sell_rnt = 0
is_sell_dad = 0
is_sell_wet = 0
is_sell_apix = 0
is_sell_true = 0

# 코인별 주문 변수 - 주문 존재 여부를 확인하기 위해서
order_soda = 0
order_con = 0
order_lamba = 0
order_eforce = 0
order_queenB = 0
order_ringX = 0
order_proton = 0
order_ae = 0
order_cennz = 0
order_vsys = 0
order_mbl = 0
order_gom2 = 0
order_wemix = 0
order_eos = 0
order_ipx = 0
order_fleta = 0
order_tmtg = 0
order_em = 0
order_evz = 0
order_aoa = 0
order_adp = 0

order_gxc = 0
order_xsr = 0
order_meta = 0
order_apm = 0
order_mix = 0
order_obsr = 0
order_dvc = 0
order_aion = 0
order_mlk = 0
order_basic = 0
order_egg = 0
order_rnt = 0
order_dad = 0
order_wet = 0
order_apix = 0
order_true = 0

# 매매 9회마다 잔고 조회는 한 번만 하기 위한 변수 (API 호출 최소화)
krw = bithumb.get_balance("BTC")[2]
count_lookup_balance=0

# 수익률
yeild = 205/200

while(1) :
    try :
        # 원화 자산 조회
        if(count_lookup_balance==10) :
            balance = bithumb.get_balance("BTC")
            if balance is None :
                balance = bithumb.get_balance("BTC")
                if balance is None : bithumb.get_balance("BTC")
            krw = balance[2]-balance[3]
            print("현재 잔고는", int(krw), "원입니다.\n")
            print("현재 잔고는", int(krw), "원입니다.\n")
            print("===================================\n")
            count_lookup_balance=-1
        count_lookup_balance+=1

        # 호가 불러오기
        all = pybithumb.get_orderbook("ALL")
        if all is None :
            all = pybithumb.get_orderbook("ALL")
            if all is None :
                all = pybithumb.get_orderbook("ALL")


        price = float(all['data']['XRP']['bids'][0]['price'])
        price2 = float(all['data']['XRP']['asks'][0]['price'])
        order=bithumb.buy_limit_order("XRP",  404.3, 53)
        bithumb.sell_limit_order("XRP",404.8, bithumb.get_balance("XRP")[0]-bithumb.get_balance("XRP")[1])

            
        print("\n===================================\n")
        time.sleep(0.01)

    except :
        continue
