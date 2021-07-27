# Bithumb 자동 매수 트레이딩 봇 By VioletBeach [재헌]

import pybithumb
import time

con_key = "7199975e6406baa3e3bce7de2f77d2b9"
sec_key = "146f48bd8e829c0d460f8a8faa45f710"

bithumb = pybithumb.Bithumb(con_key, sec_key)

### 코인별 구매 가격 설정
buy_soda_price=12.39
buy_con_price=3.781
buy_lamba_price=16.62
buy_eforce_price=1326
buy_queenB_price=5.102
buy_ringX_price=32.72
buy_proton_price=4.533
buy_vsys_price=14.32
buy_gom2_price=10.62
buy_ae_price=104.8
buy_cennz_price=29.52
buy_mbl_price=1.471
buy_wemix_price=186.2
buy_eos_price=2745
buy_ipx_price=37.62
buy_fleta_price=4.642

buy_evz_price=10.48
buy_aoa_price=1.662
buy_adp_price=11.05


buy_tmtg_price=4.583
buy_em_price=3.824


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

# 매매 9회마다 잔고 조회는 한 번만 하기 위한 변수 (API 호출 최소화)
krw = bithumb.get_balance("BTC")[2]
count_lookup_balance=0

# 수익률
yeild = 104/100
yeild2 = 205/200

while(1) :
    
    # 원화 자산 조회
    if(count_lookup_balance==10) :
        balance = bithumb.get_balance("BTC")
        if balance is None :
            balance = bithumb.get_balanace("BTC")
        krw=balance[2]
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

    # 저점 달성시 매수 [저점을 변수로 설정할까 고민중]
    soda_price = all['data']['SOC']['bids'][0]['price']
    soda_price=float(soda_price)
    print("소다코인의 현재 가격 : ", soda_price)
    if(order_soda==0 and soda_price<=buy_soda_price*1.003) :
        order_soda=bithumb.buy_limit_order("SOC", buy_soda_price, (krw/soda_price)*0.5)
        is_buy_soda=1
    if(order_soda!=0 and soda_price>=buy_soda_price*1.006) :
         bithumb.cancel_order(order_soda)
         order_soda=0
        
    con_price = all['data']['CON']['bids'][0]['price']
    print("코넌의 현재 가격 : ", con_price)
    con_price=float(con_price)
    if(order_con==0 and con_price<=buy_con_price*1.003) :
        order_con=bithumb.buy_limit_order("CON", buy_con_price, (krw/con_price)*0.5)
        is_buy_con=1
    if(order_con!=0 and con_price>=buy_con_price*1.006) :
        bithumb.cancel_order(order_con)
        order_con=0

    lamba_price = all['data']['LAMB']['bids'][0]['price']
    print("람바의 현재 가격 : ", lamba_price)
    lamba_price=float(lamba_price)
    if(order_lamba==0 and lamba_price<=buy_lamba_price*1.003) :
        order_lamba=bithumb.buy_limit_order("LAMB", buy_lamba_price, (krw/lamba_price)*0.5)
        is_buy_lamba=1
    if(order_lamba!=0 and lamba_price>=buy_lamba_price*1.006) :
        bithumb.cancel_order(order_lamba)
        order_lamba=0
        
    eforce_price = all['data']['WOZX']['bids'][0]['price']
    print("이포스의 현재 가격 : ", eforce_price)
    eforce_price=float(eforce_price)
    if(order_eforce==0 and eforce_price<=buy_eforce_price*1.003) :
        order_eforce=bithumb.buy_limit_order("WOZX", buy_eforce_price, (krw/eforce_price)*0.5)
        is_buy_eforce=1
    if(order_eforce!=0 and eforce_price>=buy_eforce_price*1.006) :
        bithumb.cancel_order(order_eforce)
        order_eforce=0

    queenB_price = all['data']['QBZ']['bids'][0]['price']
    print("퀸비의 현재 가격 : ", queenB_price)
    queenB_price=float(queenB_price)
    if(order_queenB==0 and queenB_price<=buy_queenB_price*1.003) :
        order_queenB=bithumb.buy_limit_order("QBZ", buy_queenB_price, (krw/queenB_price)*0.5)
        is_buy_queenB=1
    if(order_queenB!=0 and queenB_price>=buy_queenB_price*1.006) :
        bithumb.cancel_order(order_queenB)
        order_queenB=0
        
    ringX_price = all['data']['RINGX']['bids'][0]['price']
    print("링엑스의 현재 가격 : ", ringX_price)
    ringX_price=float(ringX_price)
    if(order_ringX==0 and ringX_price<=buy_ringX_price*1.003) :
        order_ringX=bithumb.buy_limit_order("RINGX", buy_ringX_price, (krw/ringX_price)*0.5)
        is_buy_ringX=1
    if(order_ringX!=0 and ringX_price>=buy_ringX_price*1.006) :
        bithumb.cancel_order(order_ringX)
        order_ringX=0

    proton_price = all['data']['XPR']['bids'][0]['price']
    print("프로톤의 현재 가격 : ", proton_price)
    proton_price=float(proton_price)
    if(order_proton==0 and proton_price<=buy_proton_price*1.003) :
        order_proton=bithumb.buy_limit_order("XPR", buy_proton_price, (krw/proton_price)*0.5)
        is_buy_proton=1
    if(order_proton!=0 and proton_price>=buy_proton_price*1.006) :
        bithumb.cancel_order(order_proton)
        order_proton=0

    ae_price = all['data']['AE']['bids'][0]['price']
    print("애터니티의 현재 가격 : ", ae_price)
    ae_price=float(ae_price)
    if(order_ae==0 and ae_price<=buy_ae_price*1.003) :
        order_ae=bithumb.buy_limit_order("AE", buy_ae_price, (krw/ae_price)*0.5)
        is_buy_ae=1
    if(order_ae!=0 and ae_price>=buy_ae_price*1.006) :
        bithumb.cancel_order(order_ae)
        order_ae=0
            
    gom2_price = all['data']['GOM2']['bids'][0]['price']
    print("고머니2의 현재 가격 : ", gom2_price)
    gom2_price=float(gom2_price)
    if(order_gom2==0 and gom2_price<=buy_gom2_price*1.003) :
        order_gom2=bithumb.buy_limit_order("GOM2", buy_gom2_price, (krw/gom2_price)*0.5)
        is_buy_gom2=1
    if(order_gom2!=0 and gom2_price>=buy_gom2_price*1.006) :
        bithumb.cancel_order(order_gom2)
        order_gom2=0

    vsys_price = all['data']['VSYS']['bids'][0]['price']
    print("브이시스템즈의 현재 가격 : ", vsys_price)
    vsys_price=float(vsys_price)
    if(order_vsys==0 and vsys_price<=buy_vsys_price*1.003) :
        order_vsys=bithumb.buy_limit_order("VSYS", buy_vsys_price, (krw/vsys_price)*0.5)
        is_buy_vsys=1
    if(order_vsys!=0 and vsys_price>=buy_vsys_price*1.006) :
        bithumb.cancel_order(order_vsys)
        order_vsys=0
            
    cennz_price = all['data']['CENNZ']['bids'][0]['price']
    print("센트럴리티의 현재 가격 : ", cennz_price)
    cennz_price=float(cennz_price)
    if(order_cennz==0 and cennz_price<=buy_cennz_price*1.003) :
        order_cennz=bithumb.buy_limit_order("CENNZ", buy_cennz_price, (krw/cennz_price)*0.5)
        is_buy_cennz=1
    if(order_cennz!=0 and cennz_price>=buy_cennz_price*1.006) :
        bithumb.cancel_order(order_cennz)
        order_cennz=0

    mbl_price = all['data']['MBL']['bids'][0]['price']
    print("무비블록의 현재 가격 : ", mbl_price)
    mbl_price=float(mbl_price)
    if(order_mbl==0 and mbl_price<=buy_mbl_price*1.003) :
        order_mbl=bithumb.buy_limit_order("MBL", buy_mbl_price, (krw/mbl_price)*0.5)
        is_buy_mbl=1
    if(order_mbl!=0 and mbl_price>=buy_mbl_price*1.006) :
        bithumb.cancel_order(order_mbl)
        order_mbl=0

    eos_price = all['data']['EOS']['bids'][0]['price']
    eos_price=float(eos_price)
    print("이오스의 현재 가격 : ", eos_price)
    if(order_eos==0 and eos_price<=buy_eos_price*1.003) :
        order_eos=bithumb.buy_limit_order("EOS", buy_eos_price, (krw/eos_price)*0.5)
        is_buy_eos=1
    if(order_eos!=0 and eos_price>=buy_eos_price*1.006) :
         bithumb.cancel_order(order_eos)
         order_eos=0

    ipx_price = all['data']['IPX']['bids'][0]['price']
    ipx_price=float(ipx_price)
    print("타키온프로토콜의 현재 가격 : ", ipx_price)
    if(order_ipx==0 and ipx_price<=buy_ipx_price*1.003) :
        order_ipx=bithumb.buy_limit_order("IPX", buy_ipx_price, (krw/ipx_price)*0.5)
        is_buy_ipx=1
    if(order_ipx!=0 and ipx_price>=buy_ipx_price*1.006) :
         bithumb.cancel_order(order_ipx)
         order_ipx=0

    fleta_price = all['data']['FLETA']['bids'][0]['price']
    fleta_price=float(fleta_price)
    print("플레타의 현재 가격 : ", fleta_price)
    if(order_fleta==0 and fleta_price<=buy_fleta_price*1.003) :
        order_fleta=bithumb.buy_limit_order("FLETA", buy_fleta_price, (krw/fleta_price)*0.5)
        is_buy_fleta=1
    if(order_fleta!=0 and fleta_price>=buy_fleta_price*1.006) :
         bithumb.cancel_order(order_fleta)
         order_fleta=0
    
    wemix_price = all['data']['WEMIX']['bids'][0]['price']
    print("위믹스의 현재 가격 : ", wemix_price)
    wemix_price=float(wemix_price)
    if(order_wemix==0 and wemix_price<=buy_wemix_price*1.003) :
        bithumb.buy_limit_order("WEMIX", buy_wemix_price, (krw/wemix_price)*0.5)
        is_buy_wemix=1
    if(order_wemix!=0 and wemix_price>=buy_wemix_price*1.006) :
        bithumb.cancel_order(order_wemix)
        order_wemix=0
    
            
    # 매수한 코인들 모두 지정가 매도
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

    if(is_buy_ae==1) :
        bithumb.sell_limit_order("AE", round(buy_ae_price*yeild,1) , bithumb.get_balance("AE")[0]-bithumb.get_balance("AE")[1])
        is_buy_ae=0

    if(is_buy_gom2==1) :
        bithumb.sell_limit_order("GOM2", round(buy_gom2_price*yeild,2) , bithumb.get_balance("GOM2")[0]-bithumb.get_balance("GOM2")[1])
        is_buy_gom2=0

    if(is_buy_vsys==1) :
        bithumb.sell_limit_order("VSYS", round(buy_vsys_price*yeild,3) , bithumb.get_balance("VSYS")[0]-bithumb.get_balance("VSYS")[1])
        is_buy_vsys=0

    if(is_buy_cennz==1) :
        bithumb.sell_limit_order("CENNZ", round(buy_cennz_price*yeild,2) , bithumb.get_balance("CENNZ")[0]-bithumb.get_balance("CENNZ")[1])
        is_buy_cennz=0

    if(is_buy_mbl==1) :
        bithumb.sell_limit_order("MBL", round(buy_mbl_price*yeild,3) , bithumb.get_balance("MBL")[0]-bithumb.get_balance("MBL")[1])
        is_buy_mbl=0

    if(is_buy_eos==1) :
        bithumb.sell_limit_order("EOS", int(buy_eos_price*yeild) , bithumb.get_balance("EOS")[0]-bithumb.get_balance("EOS")[1])
        is_buy_eos=0

    if(is_buy_wemix==1) :
        bithumb.sell_limit_order("WEMIX", 190.5 , bithumb.get_balance("WEMIX")[0]-bithumb.get_balance("WEMIX")[1])
        is_buy_wemix=0

    if(is_buy_ipx==1) :
        bithumb.sell_limit_order("IPX", round(buy_ipx_price*yeild,2) , bithumb.get_balance("IPX")[0]-bithumb.get_balance("IPX")[1])
        is_buy_ipx=0

    if(is_buy_fleta==1) :
        bithumb.sell_limit_order("FLETA", round(buy_fleta_price*yeild,3) , bithumb.get_balance("FLETA")[0]-bithumb.get_balance("FLETA")[1])
        is_buy_fleta=0


    # 단기 설정 코인
    
    tmtg_price = all['data']['TMTG']['bids'][0]['price']
    tmtg_price=float(tmtg_price)
    print("더마이다스터치골드의 현재 가격 : ", tmtg_price)
    if(order_tmtg==0 and tmtg_price<=buy_tmtg_price*1.003) :
        order_tmtg=bithumb.buy_limit_order("TMTG", buy_tmtg_price, (krw/tmtg_price)*0.5)
        is_buy_tmtg=1
    if(order_tmtg!=0 and tmtg_price>=buy_tmtg_price*1.006) :
         bithumb.cancel_order(order_tmtg)
         order_tmtg=0
    if(is_buy_tmtg==1) :
        bithumb.sell_limit_order("TMTG", round(buy_tmtg_price*yeild,3) , bithumb.get_balance("TMTG")[0]-bithumb.get_balance("TMTG")[1])
        is_buy_tmtg=0

    em_price = all['data']['EM']['bids'][0]['price']
    em_price=float(em_price)
    print("이마이너의 현재 가격 : ", em_price)
    if(order_em==0 and em_price<=buy_em_price*1.003) :
        order_em=bithumb.buy_limit_order("EM", buy_em_price, (krw/em_price)*0.5)
        is_buy_em=1
    if(order_em!=0 and em_price>=buy_em_price*1.006) :
         bithumb.cancel_order(order_em)
         order_em=0
    if(is_buy_em==1) :
        bithumb.sell_limit_order("EM", round(buy_em_price*yeild,3) , bithumb.get_balance("EM")[0]-bithumb.get_balance("EM")[1])
        is_buy_em=0

    evz_price = all['data']['EVZ']['bids'][0]['price']
    evz_price=float(evz_price)
    print("이브이지의 현재 가격 : ", evz_price)
    if(order_evz==0 and evz_price<=buy_evz_price*1.003) :
        order_evz=bithumb.buy_limit_order("EVZ", buy_evz_price, (krw/evz_price)*0.5)
        is_buy_evz=1
    if(order_evz!=0 and evz_price>=buy_evz_price*1.006) :
         bithumb.cancel_order(order_evz)
         order_evz=0
    if(is_buy_evz==1) :
        bithumb.sell_limit_order("EVZ", round(buy_evz_price*yeild,2) , bithumb.get_balance("EVZ")[0]-bithumb.get_balance("EVZ")[1])
        is_buy_evz=0

    aoa_price = all['data']['AOA']['bids'][0]['price']
    aoa_price=float(aoa_price)
    print("오로라의 현재 가격 : ", aoa_price)
    if(order_aoa==0 and aoa_price<=buy_aoa_price*1.003) :
        order_aoa=bithumb.buy_limit_order("AOA", buy_aoa_price, (krw/aoa_price)*0.5)
        is_buy_aoa=1
    if(order_aoa!=0 and aoa_price>=buy_aoa_price*1.006) :
         bithumb.cancel_order(order_aoa)
         order_aoa=0
    if(is_buy_aoa==1) :
        bithumb.sell_limit_order("AOA", round(buy_aoa_price*yeild,3) , bithumb.get_balance("AOA")[0]-bithumb.get_balance("AOA")[1])
        is_buy_aoa=0

    adp_price = all['data']['ADP']['bids'][0]['price']
    adp_price=float(adp_price)
    print("어댑터토큰의 현재 가격 : ", adp_price)
    if(order_adp==0 and adp_price<=buy_adp_price*1.003) :
        order_adp=bithumb.buy_limit_order("ADP", buy_adp_price, (krw/adp_price)*0.5)
        is_buy_adp=1
    if(order_adp!=0 and adp_price>=buy_adp_price*1.006) :
         bithumb.cancel_order(order_adp)
         order_adp=0
    if(is_buy_adp==1) :
        bithumb.sell_limit_order("ADP", round(buy_adp_price*yeild,2) , bithumb.get_balance("ADP")[0]-bithumb.get_balance("ADP")[1])
        is_buy_adp=0




    


    print("\n===================================\n")

    time.sleep(0.12)


