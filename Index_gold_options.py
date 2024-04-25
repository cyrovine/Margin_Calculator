'''
買進臺幣黃金期貨賣出黃金選擇權Call、賣出臺幣黃金期貨賣出黃金選擇權Put : {期貨保證金+選擇權之權利金市值}*口數

'''
def sellbuy(mod):
    if mod =='BUY':
        mod_T = 0
        return mod_T
    elif mod == 'SELL':
        mod_T = 1
        return mod_T
    else :
        mod_T = 3
        return mod_T

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
    
#               期貨買賣          買、賣權 期貨保證金  權利金     契約乘數     口數
def Index_gold_options_BS(mod2, option1, premiums, presently_price, contract, position ):

    mod=sellbuy(mod2)
    option=callput(option1)

    if mod == 3 or option == 3:
        text="請檢察買賣別是否為 SELL, BUY及買賣權是否為 CALL, PUT"
        return(3,text)

    if mod2 == "BUY" and option1 == "CALL" :
        #{期貨保證金+選擇權之權利金市值}*口數
        deposit=(presently_price*0.135+(premiums*contract))*position
        return(deposit,premiums*contract*position)
    elif mod2 == "SELL" and option1 == "PUT" :
        #{期貨保證金+選擇權之權利金市值}*口數
        deposit=(presently_price*0.135+(premiums*contract))*position
        return(deposit,premiums*contract*position)
    else:
        text = "請檢察是否為 買入期貨並賣出CALL 或 賣出期貨並賣出PUT"
        return(3, text)





'''
mod = 'SELL'
option = 'PUT'
premiums = 100
presently_price = 8520
contract = 50
position = 10
gold_options_BS(mod, option, Futures, premiums, contract, position )
'''