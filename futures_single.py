from futures_deposit_set import find_deposit

def futures_single(Buy_Sell, account_m, prod, price_now, price_bs, contract_1, position):

    
    balance,keep,raw=find_deposit(prod)

    keep=keep*position

    raw=raw*position

    if Buy_Sell == "BUY":

        differ_deposit=(price_now-price_bs)*contract_1*position
        keep_or_not= keep>(account_m-(raw+differ_deposit))
        print("原始保證金為",raw,"今日浮動",(price_now-price_bs),"浮動保證金為",differ_deposit)
        print("是否小於維持保證金",keep_or_not)

        if keep_or_not:
            print("須補",differ_deposit)
        if differ_deposit>=0:
            equity=(account_m)/(raw)*100
            print("今日保證金為",raw)
            print("帳戶餘額為",account_m-raw,"未平倉損益",differ_deposit)
        elif differ_deposit<0:
            equity=(account_m-differ_deposit)/(raw)*100
            print("今日保證金為",raw,"+",differ_deposit)
            print("帳戶餘額為",account_m-raw,"未平倉損益",differ_deposit)
        print("權益數",equity,"%")

    elif Buy_Sell == "SELL":
        differ_deposit=(price_bs-price_now)*contract_1*position
        keep_or_not= keep>(account_m+(raw+differ_deposit))
        print("原始保證金為",raw,"今日浮動",(price_now-price_bs),"浮動保證金為",differ_deposit)
        print("是否小於維持保證金",keep_or_not)
    
        if keep_or_not:
            print("須補",differ_deposit)
        if differ_deposit>0:
            equity=(account_m)/(raw)*100
            print("今日保證金為",raw)
        else:
            equity=(account_m+differ_deposit)/(raw)*100
            print("今日保證金為",raw+differ_deposit)
        print("權益數",equity,"%")

    

    
    
    
    
    return(keep, raw)
Buy_Sell="BUY"
account_m=500000
prod="TX"
price_now=21000
price_bs=20500
contract_1=50
position=1

futures_single(Buy_Sell, account_m, prod, price_now, price_bs, contract_1, position)