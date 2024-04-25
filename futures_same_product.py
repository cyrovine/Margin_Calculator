'''
相同商品契約，不同契約時間，一買一賣，收一口該商品保證金
	MTX,MXFFX TX保證金標準之四分之一
	ZEF       TE保證金標準之八分之一
	ZFF       TF保證金標準之四分之一

跨月價差委託保證金
— 新倉：兩契約月份皆為新倉部位
    僅收取單隻腳與單式委託相同之保證金
— 平倉：兩契約月份中，至少有一契約月份為平倉部位
    若原留倉部位保證金足夠，則不需收取保證金


'''
from futures_deposit_set import find_deposit

def futures_same(account_m, prod, time_1, time_2, price_now, price_1, price_2, contract_1, position):
    
    balance,keep,raw=find_deposit(prod)

    if time_1 == time_2:
        text="僅適用於不同最後結算日之組合"
        return(3, text)
    elif time_1 > time_2:
        text="請確認時間1大於時間2"
        return(3, text)
    elif time_1 < time_2:
        raw=raw*position
    
    
    balance,keep,raw=find_deposit(prod)

    keep=keep*position

    raw=raw*position

    differ=price_now-price_bs

    differ_deposit=differ*contract_1*position

    keep_or_not= keep>(account_m-raw-differ_deposit)

    print("原始保證金為",raw,"今日浮動",differ,"浮動保證金為",differ_deposit)
    print("是否小於維持保證金",keep_or_not)
    if keep_or_not:
        print("須補",differ_deposit)
    if differ_deposit>0:
        equity=(account_m)/(raw)*100
        print("今日保證金為",raw)
    else:
        equity=(account_m-differ_deposit)/(raw)*100
        print("今日保證金為",raw-differ_deposit)
    print("權益數",equity,"%")
    return(keep, raw)