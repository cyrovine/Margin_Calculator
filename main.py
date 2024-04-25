#導入函式
from Index_single import Index_single_BS
from Index_long_or_short import Index_long_or_short_BS
from Index_SCSP import Index_SCSP_BS
from Index_CP_time import Index_CP_time_BS
from Index_BPSC_BCSP import Index_BPSC_BCSP_BS
from Index_gold_options import Index_gold_options_BS

from stock_single import stock_single_BS
from stock_long_or_short import stock_long_or_short_BS
from stock_SCSP import stock_SCSP_BS
from stock_CP_time import stock_CP_time_BS
from stock_BPSC_BCSP import stock_BPSC_BCSP_BS
from stock_futures_options import stock_futures_options_BS

#導入GUI
import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 

#回傳訊息
def report(deposit,premiums_ALL):
    if deposit==3:
        deposit_text.config(text="錯誤代碼 : ")
        premiums_text.config(text="錯誤訊息 : ")
    else:
        deposit_text.config(text="保證金 :")
        premiums_text.config(text="權利金 :")
        print(deposit,premiums_ALL)

    deposit_ANS_text.config(font=1, text=deposit)
    premiums_ANS_text.config(font=1, text=premiums_ALL)

#選擇股票或指數
def click_category_com(window):
    selected_category = category_com.get()
    match selected_category:
        case "指數選擇權":
            stock_com.grid_forget()
            risk_lv_com.grid_forget()
            risk_lv_A_test.grid_forget()
            risk_lv_B_test.grid_forget()
            risk_lv_A_input.grid_forget()
            risk_lv_B_input.grid_forget()
            start_stock_buttom.grid_forget()
            option_build()
            Index_com.grid(row=1, column=2, columnspan=7)
            deposit_A_test.grid(row=3, column=4)
            deposit_B_test.grid(row=3, column=6)
            deposit_A_input.grid(row=3, column=5)
            deposit_B_input.grid(row=3, column=7)
            start_Index_buttom.grid(row=12, column=2, columnspan=7)
        case "股票選擇權":
            option_build()
            Index_com.grid_forget()
            deposit_A_test.grid_forget()
            deposit_B_test.grid_forget()
            deposit_A_input.grid_forget()
            deposit_B_input.grid_forget()
            start_Index_buttom.grid_forget()
            stock_com.grid(row=1, column=2, columnspan=7)
            risk_lv_com.grid(row=3, column=1)
            risk_lv_A_test.grid(row=3, column=4)
            risk_lv_B_test.grid(row=3, column=6)
            risk_lv_A_input.grid(row=3, column=5)
            risk_lv_B_input.grid(row=3, column=7)
            start_stock_buttom.grid(row=12, column=2, columnspan=7)
        case "期貨保證金":
            futures_build()
#選擇風險係數
def click_risk_lv(window):
    selected_lv = risk_lv_com.get()
    match selected_lv:
        case "級距 1":
            risk_lv_A_input.config(text="0.135")
            risk_lv_B_input.config(text="0.0675")
        case "級距 2":
            risk_lv_A_input.config(text="0.162")
            risk_lv_B_input.config(text="0.081")
        case "級距 3":
            risk_lv_A_input.config(text="0.2025")
            risk_lv_B_input.config(text="0.10125")

#指數選擇權列表
def click_Index_com(window):
    selected_mod = Index_com.get()
    match selected_mod:
        case "單一模式":
            mod_SB_1_com.config(state="readonly")
            mod_SB_1_com.current(0)
            mod_SB_2_com.grid_forget()
            mod_CP_2_com.grid_forget()
            performance_price_2_test.grid_forget()
            position_2_test.grid_forget()
            premiums_2_test.grid_forget()
            performance_price_2_input.grid_forget()
            position_2_input.grid_forget()
            premiums_2_input.grid_forget()
            buy_time_test.grid_forget()
            sell_time_test.grid_forget()
            buy_time_input.grid_forget()
            sell_time_input.grid_forget()
            presently_settle_com.grid_forget()
            futures.grid_forget()

        case "CALL & PUT 時間價差":
            show()
            mod_CP_2_com.grid_forget()
            #時間
            buy_time_test.grid(row=5, column=9 )
            sell_time_test.grid(row=7, column=9 )
            buy_time_input.grid(row=6, column=9 )
            sell_time_input.grid(row=8, column=9 )
            presently_settle_com.grid(row=9, column=1)
            #固定買賣別
            mod_SB_1_com.current(1)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "call空頭價差 & put多頭價差":
            show()

            #買賣權須相同
            mod_CP_2_com.grid_forget()

            #買賣口數需相同
            position_2_test.grid_forget()
            position_2_input.grid_forget()

             #固定買賣別權
            mod_SB_1_com.current(1)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "賣出call&賣出put":
            show()

            position_2_test.grid_forget()
            position_2_input.grid_forget()

            #固定買賣別權
            mod_SB_1_com.current(2)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "買進put賣出call、買進call賣出put":
            show()
            position_2_test.grid_forget()
            position_2_input.grid_forget()

            #固定買賣別權
            mod_SB_1_com.current(1)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "買進臺幣黃金期貨賣出黃金選擇權Call & 賣出臺幣黃金期貨賣出黃金選擇權Put":
            show()
            performance_price_2_test.grid_forget()
            position_2_test.grid_forget()
            premiums_2_test.grid_forget()
            performance_price_2_input.grid_forget()
            position_2_input.grid_forget()
            premiums_2_input.grid_forget()
            position_2_test.grid_forget()
            position_2_input.grid_forget()

            #固定買賣別權
            mod_SB_1_com.current(2)
            mod_SB_2_com.current(0)
            mod_SB_1_com.config(state="disabled")

            #固定為期貨
            mod_CP_2_com.grid_forget()
            futures.grid(row=8, column=8)
        
#股票選擇權列表        
def click_stock_com(window):
    selected_mod = stock_com.get()
    match selected_mod:
        case "單一模式":
            mod_SB_1_com.config(state="readonly")
            mod_SB_1_com.current(0)
            mod_SB_2_com.grid_forget()
            mod_CP_2_com.grid_forget()
            performance_price_2_test.grid_forget()
            position_2_test.grid_forget()
            premiums_2_test.grid_forget()
            performance_price_2_input.grid_forget()
            position_2_input.grid_forget()
            premiums_2_input.grid_forget()
            buy_time_test.grid_forget()
            sell_time_test.grid_forget()
            buy_time_input.grid_forget()
            sell_time_input.grid_forget()
            presently_settle_com.grid_forget()
            futures.grid_forget()

        case "CALL & PUT 時間價差":
            show()
            mod_CP_2_com.grid_forget()
            #時間
            buy_time_test.grid(row=5, column=9 )
            sell_time_test.grid(row=7, column=9 )
            buy_time_input.grid(row=6, column=9 )
            sell_time_input.grid(row=8, column=9 )
    
            #固定買賣別
            mod_SB_1_com.current(1)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "call空頭價差 & put多頭價差":
            show()

            #買賣權須相同
            mod_CP_2_com.grid_forget()

            #買賣口數需相同
            position_2_test.grid_forget()
            position_2_input.grid_forget()

             #固定買賣別權
            mod_SB_1_com.current(1)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "賣出call&賣出put":
            show()

            position_2_test.grid_forget()
            position_2_input.grid_forget()

            #固定買賣別權
            mod_SB_1_com.current(2)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")


        case "買進put賣出call、買進call賣出put":
            show()
            position_2_test.grid_forget()
            position_2_input.grid_forget()

            #固定買賣別權
            mod_SB_1_com.current(1)
            mod_SB_2_com.current(2)
            mod_SB_1_com.config(state="disabled")
            mod_SB_2_com.config(state="disabled")

        case "期貨與選擇權之組合部位":
            show()
            performance_price_2_test.grid_forget()
            position_2_test.grid_forget()
            premiums_2_test.grid_forget()
            performance_price_2_input.grid_forget()
            position_2_input.grid_forget()
            premiums_2_input.grid_forget()
            position_2_test.grid_forget()
            position_2_input.grid_forget()

            #固定買賣別權
            mod_SB_1_com.current(2)
            mod_SB_1_com.config(state="disabled")

            #固定為期貨
            mod_CP_2_com.grid_forget()
            futures.grid(row=8, column=8)

#執行指數選擇權按鈕 
def click_Index_buttom():
    deposit_text.config(text="保證金 :")
    premiums_text.config(text="權利金 :")

    #買賣
    mod1 = mod_SB_1_com.get()
    mod2 = mod_SB_2_com.get()
    option1 = mod_CP_1_com.get()
    option2 = mod_CP_2_com.get()

    #現價、AB值、契約
    presently_price = float(presently_price_input.get())
    deposit_A = float(deposit_A_input.get())
    deposit_B = float(deposit_B_input.get())
    contract = float(contract_input.get())

    #履約、口數、權利金
    performance_price_1 = float(performance_price_1_input.get())
    performance_price_2 = float(performance_price_2_input.get())
    position_1 = float(position_1_input.get())
    position_2 = float(position_2_input.get())
    premiums_1 = float(premiums_1_input.get())
    premiums_2 = float(premiums_2_input.get())

    #print(mod1, option1, premiums_1, performance_price_1, position_1, mod2, option2, premiums_2, position_2, performance_price_2, deposit_A, deposit_B, presently_price, contract,)

    selected_mod = Index_com.get()
    match selected_mod:
        case "單一模式":
            deposit,premiums_ALL = Index_single_BS(mod1, option1, premiums_1, deposit_A, deposit_B, performance_price_1, presently_price, contract, position_1 )
            report(deposit,premiums_ALL)    
            
        case "CALL & PUT 時間價差":
            presently_settle=presently_settle_com.get()
            option2 = option1

            time_B=buy_time_input.get()
            time_S=sell_time_input.get()

            deposit,premiums_ALL = Index_CP_time_BS(option1, option2, premiums_1, premiums_2, time_B, time_S, deposit_A, deposit_B, performance_price_1, performance_price_2, presently_price, contract, position_1, presently_settle )
            report(deposit,premiums_ALL)  

        case "call空頭價差 & put多頭價差":
            option2 = option1

            if mod1=="BUY":
                premiums_B=premiums_1
                premiums_S=premiums_2
                performance_price_B=performance_price_1
                performance_price_S=performance_price_2
            elif mod1=="SELL":
                premiums_B=premiums_2
                premiums_S=premiums_1
                performance_price_B=performance_price_2
                performance_price_S=performance_price_1

            deposit,premiums_ALL = Index_long_or_short_BS(option1, option2, premiums_B, premiums_S, performance_price_B, performance_price_S, contract, position_1)
            report(deposit,premiums_ALL)  

        case "賣出call&賣出put":
            deposit,premiums_ALL = Index_SCSP_BS(option1, option2, premiums_1, premiums_2, deposit_A, deposit_B, performance_price_1, performance_price_2, presently_price, contract, position_1, position_2)
            report(deposit,premiums_ALL)  

        case "買進put賣出call、買進call賣出put":
            deposit,premiums_ALL = Index_BPSC_BCSP_BS(mod1, mod2, option1, option2, premiums_1, premiums_2, deposit_A, deposit_B, performance_price_1, performance_price_2, presently_price, contract, position_1)
            report(deposit,premiums_ALL)  

        case "買進臺幣黃金期貨賣出黃金選擇權Call & 賣出臺幣黃金期貨賣出黃金選擇權Put":#not finish
            print(mod2, option1, premiums_1, presently_price, contract, position_1 )
            deposit,premiums_ALL = Index_gold_options_BS(mod2, option1, premiums_1, presently_price, contract, position_1)
            report(deposit,premiums_ALL)  

#執行股票選擇權按鈕 
def click_stock_buttom():
    deposit_text.config(text="保證金 :")
    premiums_text.config(text="權利金 :")

    #買賣
    mod1 = mod_SB_1_com.get()
    mod2 = mod_SB_2_com.get()
    option1 = mod_CP_1_com.get()
    option2 = mod_CP_2_com.get()

    #現價、AB值、契約
    presently_price = float(presently_price_input.get())
    risk_lv_A = float(risk_lv_A_input.cget("text"))
    risk_lv_B = float(risk_lv_B_input.cget("text"))
    contract = float(contract_input.get())

    #履約、口數、權利金
    performance_price_1 = float(performance_price_1_input.get())
    performance_price_2 = float(performance_price_2_input.get())
    position_1 = float(position_1_input.get())
    position_2 = float(position_2_input.get())
    premiums_1 = float(premiums_1_input.get())
    premiums_2 = float(premiums_2_input.get())

    #print(mod1, option1, premiums_1, performance_price_1, position_1, mod2, option2, premiums_2, position_2, performance_price_2, deposit_A, deposit_B, presently_price, contract,)


    selected_mod = stock_com.get()
    match selected_mod:
        case "單一模式":
            deposit,premiums_ALL = stock_single_BS(mod1, option1, premiums_1, risk_lv_A, risk_lv_B, performance_price_1, presently_price, contract, position_1 )
            report(deposit,premiums_ALL)    

        case "CALL & PUT 時間價差":
            option2 = option1

            time_B=buy_time_input.get()
            time_S=sell_time_input.get()

            deposit,premiums_ALL = stock_CP_time_BS(option1, option2, premiums_1, premiums_2, time_B, time_S, risk_lv_A, risk_lv_B, performance_price_1, performance_price_2, presently_price, contract, position_1)
            
            report(deposit,premiums_ALL)  

        case "call空頭價差 & put多頭價差":

            option2 = option1

            deposit,premiums_ALL = stock_long_or_short_BS(option1, option2, premiums_1, premiums_2, performance_price_1, performance_price_2, contract, position_1)
            
            report(deposit,premiums_ALL)  

        case "賣出call&賣出put":
            deposit,premiums_ALL = stock_SCSP_BS(option1, option2, premiums_1, premiums_2, risk_lv_A, risk_lv_B, performance_price_1, performance_price_2, presently_price, contract, position_1, position_2)

            report(deposit,premiums_ALL)  

        case "買進put賣出call、買進call賣出put":
            
            deposit,premiums_ALL = stock_BPSC_BCSP_BS(option1, option2, premiums_1, premiums_2, risk_lv_A, risk_lv_B, performance_price_1, performance_price_2, presently_price, contract, position_1)
            
            report(deposit,premiums_ALL)  

        case "期貨與選擇權之組合部位":
            risk_lv = risk_lv_com.get()
            #                                  期貨買賣          買、賣權  權利金     期貨保證金      契約乘數     口數
            deposit,premiums_ALL = stock_futures_options_BS(mod2, option1, premiums_1, presently_price, contract, position_1, risk_lv)
                                                   

            report(deposit,premiums_ALL)  

#元件出現
def show():

    buy_time_test.grid_forget()
    sell_time_test.grid_forget()
    buy_time_input.grid_forget()
    sell_time_input.grid_forget()
    presently_settle_com.grid_forget()
    futures.grid_forget()

    mod_SB_2_com.grid(row=8, column=1 )
    mod_CP_2_com.grid(row=8, column=8 )
    performance_price_2_test.grid(row=8, column=2 )
    position_2_test.grid(row=8, column=4 )
    premiums_2_test.grid(row=8, column=6 )
    performance_price_2_input.grid(row=8, column=3 )
    position_2_input.grid(row=8, column=5 )
    premiums_2_input.grid(row=8, column=7 )


    mod_SB_1_com.config(state="readonly")
    mod_SB_2_com.config(state="readonly")
    mod_SB_1_com.current(0)
    mod_SB_2_com.current(0)

#建視窗
window = tk.Tk()
window.title('選擇權保證金計算機')
window.geometry('1550x400')
window.resizable(False, False)
window.option_add("*TCombobox*Listbox.font","1")

#建立下拉式選單
category_com = ttk.Combobox(window, font=1,  width=100, values=["  請選擇種類", "期貨保證金", "指數選擇權", "股票選擇權"], state="readonly")
Index_com = ttk.Combobox(window, font=1, width=100, values=["  請選擇模式", "單一模式", "CALL & PUT 時間價差", "call空頭價差 & put多頭價差", "賣出call&賣出put", "買進put賣出call、買進call賣出put", "買進臺幣黃金期貨賣出黃金選擇權Call & 賣出臺幣黃金期貨賣出黃金選擇權Put"], state="readonly")
stock_com = ttk.Combobox(window, font=1, width=100, values=["  請選擇模式", "單一模式", "CALL & PUT 時間價差", "call空頭價差 & put多頭價差", "賣出call&賣出put", "買進put賣出call、買進call賣出put", "期貨與選擇權之組合部位"], state="readonly")
futures_com = ttk.Combobox(window, font=1, width=100, values=["請選擇模式""單一模式""跨月價差"], state="readonly")
risk_lv_com = ttk.Combobox(window, font=1, values=["  請選擇風險級距", "級距 1", "級距 2", "級距 3"], state="readonly")
mod_SB_1_com = ttk.Combobox(window, font=1, values=["  請選擇買賣別", "BUY", "SELL"], state="readonly")
mod_SB_2_com = ttk.Combobox(window, font=1, values=["  請選擇買賣別", "BUY", "SELL"], state="readonly")
mod_CP_1_com = ttk.Combobox(window, font=1, values=["  請選擇買賣權", "CALL", "PUT"], state="readonly")
mod_CP_2_com = ttk.Combobox(window, font=1, values=["  請選擇買賣權", "CALL", "PUT"], state="readonly")
presently_settle_com = ttk.Combobox(window, font=1, values=["  請選擇同標的期貨", "臺股期貨", "小型臺指", "電子期貨", "小型電子期貨", "金融期貨", "小型金融期貨", ], state="readonly")

category_com.current(0)
Index_com.current(0)
stock_com.current(0)
risk_lv_com.current(0)
mod_SB_1_com.current(0)
mod_SB_2_com.current(0)
mod_CP_1_com.current(0)
mod_CP_2_com.current(0)
presently_settle_com.current(0)

category_com.bind("<<ComboboxSelected>>", click_category_com)
Index_com.bind("<<ComboboxSelected>>", click_Index_com)
stock_com.bind("<<ComboboxSelected>>", click_stock_com)
risk_lv_com.bind("<<ComboboxSelected>>", click_risk_lv)


#建立Lable
presently_price_test = tk.Label(window, font=1, text="標的價格 :")
deposit_A_test = tk.Label(window, font=1, text="保證金A值 :")
deposit_B_test = tk.Label(window, font=1, text="保證金B值 :")
risk_lv_A_test = tk.Label(window, font=1, text="風險係數A值 :")
risk_lv_B_test = tk.Label(window, font=1, text="風險係數B值 :")
risk_lv_A_input = tk.Label(window, font=1, text="1")
risk_lv_B_input = tk.Label(window, font=1, text="1")
contract_test = tk.Label(window, font=1, text="契約乘數 :")

performance_price_1_test = tk.Label(window, font=1, text="履約價 :")
performance_price_2_test = tk.Label(window, font=1, text="履約價 :")
position_1_test = tk.Label(window, font=1, text="口數 :")
position_2_test = tk.Label(window, font=1, text="口數 :")
premiums_1_test = tk.Label(window, font=1, text="權利金 :")
premiums_2_test = tk.Label(window, font=1, text="權利金 :")

deposit_text = tk.Label(window, font=1, text="保證金 :")
deposit_ANS_text = tk.Label()
premiums_text = tk.Label(window, font=1, text="權利金 :")
premiums_ANS_text = tk.Label()

buy_time_test = tk.Label(window, font=1, text="買入時間 :")
sell_time_test = tk.Label(window, font=1, text="賣出時間 :")

futures = tk.Label(window, font=1, text="期貨")

start_Index_buttom=tk.Button(window, font=1, width=100, text="開始計算", command=click_Index_buttom)
start_stock_buttom=tk.Button(window, font=1, width=100, text="開始計算", command=click_stock_buttom)

emp = tk.Label(window, font=1)
emp1 = tk.Label(window, font=1)
emp2 = tk.Label(window, font=1)
emp3 = tk.Label(window, font=1)
emp4 = tk.Label(window, font=1)

#建立Entry
presently_price_input = tk.Entry(window, font=1)
deposit_A_input = tk.Entry(window, font=1)
deposit_B_input = tk.Entry(window, font=1)
contract_input = tk.Entry(window, font=1)

performance_price_1_input = tk.Entry(window, font=1)
performance_price_2_input = tk.Entry(window, font=1)
position_1_input = tk.Entry(window, font=1)
position_2_input = tk.Entry(window, font=1)
premiums_1_input = tk.Entry(window, font=1)
premiums_2_input = tk.Entry(window, font=1)

buy_time_input = tk.Entry(window, font=1)
sell_time_input = tk.Entry(window, font=1)

#Entry預先輸入
presently_price_input.insert(0,"19900")
deposit_A_input.insert(0,"48000")
deposit_B_input.insert(0,"24000")
contract_input.insert(0,"50")

performance_price_1_input.insert(0,"20000")
performance_price_2_input.insert(0,"20000")
position_1_input.insert(0,"10")
position_2_input.insert(0,"10")
premiums_1_input.insert(0,"100")
premiums_2_input.insert(0,"100")

buy_time_input.insert(0,"202404")
sell_time_input.insert(0,"202403")

#排列

for i in range(10):
    window.rowconfigure(i, minsize=30)
window.columnconfigure(0, minsize=20)
window.rowconfigure(5, minsize=0)

category_com.grid(row=0, column=2, columnspan=7)

emp.grid(row=0, column=1)
emp1.grid(row=2, column=0)
emp2.grid(row=7, column=0)
emp3.grid(row=9, column=0)
emp4.grid(row=11, column=0)


def option_build():
    Index_com.grid(row=1, column=2, columnspan=7)
    mod_SB_1_com.grid(row=6, column=1)
    mod_SB_2_com.grid(row=8, column=1)
    mod_CP_1_com.grid(row=6, column=8)
    mod_CP_2_com.grid(row=8, column=8)
    
    presently_price_test.grid(row=3, column=2)
    deposit_A_test.grid(row=3, column=4)
    deposit_B_test.grid(row=3, column=6)
    contract_test.grid(row=3, column=8)
    
    presently_price_input.grid(row=3, column=3)
    deposit_A_input.grid(row=3, column=5)
    deposit_B_input.grid(row=3, column=7)
    contract_input.grid(row=3, column=9)
    
    performance_price_1_test.grid(row=6, column=2 )
    performance_price_2_test.grid(row=8, column=2 )
    position_1_test.grid(row=6, column=4 )
    position_2_test.grid(row=8, column=4 )
    premiums_1_test.grid(row=6, column=6 )
    premiums_2_test.grid(row=8, column=6 )
    
    performance_price_1_input.grid(row=6, column=3 )
    performance_price_2_input.grid(row=8, column=3 )
    position_1_input.grid(row=6, column=5 )
    position_2_input.grid(row=8, column=5 )
    premiums_1_input.grid(row=6, column=7 )
    premiums_2_input.grid(row=8, column=7 )
    
    deposit_text.grid(row=10, column=4 )
    deposit_ANS_text.grid(row=10, column=5 )
    premiums_text.grid(row=10, column=6 )
    premiums_ANS_text.grid(row=10, column=7, columnspan=3)




    start_Index_buttom.grid(row=12, column=2, columnspan=7)

def futures_build():
    Index_com.grid(row=1, column=2, columnspan=7)
    mod_SB_1_com.grid(row=6, column=1)
    mod_SB_2_com.grid(row=8, column=1)
    mod_CP_1_com.grid(row=6, column=8)
    mod_CP_2_com.grid(row=8, column=8)
    
    presently_price_test.grid(row=3, column=2)
    deposit_A_test.grid(row=3, column=4)
    deposit_B_test.grid(row=3, column=6)
    contract_test.grid(row=3, column=8)
    
    presently_price_input.grid(row=3, column=3)
    deposit_A_input.grid(row=3, column=5)
    deposit_B_input.grid(row=3, column=7)
    contract_input.grid(row=3, column=9)
    
    performance_price_1_test.grid(row=6, column=2 )
    performance_price_2_test.grid(row=8, column=2 )
    position_1_test.grid(row=6, column=4 )
    position_2_test.grid(row=8, column=4 )
    premiums_1_test.grid(row=6, column=6 )
    premiums_2_test.grid(row=8, column=6 )
    
    performance_price_1_input.grid(row=6, column=3 )
    performance_price_2_input.grid(row=8, column=3 )
    position_1_input.grid(row=6, column=5 )
    position_2_input.grid(row=8, column=5 )
    premiums_1_input.grid(row=6, column=7 )
    premiums_2_input.grid(row=8, column=7 )
    
    deposit_text.grid(row=10, column=4 )
    deposit_ANS_text.grid(row=10, column=5 )
    premiums_text.grid(row=10, column=6 )
    premiums_ANS_text.grid(row=10, column=7, columnspan=3)




    start_Index_buttom.grid(row=12, column=2, columnspan=7)

window.mainloop()

