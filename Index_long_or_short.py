'''
call空頭價差 : {買進與賣出部位之履約價差 ×契約乘數}*口數   #買高CALL賣低CALL

put 多頭價差 : {買進與賣出部位之履約價差 ×契約乘數}*口數   #買低PUT 賣高PUT
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

def Index_long_or_short_BS(option1, option2, premiums_1, premiums_2, performance_price_1, performance_price_2, contract, position_1):
    
    option=max(callput(option1),callput(option2))

    if  option == 3 :
        text="請檢察買賣別是否為 SELL, BUY及買賣權是否為 CALL, PUT"
        return(3,text)



    if option1 == "CALL":
        #call空頭價差 : {買進與賣出部位之履約價差 ×契約乘數}*口數
        if performance_price_1 > performance_price_2:
            deposit=(performance_price_1-performance_price_2)*contract*position_1
            return(deposit,(premiums_2-premiums_1)*contract*position_1)
        
        elif performance_price_1 < performance_price_2:
            return(0,(premiums_2-premiums_1)*contract*position_1)
        
        else:
            text="call空頭價差 :買高CALL賣低CALL"
            return(3,text)
        
    elif option1 == "PUT":
        #put 多頭價差 : {買進與賣出部位之履約價差 ×契約乘數}*口數
        if performance_price_1 < performance_price_2:
            deposit=(performance_price_2-performance_price_1)*contract*position_1
            return(deposit,(premiums_2-premiums_1)*contract*position_1)
        
        elif performance_price_1 > performance_price_2:
            return(0,(premiums_2-premiums_1)*contract*position_1)
        
        else:
            text="put 多頭價差 : 買低PUT賣高PUT"
            return(3,text)
    

       





'''  
mod1 = 'BUY'
mod2 = 'SELL'
option1 = 'PUT'
option2 = 'PUT'
premiums_1=100
premiums_2=100
performance_price_1 = 20000
performance_price_2 = 20100
contract = 50
position_1 = 10
deposit,premiums_ALL =long_or_short_BS(mod1, mod2, option1, option2, premiums_1, premiums_2, performance_price_1, performance_price_2, contract, position_1)
print(deposit,premiums_ALL)
'''