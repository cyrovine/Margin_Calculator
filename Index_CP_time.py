'''
CALL & PUT 時間價差 : {Max【(同標的期貨結算保證金 ×10%)，(2 ×權利金差價點數 ×契約乘數)】}*口數
一買一賣
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

def settle_ch(presently_settle):
    if presently_settle =="臺股期貨":
        settle=132000
        return(settle)
    elif presently_settle =="小型臺指":
        settle=33000
        return(settle)
    elif presently_settle =="電子期貨":
        settle=152000
        return(settle)
    elif presently_settle =="小型電子期貨":
        settle=19000
        return(settle)
    elif presently_settle =="金融期貨":
        settle=58000
        return(settle)
    elif presently_settle =="小型金融期貨":
        settle=14500
        return(settle)
    else:
        return(3)

#            買、賣權  權利金CALL  權利金PUT   買時間   賣時間  保證金A    保證金B      履約價CALL           履約價PUT            標的價格                              契約乘數   口數      同標的期貨結算保證金風險係數*價值 
def Index_CP_time_BS(option1, option2, premiums_1, premiums_2, time_B, time_S, deposit_A, deposit_B, performance_price_1, performance_price_2, presently_price, contract, position, presently_settle ):
    option=callput(option1)
    settle=settle_ch(presently_settle)

    if option ==3 or settle==3:
        text="請檢察是否選擇同標的期貨 及 買賣權是否為 CALL, PUT"
        return(3,text)
    
    if time_B > time_S :
        #CALL & PUT 時間價差 : {Max【(同標的期貨結算保證金 ×10%)，(2 ×權利金差價點數 ×契約乘數)】}*口數
        deposit=max((settle*0.1),(2*abs(premiums_1-premiums_2)*contract))*position
        premiums_ALL=(premiums_2-premiums_1)*contract*position
        return(deposit, premiums_ALL)
    
    elif time_B < time_S :
        premiums_ALL=(premiums_2-premiums_1)*contract*position

        if option2 == "CALL":
            #SELL CALL: {權利金＋MAX (保證金A值- MAX((履約價格-標的價格) ×契約乘數,0), 保證金B值)}*口數
            deposit=((premiums_2-premiums_1)*contract+max(deposit_A-max((performance_price_1-presently_price)*contract,0),deposit_B))*position
        elif option == 1:
            #SELL PUT : {權利金＋MAX (保證金A值- MAX((標的價格-履約價格) ×契約乘數,0), 保證金B值)}*口數
            deposit=((premiums_2-premiums_1)*contract+max(deposit_A-max((presently_price-performance_price_2)*contract,0),deposit_B))*position
            
        return(deposit, premiums_ALL)
    
    else :
        text="請檢察買入時間是否為【遠月】"
        return(3,text)




'''
mod = 'SELL'
option = 'PUT'
premiums_C = 100
premiums_P = 100
time_B = 202404
time_S = 202403
deposit_A = 48000
deposit_B = 24000
performance_price_C = 20000
performance_price_P = 20000
presently_price = 19866
contract = 50
position = 1
presently_settle=200*0.1
CP_time_BS(mod, option, premiums_C, premiums_P, time_B, time_S, deposit_A, deposit_B, performance_price_C, performance_price_P, presently_price, contract, position, presently_settle)
'''