'''
期貨與選擇權之組合部位
	買進一口二千股標的證券之股票期貨，賣出一口同一標的股票選擇權買權：  收取一  口二千股標的證券之 股票期貨保證金+選擇權之權利金市值
	賣出一口二千股標的證券之股票期貨，賣出一口同一標的股票選擇權賣權：  收取一  口二千股標的證券之 股票期貨保證金+選擇權之權利金市值
	買進二十口一百股標的證券之股票期貨，賣出一口同一標的股票選擇權買權：收取二十口一百股標的證券之 股票期貨保證金+選擇權之權利金市值
	賣出二十口一百股標的證券之股票期貨，賣出一口同一標的股票選擇權賣權：收取二十口一百股標的證券之 股票期貨保證金+選擇權之權利金市值
     
    大股  一口 對應 選擇權一口
    小股  20口 對應 選擇權一口


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
def stock_futures_options_BS(mod2, option1, premiums, presently_price, contract, position, risk_lv):

    mod=sellbuy(mod2)
    option=callput(option1)

    if risk_lv == "級距 1":
        risk=float(0.1350)
        risk_end=float(0.10)
    elif risk_lv=="級距 2":
        risk=float(0.1620)
        risk_end=float(0.12)
    elif risk_lv == "級距 3":
        risk=float(0.2025)
        risk_end=float(0.15)
    else:
        text="沒有這個風險級距"
        return(3,text)

    if mod == 3 or option == 3:
        text="請檢察買賣別是否為 SELL, BUY及買賣權是否為 CALL, PUT"
        return(3,text)
    #判斷大小股
    if contract == 100:
        if position < 20:
            text="小型股期貨須滿二十口才對應選擇權一口"
            return(3, text)
        elif (position%20) != 0:
            text="小型股期貨須每二十口才對應選擇權一口"
            return(3, text)
    elif contract != 2000:
        text="股票期貨契約乘數只有100或2000"
        return(3, text)

    if mod2 == "BUY" and option1 == "CALL" :
        #{股票期貨保證金+選擇權之權利金市值}*口數
        deposit=(presently_price*contract*risk_end+(premiums*contract))*position
        premiums_ALL=(premiums-(presently_price*risk))*contract*position
        return(deposit,premiums_ALL)
    elif mod2 == "SELL" and option1 == "PUT" :
        #{股票期貨保證金+選擇權之權利金市值}*口數
        deposit=(presently_price*contract*risk_end+(premiums*contract))*position
        premiums_ALL=(premiums-(presently_price*risk))*contract*position
        return(deposit,premiums_ALL)
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