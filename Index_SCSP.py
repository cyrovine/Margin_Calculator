'''
賣出call&賣出put : {MAX(賣出call之保證金，賣出put之保證金)＋保證金較低方之權利金市值＋混合部位風險保證金(C值)}*口數
雙買雙賣
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
    
#            買賣  買、賣權 權利金CALL   權利金PUT  保證金A     保證金B       履約價CALL          履約價PUT              標的價格        契約乘數     口數CALL   口數PUT 
#def SCSP_BS(mod,        option,          premiums_C, premiums_P, deposit_A, deposit_B, performance_price_C, performance_price_P, presently_price, contract, position_C, position_P ):
def Index_SCSP_BS(option1, option2, premiums_1, premiums_2, deposit_A, deposit_B, performance_price_1, performance_price_2, presently_price, contract, position_1, position_2):
    option=max(callput(option1),callput(option2))

    if option == 3:
        text="請檢察買賣別是否為 SELL, BUY及買賣權是否為 CALL, PUT"
        return(3,text)
    
    option=abs(callput(option1)-callput(option2))
    if option != 1:
        text="請檢察買賣權是否為 一個CALL, 一個PUT"
        return(3, text)
    
    #call之保證金
    deposit_C=(premiums_1*contract+max(deposit_A-max((performance_price_1-presently_price)*contract,0),deposit_B))*position_1
    #put之保證金
    deposit_P=(premiums_2*contract+max(deposit_A-max((presently_price-performance_price_2)*contract,0),deposit_B))*position_2
    #{MAX(賣出call之保證金，賣出put之保證金)＋保證金較低方之權利金市值＋混合部位風險保證金(C值)}*口數
    if deposit_C > deposit_P:
        deposit= deposit_C + (premiums_2*contract*position_1)+(deposit_C-deposit_P)
        return(deposit,(premiums_1*position_1+premiums_2*position_1)*contract)
    else :
        deposit= deposit_C + (premiums_1*contract*position_1)+(deposit_P-deposit_C)
        return(deposit,(premiums_1*position_1+premiums_2*position_1)*contract)
            
        
            





'''
mod = 'SELL'
option = 'CALL'
premiums_C = 100
premiums_P = 100
deposit_A = 48000
deposit_B = 24000
performance_price_C = 20000
performance_price_P = 19800
presently_price = 19900
contract = 50
position_C = 1
position_P = 1
SCSP_BS(mod, option, premiums_C, premiums_P, deposit_A, deposit_B, performance_price_C, performance_price_P, presently_price, contract, position_C, position_P )
'''