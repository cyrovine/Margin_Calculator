'''
SELL CALL: {權利金＋MAX (保證金A值- MAX((履約價格-標的價格) ×契約乘數,0), 保證金B值)}*口數

SELL PUT : {權利金＋MAX (保證金A值- MAX((標的價格-履約價格) ×契約乘數,0), 保證金B值)}*口數

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

#            買賣  買、賣權 權利金     保證金A     保證金B     履約價              標的價格        契約乘數     口數
def Index_single_BS(mod1, option1, premiums_1, deposit_A, deposit_B, performance_price_1, presently_price, contract, position_1 ):
    print(mod1, option1, premiums_1, deposit_A, deposit_B, performance_price_1, presently_price, contract, position_1 )
    mod=sellbuy(mod1)
    option=callput(option1)

    if mod == 3 or option == 3 :
        text="請檢察買賣別是否為 SELL, BUY及買賣權是否為 CALL, PUT"
        return(3,text)

    if mod1 == "BUY":
        #買方不用保證金，但須支付權利金
        premiums_ALL=-(premiums_1*contract*position_1)
        print(premiums_ALL)
        return(0, premiums_ALL)
    elif mod1 == "SELL":
        if option1 == "CALL":
            #SELL CALL: {權利金＋MAX (保證金A值- MAX((履約價格-標的價格) ×契約乘數,0), 保證金B值)}*口數
            deposit=(premiums_1*contract+max(deposit_A-max((performance_price_1-presently_price)*contract,0),deposit_B))*position_1
            premiums_ALL=premiums_1*contract*position_1
            return(deposit, premiums_ALL)
        elif option1 == "PUT":
            #SELL PUT : {權利金＋MAX (保證金A值- MAX((標的價格-履約價格) ×契約乘數,0), 保證金B值)}*口數
            deposit=(premiums_1*contract+max(deposit_A-max((presently_price-performance_price_1)*contract,0),deposit_B))*position_1
            premiums_ALL=premiums_1*contract*position_1
            return(deposit, premiums_ALL)

    
    



"""
mod = 'SELL'
option = 'CALL'
premiums = 100
deposit_A = 48000
deposit_B = 24000
performance_price = 20000
presently_price = 19900
contract = 50
position = 10
deposit,premiums_ALL = single_BS(mod, option, premiums, deposit_A, deposit_B, performance_price, presently_price, contract, position )
print(deposit,premiums_ALL)


            mod = mod_radio1['text']
            option = option_radio3['text']
            premiums = float(premiums_input.get())
            deposit_A = float(deposit_A_input.get())
            deposit_B = float(deposit_B_input.get())
            performance_price = float(performance_price_input.get())
            presently_price = float(presently_price_input.get())
            contract = float(contract_input.get())
            position = float(position_input.get())
"""