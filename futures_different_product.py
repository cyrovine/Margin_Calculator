'''
相同商品契約，不同契約時間，一買一賣，收一口該商品保證金
	MTX,MXFFX TX保證金標準之四分之一
	ZEF       TE保證金標準之八分之一
	ZFF       TF保證金標準之四分之一

不同商品契約， MAXIMUM(一口買保證金,一口賣保證金)
	僅TX、TE、TF、MTX、GTF、G2F、E4F、ZEF、ZFF、SOF、RHF、RTF、UDF、SPF、UNF及SXF適用
'''
from futures_deposit_set import find_deposit

def future_different(prod_1, prod_2):

    keep_1,raw_1=find_deposit(prod_1)
    keep_2,raw_2=find_deposit(prod_2)
    keep_f=max(keep_1, keep_2)
    raw_f=max(raw_1, raw_2)
    return(keep_f, raw_f)