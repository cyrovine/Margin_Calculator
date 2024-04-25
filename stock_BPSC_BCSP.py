'''
買進put賣出call、買進call賣出put : 買進部位不需計收保證金 賣出部位之保證金依賣出call或賣出put之保證金計收方式計算

'''

def callput(option):
    if option =='CALL':
        option_T = 0
        return option_T
    elif option == 'PUT':
        option_T = 1
        return option_T
    else :
        option_T = 3
        return option_T

#          買(買、賣權) 賣(買、賣權) 權利金BUY  權利金SELL    保證金A     保證金B     履約價BUY            履約價SELL           標的價格          契約乘數     口數
#def BPSC_BCSP_BS(option_B, option_S, premiums_B, premiums_S, deposit_A, deposit_B, performance_price_B, performance_price_S, presently_price, contract, position ):
def stock_BPSC_BCSP_BS(option1, option2, premiums_1, premiums_2, risk_LV_A, risk_LV_B, performance_price_1, performance_price_2, presently_price, contract, position_1):
    option=max(callput(option1),callput(option2))

    if  option == 3:
        text="請檢察買賣別是否為 SELL, BUY及買賣權是否為 CALL, PUT"
        return(3,text)
    
    option=abs(callput(option1)-callput(option2))
    if option != 1:
        text="請檢察買賣權是否為 一個CALL, 一個PUT"
        return(3, text)

    if option1 == "PUT" and option2 == "CALL" :
        deposit=(premiums_1*contract+max(presently_price*contract*risk_LV_A-max((performance_price_1-presently_price)*contract,0),presently_price*contract*risk_LV_B))*position_1
        return(deposit,(premiums_2-premiums_1)*contract*position_1)
    elif option1 == "CALL" and option2 == "PUT" :
        deposit=(premiums_1*contract+max(presently_price*contract*risk_LV_A-max((presently_price-performance_price_2)*contract,0),presently_price*contract*risk_LV_B))*position_1
        return(deposit,(premiums_2-premiums_1)*contract*position_1)


'''
option_B = "PUT"
option_S = "CALL"
premiums_B = 100
premiums_S = 100
deposit_A = 48000
deposit_B = 24000
performance_price_B =20000
performance_price_S =20000
presently_price = 19900
contract = 50
position = 1
BPSC_BCSP_BS(option_B, option_S, premiums_B, premiums_S, deposit_A, deposit_B, performance_price_B, performance_price_S, presently_price, contract, position )
'''