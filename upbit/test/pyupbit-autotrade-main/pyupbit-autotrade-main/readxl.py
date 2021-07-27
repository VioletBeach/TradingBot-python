import pandas as pd

count=0
list=[]

df = pd.read_excel('엑셀/KRW-BCH.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])

df = pd.read_excel('엑셀/KRW-BTT.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])

df = pd.read_excel('엑셀/KRW-CBK.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-DKA.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-EMC2.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-HIVE.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-MLK.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-MOC.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-PXL.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-RFR.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-STORJ.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])


df = pd.read_excel('엑셀/KRW-UPP.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])

df = pd.read_excel('엑셀/KRW-XEM.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])



df = pd.read_excel('엑셀/KRW-XRP.xlsx', header=None, sheet_name=None, usecols=[6])
for i in range(1,29) :
    t=df['sheet'+str(i)]
    p=pd.DataFrame.to_numpy(t)
    list.append(p[0][0])

print(list)
df=pd.DataFrame(list)
df.to_excel('엑셀/토탈.xlsx')






