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
buy_dvc_price=36.46
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
is_buy_true = 0

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

# 2000번 반복마다 로그인 하기 위한 변수
repeat_count=0

# 수익률
yeild = 205/200

# 시작 알림
start_count=0

# 매매 수량
buy_amount1=111732
buy_amount2=92976
buy_amount3=72764

while(1) :
    try :

        
        # 로그인
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

        # 저점 달성시 매수 [저점을 변수로 설정할까 고민중]
        soda_price = all['data']['SOC']['bids'][0]['price']
        soda_price=float(soda_price)
        if(is_sell_soda==0 and order_soda==0 and soda_price<=buy_soda_price*1.003) :
            order_soda=bithumb.buy_limit_order("SOC", buy_soda_price, (krw/soda_price)*0.5)
            print(order_soda)
        if(soda_price<buy_soda_price) :
            is_buy_soda=1
        if(order_soda!=0 and soda_price>=buy_soda_price*1.012) :
             bithumb.cancel_order(order_soda)
             order_soda=0
             is_buy_soda=0
        if(is_sell_soda==1) :
            if(float(all['data']['SOC']['asks'][0]['price'])>buy_soda_price*yeild) :
                is_sell_soda=0
                is_order_soda=0
            
        con_price = all['data']['CON']['bids'][0]['price']
        con_price=float(con_price)
        if(is_sell_con==0 and order_con==0 and con_price<=buy_con_price*1.003) :
            order_con=bithumb.buy_limit_order("CON", buy_con_price, (krw/con_price)*0.5)
            print(order_con)
        if(con_price<buy_con_price) :
            is_buy_con=1
        if(order_con!=0 and con_price>=buy_con_price*1.012) :
            bithumb.cancel_order(order_con)
            order_con=0
            is_buy_con=0
        if(is_sell_con==1) :
            if(float(all['data']['CON']['asks'][0]['price'])>buy_con_price*yeild) :
                is_sell_con=0
                is_order_con=0

        lamba_price = all['data']['LAMB']['bids'][0]['price']
        lamba_price=float(lamba_price)
        if(is_sell_lamba==0 and order_lamba==0 and lamba_price<=buy_lamba_price*1.003) :
            order_lamba=bithumb.buy_limit_order("LAMB", buy_lamba_price, (krw/lamba_price)*0.5)
            print(order_lamba)
        if(lamba_price<buy_lamba_price) :
            is_buy_lamba=1
        if(order_lamba!=0 and lamba_price>=buy_lamba_price*1.012) :
            bithumb.cancel_order(order_lamba)
            order_lamba=0
            is_buy_lamba=0
        if(is_sell_lamba==1) :
            if(float(all['data']['LAMB']['asks'][0]['price'])>buy_lamba_price*yeild) :
                is_sell_lamba=0
                is_order_lamba=0

        eforce_price = all['data']['WOZX']['bids'][0]['price']
        eforce_price=float(eforce_price)
        if(is_sell_eforce==0 and order_eforce==0 and eforce_price<=buy_eforce_price*1.003) :
            order_eforce=bithumb.buy_limit_order("WOZX", buy_eforce_price, (krw/eforce_price)*0.5)
            print(order_eforce)
        if(eforce_price<buy_eforce_price) :
            is_buy_eforce=1
        if(order_eforce!=0 and eforce_price>=buy_eforce_price*1.012) :
            bithumb.cancel_order(order_eforce)
            order_eforce=0
            is_buy_eforce=0
        if(is_sell_eforce==1) :
            if(float(all['data']['WOZX']['asks'][0]['price'])>buy_eforce_price*yeild) :
                is_sell_eforce=0
                is_order_eforce=0

        queenB_price = all['data']['QBZ']['bids'][0]['price']
        queenB_price=float(queenB_price)
        if(is_sell_queenB==0 and order_queenB==0 and queenB_price<=buy_queenB_price*1.003) :
            order_queenB=bithumb.buy_limit_order("QBZ", buy_queenB_price, (krw/queenB_price)*0.5)
            print(order_queenB)
        if(queenB_price<buy_queenB_price) :
            is_buy_queenB=1
        if(order_queenB!=0 and queenB_price>=buy_queenB_price*1.012) :
            bithumb.cancel_order(order_queenB)
            order_queenB=0
            is_buy_queenB=0
        if(is_sell_queenB==1) :
            if(float(all['data']['QBZ']['asks'][0]['price'])>buy_queenB_price*yeild) :
                is_sell_queenB=0
                is_order_queenB=0
        
            
        ringX_price = all['data']['RINGX']['bids'][0]['price']
        ringX_price=float(ringX_price)
        if(is_sell_ringX==0 and order_ringX==0 and ringX_price<=buy_ringX_price*1.003) :
            order_ringX=bithumb.buy_limit_order("RINGX", buy_ringX_price, (krw/ringX_price)*0.5)
            print(order_ringX)
        if(ringX_price<buy_ringX_price) :
            is_buy_ringX=1
        if(order_ringX!=0 and ringX_price>=buy_ringX_price*1.012) :
            bithumb.cancel_order(order_ringX)
            order_ringX=0
            is_buy_ringX=0
        if(is_sell_ringX==1) :
            if(float(all['data']['RINGX']['asks'][0]['price'])>buy_ringX_price*yeild) :
                is_sell_ringX=0
                is_order_ringX=0

        

        proton_price = all['data']['XPR']['bids'][0]['price']
        proton_price=float(proton_price)
        if(is_sell_proton==0 and order_proton==0 and proton_price<=buy_proton_price*1.003) :
            order_proton=bithumb.buy_limit_order("XPR", buy_proton_price, (krw/proton_price)*0.5)
            print(order_proton)
        if(proton_price<buy_proton_price) :
            is_buy_proton=1
        if(order_proton!=0 and proton_price>=buy_proton_price*1.012) :
            bithumb.cancel_order(order_proton)
            order_proton=0
            is_buy_proton=0
        if(is_sell_proton==1) :
            if(float(all['data']['XPR']['asks'][0]['price'])>buy_proton_price*yeild) :
                is_sell_proton=0
                is_order_proton=0

        ae_price = all['data']['AE']['bids'][0]['price']
        ae_price=float(ae_price)
        if(is_sell_ae==0 and order_ae==0 and ae_price<=buy_ae_price*1.003) :
            order_ae=bithumb.buy_limit_order("AE", buy_ae_price, (krw/ae_price)*0.5)
        if(ae_price<buy_ae_price) :
            is_buy_ae=1
        if(order_ae!=0 and ae_price>=buy_ae_price*1.012) :
            bithumb.cancel_order(order_ae)
            order_ae=0
            is_buy_ae=0
        if(is_sell_ae==1) :
            if(float(all['data']['AE']['asks'][0]['price'])>buy_ae_price*yeild) :
                is_sell_ae=0
                is_order_ae=0
                
        gom2_price = all['data']['GOM2']['bids'][0]['price']
        gom2_price=float(gom2_price)
        if(is_sell_gom2==0 and order_gom2==0 and gom2_price<=buy_gom2_price*1.003) :
            order_gom2=bithumb.buy_limit_order("GOM2", buy_gom2_price, (krw/gom2_price)*0.5)
        if(gom2_price<buy_gom2_price) :
            is_buy_gom2=1
        if(order_gom2!=0 and gom2_price>=buy_gom2_price*1.012) :
            bithumb.cancel_order(order_gom2)
            order_gom2=0
            is_buy_gom2=0
        if(is_sell_gom2==1) :
            if(float(all['data']['GOM2']['asks'][0]['price'])>buy_gom2_price*yeild) :
                is_sell_gom2=0
                is_order_gom2=0

        vsys_price = all['data']['VSYS']['bids'][0]['price']
        vsys_price=float(vsys_price)
        if(is_sell_vsys==0 and order_vsys==0 and vsys_price<=buy_vsys_price*1.003) :
            order_vsys=bithumb.buy_limit_order("VSYS", buy_vsys_price, (krw/vsys_price)*0.5)
        if(vsys_price<buy_vsys_price):
            is_buy_vsys=1
        if(order_vsys!=0 and vsys_price>=buy_vsys_price*1.012) :
            bithumb.cancel_order(order_vsys)
            order_vsys=0
            is_buy_vsys=0
        if(is_sell_vsys==1) :
            if(float(all['data']['VSYS']['asks'][0]['price'])>buy_vsys_price*yeild) :
                is_sell_vsys=0
                is_order_vsys=0

        
                
        cennz_price = all['data']['CENNZ']['bids'][0]['price']
        cennz_price=float(cennz_price)
        if(is_sell_cennz==0 and order_cennz==0 and cennz_price<=buy_cennz_price*1.003) :
            order_cennz=bithumb.buy_limit_order("CENNZ", buy_cennz_price, (krw/cennz_price)*0.5)
        if(cennz_price<buy_cennz_price) :
            is_buy_cennz=1
        if(order_cennz!=0 and cennz_price>=buy_cennz_price*1.012) :
            bithumb.cancel_order(order_cennz)
            order_cennz=0
            is_buy_cennz=0
        if(is_sell_cennz==1) :
            if(float(all['data']['CENNZ']['asks'][0]['price'])>buy_cennz_price*yeild) :
                is_sell_cennz=0
                is_order_cennz=0

        mbl_price = all['data']['MBL']['bids'][0]['price']
        mbl_price=float(mbl_price)
        if(is_sell_mbl==0 and order_mbl==0 and mbl_price<=buy_mbl_price*1.003) :
            order_mbl=bithumb.buy_limit_order("MBL", buy_mbl_price, (krw/mbl_price)*0.5)
        if(mbl_price<buy_mbl_price):
            is_buy_mbl=1
        if(order_mbl!=0 and mbl_price>=buy_mbl_price*1.012) :
            bithumb.cancel_order(order_mbl)
            order_mbl=0
            is_buy_mbl=0
        if(is_sell_mbl==1) :
            if(float(all['data']['MBL']['asks'][0]['price'])>buy_mbl_price*yeild) :
                is_sell_mbl=0
                is_order_mbl=0

        eos_price = all['data']['EOS']['bids'][0]['price']
        eos_price=float(eos_price)
        if(is_sell_eos==0 and order_eos==0 and eos_price<=buy_eos_price*1.003) :
            order_eos=bithumb.buy_limit_order("EOS", buy_eos_price, (krw/eos_price)*0.5)
        if(eos_price<buy_eos_price):
            is_buy_eos=1
        if(order_eos!=0 and eos_price>=buy_eos_price*1.012) :
             bithumb.cancel_order(order_eos)
             order_eos=0
             is_buy_eos=0
        if(is_sell_eos==1) :
            if(float(all['data']['EOS']['asks'][0]['price'])>buy_eos_price*yeild) :
                is_sell_eos=0
                is_order_eos=0

        ipx_price = all['data']['IPX']['bids'][0]['price']
        ipx_price=float(ipx_price)
        if(is_sell_ipx==0 and order_ipx==0 and ipx_price<=buy_ipx_price*1.003) :
            order_ipx=bithumb.buy_limit_order("IPX", buy_ipx_price, (krw/ipx_price)*0.5)
        if(ipx_price<buy_ipx_price):
            is_buy_ipx=1
        if(order_ipx!=0 and ipx_price>=buy_ipx_price*1.012) :
             bithumb.cancel_order(order_ipx)
             order_ipx=0
             is_buy_ipx=0
        if(is_sell_ipx==1) :
            if(float(all['data']['IPX']['asks'][0]['price'])>buy_ipx_price*yeild) :
                is_sell_ipx=0
                is_order_ipx=0
        

        fleta_price = all['data']['FLETA']['bids'][0]['price']
        fleta_price=float(fleta_price)
        if(is_sell_fleta==0 and order_fleta==0 and fleta_price<=buy_fleta_price*1.003) :
            order_fleta=bithumb.buy_limit_order("FLETA", buy_fleta_price, (krw/fleta_price)*0.5)
            print(order_fleta)
        if(fleta_price<buy_fleta_price):
            is_buy_fleta=1
        if(order_fleta!=0 and fleta_price>=buy_fleta_price*1.012) :
             bithumb.cancel_order(order_fleta)
             order_fleta=0
             is_buy_fleta=0
        if(is_sell_fleta==1) :
            if(float(all['data']['FLETA']['asks'][0]['price'])>buy_fleta_price*yeild) :
                is_sell_fleta=0
                is_order_fleta=0
        
        wemix_price = all['data']['WEMIX']['bids'][0]['price']
        wemix_price=float(wemix_price)
        if(is_sell_wemix==0 and order_wemix==0 and wemix_price<=buy_wemix_price*1.003) :
            order_wemix=bithumb.buy_limit_order("WEMIX", buy_wemix_price, (krw/wemix_price)*0.5)
            print(order_wemix)
        if(wemix_price<buy_wemix_price):
            is_buy_wemix=1
        if(order_wemix!=0 and wemix_price>=buy_wemix_price*1.012) :
            bithumb.cancel_order(order_wemix)
            order_wemix=0
            is_buy_wemix=0
        if(is_sell_wemix==1) :
            if(float(all['data']['WEMIX']['asks'][0]['price'])>buy_wemix_price*yeild) :
                is_sell_wemix=0
                is_order_wemix=0
        
        # 매수한 코인들 모두 지정가 매도
        if(is_buy_soda==1) :
            bithumb.sell_limit_order("SOC", round(buy_soda_price*yeild,3) , bithumb.get_balance("SOC")[0]-bithumb.get_balance("SOC")[1])
            is_buy_soda=0
            is_sell_soda=1

        if(is_buy_con==1) :
            bithumb.sell_limit_order("CON", round(buy_con_price*yeild,3) , bithumb.get_balance("CON")[0]-bithumb.get_balance("CON")[1])
            is_buy_con=0
            is_sell_con=1

        if(is_buy_lamba==1) :
            bithumb.sell_limit_order("LAMB", round(buy_lamba_price*yeild,2) , bithumb.get_balance("LAMB")[0]-bithumb.get_balance("LAMB")[1])
            is_buy_lamba=0
            is_sell_lamba=1

        if(is_buy_eforce==1) :
            bithumb.sell_limit_order("WOZX", int(buy_eforce_price*yeild) , bithumb.get_balance("WOZX")[0]-bithumb.get_balance("WOZX")[1])
            is_buy_eforce=0
            is_sell_eforce=1

        if(is_buy_queenB==1) :
            bithumb.sell_limit_order("QBZ", round(buy_queenB_price*yeild,3) , bithumb.get_balance("QBZ")[0]-bithumb.get_balance("QBZ")[1])
            is_buy_queenB=0
            is_sell_queenB=1

        if(is_buy_ringX==1) :
            bithumb.sell_limit_order("RINGX", round(buy_ringX_price*yeild,2) , bithumb.get_balance("RINGX")[0]-bithumb.get_balance("RINGX")[1])
            is_buy_ringX=0
            is_sell_ringX=1

        if(is_buy_proton==1) :
            bithumb.sell_limit_order("XPR", round(buy_proton_price*yeild,3) , bithumb.get_balance("XPR")[0]-bithumb.get_balance("XPR")[1])
            is_buy_proton=0
            is_sell_proton=1

        if(is_buy_ae==1) :
            bithumb.sell_limit_order("AE", round(buy_ae_price*yeild,1) , bithumb.get_balance("AE")[0]-bithumb.get_balance("AE")[1])
            is_buy_ae=0
            is_sell_ae=1
            
        if(is_buy_gom2==1) :
            bithumb.sell_limit_order("GOM2", round(buy_gom2_price*yeild,2) , bithumb.get_balance("GOM2")[0]-bithumb.get_balance("GOM2")[1])
            is_buy_gom2=0
            is_sell_gom2=1
            
        if(is_buy_vsys==1) :
            bithumb.sell_limit_order("VSYS", round(buy_vsys_price*yeild,3) , bithumb.get_balance("VSYS")[0]-bithumb.get_balance("VSYS")[1])
            is_buy_vsys=0
            is_sell_vsys=1
            
        if(is_buy_cennz==1) :
            bithumb.sell_limit_order("CENNZ", round(buy_cennz_price*yeild,2) , bithumb.get_balance("CENNZ")[0]-bithumb.get_balance("CENNZ")[1])
            is_buy_cennz=0
            is_sell_cennz=1
            
        if(is_buy_mbl==1) :
            bithumb.sell_limit_order("MBL", round(buy_mbl_price*yeild,3) , bithumb.get_balance("MBL")[0]-bithumb.get_balance("MBL")[1])
            is_buy_mbl=0
            is_sell_mbl=1
            
        if(is_buy_eos==1) :
            bithumb.sell_limit_order("EOS", int(buy_eos_price*yeild) , bithumb.get_balance("EOS")[0]-bithumb.get_balance("EOS")[1])
            is_buy_eos=0
            is_sell_eos=1
            
        if(is_buy_wemix==1) :
            bithumb.sell_limit_order("WEMIX", 190.5 , bithumb.get_balance("WEMIX")[0]-bithumb.get_balance("WEMIX")[1])
            is_buy_wemix=0
            is_sell_wemix=1

        if(is_buy_ipx==1) :
            bithumb.sell_limit_order("IPX", round(buy_ipx_price*yeild,2) , bithumb.get_balance("IPX")[0]-bithumb.get_balance("IPX")[1])
            is_buy_ipx=0
            is_sell_ipx=1

        if(is_buy_fleta==1) :
            bithumb.sell_limit_order("FLETA", round(buy_fleta_price*yeild,3) , bithumb.get_balance("FLETA")[0]-bithumb.get_balance("FLETA")[1])
            is_buy_fleta=0
            is_sell_fleta=1


        # 단기 설정 코인
        
        tmtg_price = all['data']['TMTG']['bids'][0]['price']
        tmtg_price=float(tmtg_price)
        if(is_sell_tmtg==0 and order_tmtg==0 and tmtg_price<=buy_tmtg_price*1.003) :
            order_tmtg=bithumb.buy_limit_order("TMTG", buy_tmtg_price, (krw/tmtg_price)*0.5)
            print(order_tmtg)
        if(tmtg_price<buy_tmtg_price):
            is_buy_tmtg=1
        if(order_tmtg!=0 and tmtg_price>=buy_tmtg_price*1.012) :
             bithumb.cancel_order(order_tmtg)
             order_tmtg=0
             is_buy_tmtg=0
        if(is_buy_tmtg==1) :
            bithumb.sell_limit_order("TMTG", round(buy_tmtg_price*yeild,3) , bithumb.get_balance("TMTG")[0]-bithumb.get_balance("TMTG")[1])
            is_buy_tmtg=0
            is_sell_tmtg=1
        if(is_sell_tmtg==1) :
            if(float(all['data']['TMTG']['asks'][0]['price'])>buy_tmtg_price*yeild) :
                is_sell_tmtg=0
                is_order_tmtg=0

        em_price = all['data']['EM']['bids'][0]['price']
        em_price=float(em_price)
        if(is_sell_em==0 and order_em==0 and em_price<=buy_em_price*1.003) :
            order_em=bithumb.buy_limit_order("EM", buy_em_price, (krw/em_price)*0.5)
        if(em_price<buy_em_price):
            is_buy_em=1
        if(order_em!=0 and em_price>=buy_em_price*1.012) :
             bithumb.cancel_order(order_em)
             order_em=0
             is_buy_em=0
        if(is_buy_em==1) :
            bithumb.sell_limit_order("EM", round(buy_em_price*yeild,3) , bithumb.get_balance("EM")[0]-bithumb.get_balance("EM")[1])
            is_buy_em=0
            is_sell_em=1
        if(is_sell_em==1) :
            if(float(all['data']['EM']['asks'][0]['price'])>buy_em_price*yeild) :
                is_sell_em=0
                is_order_em=0

        evz_price = all['data']['EVZ']['bids'][0]['price']
        evz_price=float(evz_price)
        if(is_sell_evz==0 and order_evz==0 and evz_price<=buy_evz_price*1.003) :
            order_evz=bithumb.buy_limit_order("EVZ", buy_evz_price, (krw/evz_price)*0.5)
        if(evz_price<buy_evz_price):
            is_buy_evz=1
        if(order_evz!=0 and evz_price>=buy_evz_price*1.012) :
             bithumb.cancel_order(order_evz)
             order_evz=0
             is_buy_evz=0
        if(is_buy_evz==1) :
            bithumb.sell_limit_order("EVZ", round(buy_evz_price*yeild,3) , bithumb.get_balance("EVZ")[0]-bithumb.get_balance("EVZ")[1])
            is_buy_evz=0
            is_sell_evz=1
        if(is_sell_evz==1) :
            if(float(all['data']['EVZ']['asks'][0]['price'])>buy_evz_price*yeild) :
                is_sell_evz=0
                is_order_evz=0
        aoa_price = all['data']['AOA']['bids'][0]['price']
        aoa_price=float(aoa_price)
        if(is_sell_aoa==0 and order_aoa==0 and aoa_price<=buy_aoa_price*1.003) :
            order_aoa=bithumb.buy_limit_order("AOA", buy_aoa_price, (krw/aoa_price)*0.5)
        if(aoa_price<buy_aoa_price):
            is_buy_aoa=1
        if(order_aoa!=0 and aoa_price>=buy_aoa_price*1.012) :
             bithumb.cancel_order(order_aoa)
             order_aoa=0
             is_buy_aoa=0
        if(is_buy_aoa==1) :
            bithumb.sell_limit_order("AOA", round(buy_aoa_price*yeild,3) , bithumb.get_balance("AOA")[0]-bithumb.get_balance("AOA")[1])
            is_buy_aoa=0
            is_sell_aoa=1
        if(is_sell_aoa==1) :
            if(float(all['data']['AOA']['asks'][0]['price'])>buy_aoa_price*yeild) :
                is_sell_aoa=0
                is_order_aoa=0

        adp_price = all['data']['ADP']['bids'][0]['price']
        adp_price=float(adp_price)
        if(is_sell_adp==0 and order_adp==0 and adp_price<=buy_adp_price*1.003) :
            order_adp=bithumb.buy_limit_order("ADP", buy_adp_price, (krw/adp_price)*0.5)
        if(adp_price<buy_adp_price):
            is_buy_adp=1
        if(order_adp!=0 and adp_price>=buy_adp_price*1.012) :
             bithumb.cancel_order(order_adp)
             order_adp=0
             is_buy_adp=0
        if(is_buy_adp==1) :
            bithumb.sell_limit_order("ADP", round(buy_adp_price*yeild,2) , bithumb.get_balance("ADP")[0]-bithumb.get_balance("ADP")[1])
            is_buy_adp=0
            is_sell_adp=1
        if(is_sell_adp==1) :
            if(float(all['data']['ADP']['asks'][0]['price'])>buy_adp_price*yeild) :
                is_sell_adp=0
                is_order_adp=0

        gxc_price = all['data']['GXC']['bids'][0]['price']
        gxc_price=float(gxc_price)
        if(is_sell_gxc==0 and order_gxc==0 and gxc_price<=buy_gxc_price*1.003) :
            order_gxc=bithumb.buy_limit_order("GXC", buy_gxc_price, (krw/gxc_price)*0.5)
        if(gxc_price<buy_gxc_price):
            is_buy_gxc=1
        if(order_gxc!=0 and gxc_price>=buy_gxc_price*1.012) :
             bithumb.cancel_order(order_gxc)
             order_gxc=0
             is_buy_gxc=0
        if(is_buy_gxc==1) :
            bithumb.sell_limit_order("GXC", round(buy_gxc_price*yeild,1) , bithumb.get_balance("GXC")[0]-bithumb.get_balance("GXC")[1])
            is_buy_gxc=0
            is_sell_gxc=1
        if(is_sell_gxc==1) :
            if(float(all['data']['GXC']['asks'][0]['price'])>buy_gxc_price*yeild) :
                is_sell_gxc=0
                is_order_gxc=0
            
        xsr_price = all['data']['XSR']['bids'][0]['price']
        xsr_price=float(xsr_price)
        if(is_sell_xsr==0 and order_xsr==0 and xsr_price<=buy_xsr_price*1.003) :
            order_xsr=bithumb.buy_limit_order("XSR", buy_xsr_price, (krw/xsr_price)*0.5)
        if(xsr_price<buy_xsr_price):
            is_buy_xsr=1
        if(order_xsr!=0 and xsr_price>=buy_xsr_price*1.012) :
             bithumb.cancel_order(order_xsr)
             order_xsr=0
             is_buy_xsr=0
        if(is_buy_xsr==1) :
            bithumb.sell_limit_order("XSR", round(buy_xsr_price*yeild,3) , bithumb.get_balance("XSR")[0]-bithumb.get_balance("XSR")[1])
            is_buy_xsr=0
            is_sell_xsr=1
        if(is_sell_xsr==1) :
            if(float(all['data']['XSR']['asks'][0]['price'])>buy_xsr_price*yeild) :
                is_sell_xsr=0
                is_order_xsr=0
        

        meta_price = all['data']['META']['bids'][0]['price']
        meta_price=float(meta_price)
        if(is_sell_meta==0 and order_meta==0 and meta_price<=buy_meta_price*1.003) :
            order_meta=bithumb.buy_limit_order("META", buy_meta_price, (krw/meta_price)*0.5)
        if(meta_price<buy_meta_price):
            is_buy_meta=1
        if(order_meta!=0 and meta_price>=buy_meta_price*1.012) :
             bithumb.cancel_order(order_meta)
             order_meta=0
             is_buy_meta=0
        if(is_buy_meta==1) :
            bithumb.sell_limit_order("META", round(buy_meta_price*yeild,3) , bithumb.get_balance("META")[0]-bithumb.get_balance("META")[1])
            is_buy_meta=0
            is_sell_meta=1
        if(is_sell_meta==1) :
            if(float(all['data']['META']['asks'][0]['price'])>buy_meta_price*yeild) :
                is_sell_meta=0
                is_order_meta=0
        
        apm_price = all['data']['APM']['bids'][0]['price']
        apm_price=float(apm_price)
        if(is_sell_apm==0 and order_apm==0 and apm_price<=buy_apm_price*1.003) :
            order_apm=bithumb.buy_limit_order("APM", buy_apm_price, (krw/apm_price)*0.5)
        if(apm_price<buy_apm_price):
            is_buy_apm=1
        if(order_apm!=0 and apm_price>=buy_apm_price*1.012) :
             bithumb.cancel_order(order_apm)
             order_apm=0
             is_buy_apm=0
        if(is_buy_apm==1) :
            bithumb.sell_limit_order("APM", round(buy_apm_price*yeild,2) , bithumb.get_balance("APM")[0]-bithumb.get_balance("APM")[1])
            is_buy_apm=0
            is_sell_apm=1
        if(is_sell_apm==1) :
            if(float(all['data']['APM']['asks'][0]['price'])>buy_apm_price*yeild) :
                is_sell_apm=0
                is_order_apm=0

        mix_price = all['data']['MIX']['bids'][0]['price']
        mix_price=float(mix_price)
        if(is_sell_mix==0 and order_mix==0 and mix_price<=buy_mix_price*1.003) :
            order_mix=bithumb.buy_limit_order("MIX", buy_mix_price, (krw/mix_price)*0.5)
        if(mix_price<buy_mix_price):
            is_buy_mix=1
        if(order_mix!=0 and mix_price>=buy_mix_price*1.012) :
             bithumb.cancel_order(order_mix)
             order_mix=0
             is_buy_mix=0
        if(is_buy_mix==1) :
            bithumb.sell_limit_order("MIX", round(buy_mix_price*yeild,3) , bithumb.get_balance("MIX")[0]-bithumb.get_balance("MIX")[1])
            is_buy_mix=0
            is_sell_mix=1
        if(is_sell_mix==1) :
            if(float(all['data']['MIX']['asks'][0]['price'])>buy_mix_price*yeild) :
                is_sell_mix=0
                is_order_mix=0

        obsr_price = all['data']['OBSR']['bids'][0]['price']
        obsr_price=float(obsr_price)
        if(is_sell_obsr==0 and order_obsr==0 and obsr_price<=buy_obsr_price*1.003) :
            order_obsr=bithumb.buy_limit_order("OBSR", buy_obsr_price, (krw/obsr_price)*0.5)
            print(order_obsr)
        if(obsr_price<buy_obsr_price):
            is_buy_obsr=1
        if(order_obsr!=0 and obsr_price>=buy_obsr_price*1.012) :
             bithumb.cancel_order(order_obsr)
             order_obsr=0
             is_buy_obsr=0
        if(is_buy_obsr==1) :
            bithumb.sell_limit_order("OBSR", round(buy_obsr_price*yeild,3) , bithumb.get_balance("OBSR")[0]-bithumb.get_balance("OBSR")[1])
            is_buy_obsr=0
            is_sell_obsr=1
        if(is_sell_obsr==1) :
            if(float(all['data']['OBSR']['asks'][0]['price'])>buy_obsr_price*yeild) :
                is_sell_obsr=0
                is_order_obsr=0

        dvc_price = all['data']['DVC']['bids'][0]['price']
        dvc_price=float(dvc_price)
        if(is_sell_dvc==0 and order_dvc==0 and dvc_price<=buy_dvc_price*1.003) :
            order_dvc=bithumb.buy_limit_order("DVC", buy_dvc_price, (krw/dvc_price)*0.5)
            print(order_dvc)
        if(dvc_price<buy_dvc_price):
            is_buy_dvc=1
        if(order_dvc!=0 and dvc_price>=buy_dvc_price*1.012) :
             bithumb.cancel_order(order_dvc)
             order_dvc=0
             is_buy_dvc=0
        if(is_buy_dvc==1) :
            bithumb.sell_limit_order("DVC", round(buy_dvc_price*yeild,2) , bithumb.get_balance("DVC")[0]-bithumb.get_balance("DVC")[1])
            is_buy_dvc=0
            is_sell_dvc=1
        if(is_sell_dvc==1) :
            if(float(all['data']['DVC']['asks'][0]['price'])>buy_dvc_price*yeild) :
                is_sell_dvc=0
                is_order_dvc=0

        aion_price = all['data']['AION']['bids'][0]['price']
        aion_price=float(aion_price)
        if(is_sell_aion==0 and order_aion==0 and aion_price<=buy_aion_price*1.003) :
            order_aion=bithumb.buy_limit_order("AION", buy_aion_price, (krw/aion_price)*0.5)
        if(aion_price<buy_aion_price):
            is_buy_aion=1
        if(order_aion!=0 and aion_price>=buy_aion_price*1.012) :
             bithumb.cancel_order(order_aion)
             order_aion=0
             is_buy_aion=0
        if(is_buy_aion==1) :
            bithumb.sell_limit_order("AION", round(buy_aion_price*yeild,2) , bithumb.get_balance("AION")[0]-bithumb.get_balance("AION")[1])
            is_buy_aion=0
            is_sell_aion=1
        if(is_sell_aion==1) :
            if(float(all['data']['AION']['asks'][0]['price'])>buy_aion_price*yeild) :
                is_sell_aion=0
                is_order_aion=0
        
        mlk_price = all['data']['MLK']['bids'][0]['price']
        mlk_price=float(mlk_price)
        if(is_sell_mlk==0 and order_mlk==0 and mlk_price<=buy_mlk_price*1.003) :
            order_mlk=bithumb.buy_limit_order("MLK", buy_mlk_price, (krw/mlk_price)*0.5)
        if(mlk_price<buy_mlk_price) :
            is_buy_mlk=1
        if(order_mlk!=0 and mlk_price>=buy_mlk_price*1.012) :
            bithumb.cancel_order(order_mlk)
            order_mlk=0
            is_buy_mlk=0
        if(is_buy_mlk==1) :
            bithumb.sell_limit_order("MLK", round(buy_mlk_price*yeild,1), bithumb.get_balance("MLK")[0]-bithumb.get_balance("MLK")[1])
            is_buy_mlk=0
            is_sell_mlk=1
        if(is_sell_mlk==1) :
            if(float(all['data']['MLK']['asks'][0]['price'])>buy_mlk_price*yeild) :
                is_sell_mlk=0
                is_order_mlk=0

        basic_price = all['data']['BASIC']['bids'][0]['price']
        basic_price=float(basic_price)
        if(is_sell_basic==0 and order_basic==0 and basic_price<=buy_basic_price*1.003) :
            order_basic=bithumb.buy_limit_order("BASIC", buy_basic_price, (krw/basic_price)*0.5)
            print(order_basic)
        if(basic_price<buy_basic_price) :
            is_buy_basic=1
        if(order_basic!=0 and basic_price>=buy_basic_price*1.012) :
            bithumb.cancel_order(order_basic)
            order_basic=0
            is_buy_basic=0
        if(is_buy_basic==1) :
            bithumb.sell_limit_order("BASIC", round(buy_basic_price*yeild,3), bithumb.get_balance("BASIC")[0]-bithumb.get_balance("BASIC")[1])
            is_buy_basic=0
            is_sell_basic=1
        if(is_sell_basic==1) :
            if(float(all['data']['BASIC']['asks'][0]['price'])>buy_basic_price*yeild) :
                is_sell_basic=0
                is_order_basic=0

        egg_price = all['data']['EGG']['bids'][0]['price']
        egg_price=float(egg_price)
        if(is_sell_egg==0 and order_egg==0 and egg_price<=buy_egg_price*1.003) :
            order_egg=bithumb.buy_limit_order("EGG", buy_egg_price, (krw/egg_price)*0.5)
        if(egg_price<buy_egg_price) :
            is_buy_egg=1
        if(order_egg!=0 and egg_price>=buy_egg_price*1.012) :
            bithumb.cancel_order(order_egg)
            order_egg=0
            is_buy_egg=0
        if(is_buy_egg==1) :
            bithumb.sell_limit_order("EGG", round(buy_egg_price*yeild,3), bithumb.get_balance("EGG")[0]-bithumb.get_balance("EGG")[1])
            is_buy_egg=0
            is_sell_egg=1
        if(is_sell_egg==1) :
            if(float(all['data']['EGG']['asks'][0]['price'])>buy_egg_price*yeild) :
                is_sell_egg=0
                is_order_egg=0

        rnt_price = all['data']['RNT']['bids'][0]['price']
        rnt_price=float(rnt_price)
        if(is_sell_rnt==0 and order_rnt==0 and rnt_price<=buy_rnt_price*1.003) :
            order_rnt=bithumb.buy_limit_order("RNT", buy_rnt_price, (krw/rnt_price)*0.5)
        if(rnt_price<buy_rnt_price) :
            is_buy_rnt=1
        if(order_rnt!=0 and rnt_price>=buy_rnt_price*1.012) :
            bithumb.cancel_order(order_rnt)
            order_rnt=0
            is_buy_rnt=0
        if(is_buy_rnt==1) :
            bithumb.sell_limit_order("RNT", round(buy_rnt_price*yeild,2), bithumb.get_balance("RNT")[0]-bithumb.get_balance("RNT")[1])
            is_buy_rnt=0
            is_sell_rnt=1
        if(is_sell_rnt==1) :
            if(float(all['data']['RNT']['asks'][0]['price'])>buy_rnt_price*yeild) :
                is_sell_rnt=0
                is_order_rnt=0

        dad_price = all['data']['DAD']['bids'][0]['price']
        dad_price=float(dad_price)
        if(is_sell_dad==0 and order_dad==0 and dad_price<=buy_dad_price*1.003) :
            order_dad=bithumb.buy_limit_order("DAD", buy_dad_price, (krw/dad_price)*0.5)
        if(dad_price<buy_dad_price) :
            is_buy_dad=1
        if(order_dad!=0 and dad_price>=buy_dad_price*1.012) :
            bithumb.cancel_order(order_dad)
            order_dad=0
            is_buy_dad=0
        if(is_buy_dad==1) :
            bithumb.sell_limit_order("DAD", round(buy_dad_price*yeild,1), bithumb.get_balance("DAD")[0]-bithumb.get_balance("DAD")[1])
            is_buy_dad=0
            is_sell_dad=1
        if(is_sell_dad==1) :
            if(float(all['data']['DAD']['asks'][0]['price'])>buy_dad_price*yeild) :
                is_sell_dad=0
                is_order_dad=0

        wet_price = all['data']['WET']['bids'][0]['price']
        wet_price=float(wet_price)
        if(is_sell_wet==0 and order_wet==0 and wet_price<=buy_wet_price*1.003) :
            order_wet=bithumb.buy_limit_order("WET", buy_wet_price, (krw/wet_price)*0.5)
        if(wet_price<buy_wet_price) :
            is_buy_wet=1
        if(order_wet!=0 and wet_price>=buy_wet_price*1.012) :
            bithumb.cancel_order(order_wet)
            order_wet=0
            is_buy_wet=0
        if(is_buy_wet==1) :
            bithumb.sell_limit_order("WET", round(buy_wet_price*yeild,3), bithumb.get_balance("WET")[0]-bithumb.get_balance("WET")[1])
            is_buy_wet=0
            is_sell_wet=1
        if(is_sell_wet==1) :
            if(float(all['data']['WET']['asks'][0]['price'])>buy_wet_price*yeild) :
                is_sell_wet=0
                is_order_wet=0

        apix_price = all['data']['APIX']['bids'][0]['price']
        apix_price=float(apix_price)
        if(is_sell_apix==0 and order_apix==0 and apix_price<=buy_apix_price*1.003) :
            order_apix=bithumb.buy_limit_order("APIX", buy_apix_price, (krw/apix_price)*0.5)
        if(apix_price<buy_apix_price) :
            is_buy_apix=1
        if(order_apix!=0 and apix_price>=buy_apix_price*1.012) :
            bithumb.cancel_order(order_apix)
            order_apix=0
            is_buy_apix=0
        if(is_buy_apix==1) :
            bithumb.sell_limit_order("APIX", round(buy_apix_price*yeild,2), bithumb.get_balance("APIX")[0]-bithumb.get_balance("APIX")[1])
            is_buy_apix=0
            is_sell_apix=1
        if(is_sell_apix==1) :
            if(float(all['data']['APIX']['asks'][0]['price'])>buy_apix_price*yeild) :
                is_sell_apix=0
                is_order_apix=0
        
        true_price = all['data']['TRUE']['bids'][0]['price']
        true_price=float(true_price)
        if(is_sell_true==0 and order_true==0 and true_price<=buy_true_price*1.003) :
            order_true=bithumb.buy_limit_order("TRUE", buy_true_price, (krw/true_price)*0.5)
        if(true_price<buy_true_price) :
            is_buy_true=1
        if(order_true!=0 and true_price>=buy_true_price*1.012) :
            bithumb.cancel_order(order_true)
            order_true=0
            is_buy_true=0
        if(is_buy_true==1) :
            bithumb.sell_limit_order("TRUE", round(buy_true_price*yeild,1), bithumb.get_balance("TRUE")[0]-bithumb.get_balance("TRUE")[1])
            is_buy_true=0
            is_sell_true=1
            
        if(is_sell_true==1) :
            if(float(all['data']['TRUE']['asks'][0]['price'])>buy_true_price*yeild) :
                is_sell_true=0
                is_order_true=0

        if(start_count==0) :
            print("start")
            start_count=1
            
        time.sleep(0.5)

    except :
        print("에러 발생")
        continue
