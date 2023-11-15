import time
import datetime as dt
from tkinter import *
from time import strftime

root = Tk()

root.title("ATM")

root.geometry("1000x650+300+100")

root.resizable(False, False)

root.configure(bg="#171618")

state = "logged_out"

num = ""

pin_verified = False

balanceamt = 15000

pn = ""
amt = ""
last_trac = ""
default_pin = '0'
dep_cash = 0
trans_act = ""
trans_amt = ""
yo=0
date = dt.datetime.now()
font = {'ariel',30}
trac_time = ''
def fast_cash():
    # Implement the functionality for Transfer Funds
    global state

    state = "fast_cash"

    label_result.config(text="Select amount to be dispensed")

    # Create a dictionary to store references to the buttons
    global buttons_dict
    buttons_dict = {}

    fivehundred_btn = Button(root, text="500", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda: fastCash_dispense("500"))

    fivehundred_btn.place(x=50, y=30)
    buttons_dict["500"] = fivehundred_btn

    thousand_btn = Button(root, text="1000", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                     command=lambda: fastCash_dispense("1000"))

    thousand_btn.place(x=50, y=100)
    buttons_dict["1000"] = thousand_btn

    fifteenhundred_btn = Button(root, text="1500", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                       command=lambda: fastCash_dispense("1500"))

    fifteenhundred_btn.place(x=800, y=30)
    buttons_dict["1500"] = fifteenhundred_btn

    twothousand_btn = Button(root, text="2000", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                      command=lambda: fastCash_dispense("2000"))

    twothousand_btn.place(x=800, y=100)
    buttons_dict["2000"] = twothousand_btn

def fastCash_dispense(amount):
    global last_trac, balanceamt, trac_time
    label_result.config(text=f"{amount} dispensed successfully.")
    trac_time = strftime('%H:%M:%S %p')
    last_trac = f"{amount} dispensed as fast cash at {trac_time}."


    balanceamt -= int(amount)

    # Destroy all buttons
    for button in buttons_dict.values():
        button.destroy()

    disable_options()

    disable_number()
    enter_btn["state"] = DISABLED
    delete_btn["state"]=DISABLED

def change_pin():
    # Implement the functionality for Transfer Funds

    global state

    state = "verify"

    label_result.config(text="Enter New Pin:")
    disable_options()
    enable_number()


def transfer_funds():
    # Implement the functionality for Transfer Funds

    global state

    state = "askact"

    label_result.config(text="Enter the Account no. to Transfer to :")
    disable_options()
    enable_number()


def mobile_recharge():
    # Implement the functionality for Mobile Recharge

    global state, pn

    state = "mobile_recharge"
    enable_number()
    disable_options()
    label_result.config(text="Enter Phone Number(only Rs.100):\n")


def withdrawal():
    # Implement the functionality for Withdrawal

    global state, amt

    state = "withdrawal"
    enable_number()
    disable_options()
    label_result.config(text="Enter Withdrawal Amount:\n")


def mini_statement():
    # Implement the functionality for Mini Statement

    global state, last_trac

    state = "mini_statement"
    disable_options()
    disable_number()
    label_result.config(text=last_trac)


def cash_deposit():
    # Implement the functionality for Cash Deposit

    global state, dep_cash

    state = "cash_deposit"

    label_result.config(text="Enter the amount of money needed to be deposited(multiple of Rs.500):")

    disable_options()
    enable_number()


def delete():
    global num

    num = num[:-1]

    label_result.config(text=num)


def show(value):
    global num

    num += value

    label_result.config(text=num)

def time():
    global font
    time_string = strftime('%H:%M:%S %p')  # time format
    label_time.config(text=time_string)
    label_time.place(x=400,y=250)
    label_date.place(x=350, y =200)
    label_time.after(1000, time)
    font = {'ariel',30, 'bold'}
def in_amt():
    label_result.config(text="Insufficient Balance... Try again")
    disable_number()
    disable_options()


def balance():
    global balanceamt
    label_result.config(text=f"Balance: {balanceamt}\n")


def transferf():
    global num, state
    num = ""
    label_result.config(text="Enter Transfer Amount:")
    state = "transfer_funds"

def hold():
    time.sleep(5)
    exit()
def exit():
    global num, state, pin_verified, default_pin
    state = 'logged_out'
    pin_verified = False
    num = ""
    enter_btn["state"] = NORMAL
    label_result.config(text="Enter the pin:")
    disable_options()
    enable_number()
    if (num == default_pin):
        verify_pin()


def enter():
    global num, state, last_trac, balanceamt, first_pin,second_pin,default_pin,trac_time
    trac_time = strftime('%H:%M:%S %p')
    if (state == 'logged_out' or pin_verified == False):

        verify_pin()


    elif(state=='verify'):
        state = "change_pin"
        first_pin = num
        num = ""
        label_result.config(text="Re-Enter the Pin: ")

    elif (state == 'change_pin'):
        second_pin = num
        if(first_pin==second_pin):
            default_pin = second_pin
            label_result.config(text="Pin Successfully Changed.")
        else:
            label_result.config(text="Different Pin Entered.")
        disable_number()
        disable_number()



    elif (state == "withdrawal"):
        with_amt = num
        if (balanceamt >= int(with_amt)):
            last_trac = f"Rs.{with_amt} Successfully Dispenced at {trac_time}."
            label_result.config(text=f"Rs.{with_amt} Successfully Dispenced.")
            balanceamt = balanceamt - int(with_amt)

        else:
            in_amt()
        disable_options()
        disable_number()

    elif (state == "askact"):
        global trans_act
        trans_act = num
        transferf()


    elif (state == "transfer_funds"):
        global trans_amt
        trans_amt = num
        if (balanceamt >= int(trans_amt)):
            label_result.config(text=f"Rs.{trans_amt} was Transfered to Acct no.{trans_act}")
            last_trac = f"Rs.{trans_amt} was Transfered to Acct no.{trans_act} at {trac_time} "
            balanceamt = balanceamt - int(trans_amt)
        else:
            in_amt()
        disable_options()
        disable_number()

    elif (state == "cash_deposit"):

        dep_cash = num
        if int(dep_cash) % 500 == 0:
            label_result.config(text="Deposit the Money in the Terminal.")
        else:
            label_result.config(text="Invalid Amount to Deposit.")
        disable_number()
        disable_options()



    elif (state == "mobile_recharge"):
        pnnumber = num
        if int(balanceamt) >= 100:
            last_trac = f"Rs. 100 Successfully Recharged on +91-{pnnumber} at {trac_time}."
            label_result.config(text=f"Rs. 100 Successfully Recharged on +91-{pnnumber}.")
            balanceamt = balanceamt - 100
            disable_options()
            disable_number()
        else:
            in_amt()


def verify_pin():
    global pin_verified, default_pin

    if pin_verified == False:

        global num

        user_pin = num

        if user_pin == default_pin:

            num = ""

            label_result.config(text="PIN Verified\nChoose an option:")

            pin_verified = True

            enable_options()

            disable_number()

        else:

            num = ""

            label_result.config(text="Incorrect PIN. Try again:")

            pin_verified = False

            disable_options()



    else:

        label_result.config(text="Pin Already Verified. Press Cancel to logout..")


def enable_options():
    # Enable the buttons for ATM options
    delete_btn["state"]=NORMAL

    transfer_funds_btn["state"] = NORMAL

    fast_cash_btn["state"] = NORMAL

    balance_inquiry_btn["state"] = NORMAL

    withdrawal_btn["state"] = NORMAL

    mini_statement_btn["state"] = NORMAL

    cash_deposit_btn["state"] = NORMAL

    mobile_recharge_btn["state"] = NORMAL

    pin_change_btn["state"] = NORMAL


def disable_number():
    one_btn["state"] = DISABLED

    two_btn["state"] = DISABLED

    three_btn["state"] = DISABLED

    four_btn["state"] = DISABLED

    five_btn["state"] = DISABLED

    six_btn["state"] = DISABLED

    seven_btn["state"] = DISABLED

    eight_btn["state"] = DISABLED

    nine_btn["state"] = DISABLED

    zero_btn["state"] = DISABLED


def enable_number():
    one_btn["state"] = NORMAL

    two_btn["state"] = NORMAL

    three_btn["state"] = NORMAL

    four_btn["state"] = NORMAL

    five_btn["state"] = NORMAL

    six_btn["state"] = NORMAL

    seven_btn["state"] = NORMAL

    eight_btn["state"] = NORMAL

    nine_btn["state"] = NORMAL

    zero_btn["state"] = NORMAL


def disable_options():
    # Disable the buttons for ATM options

    transfer_funds_btn["state"] = DISABLED

    fast_cash_btn["state"] = DISABLED

    balance_inquiry_btn["state"] = DISABLED

    withdrawal_btn["state"] = DISABLED

    mini_statement_btn["state"] = DISABLED

    cash_deposit_btn["state"] = DISABLED

    mobile_recharge_btn["state"] = DISABLED

    pin_change_btn["state"] = DISABLED



label_result = Label(root, width=150, height=10, text="Enter the pin:", font={"arial", 30} , bg = "#fff")

label_result.pack()

transfer_funds_btn = Button(root, text="Transfer Funds", width=15, height=2, font={"arial", 30, "bold"}, bd=1,
                            fg="#fff", bg="#3697f5", state=DISABLED, command=lambda: transfer_funds())

transfer_funds_btn.place(x=10, y=250)

fast_cash_btn = Button(root, text="Fast Cash", width=15, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff",
                       bg="#3697f5", state=DISABLED, command=lambda: fast_cash())

fast_cash_btn.place(x=815, y=250, )

balance_inquiry_btn = Button(root, text="Balance Enquiry", width=15, height=2, font={"arial", 30, "bold"}, bd=1,
                             fg="#fff", bg="#3697f5", state=DISABLED, command=lambda: balance())

balance_inquiry_btn.place(x=10, y=350)

withdrawal_btn = Button(root, text="Withdrawal", width=15, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff",
                        bg="#3697f5", state=DISABLED, command=lambda: withdrawal())

withdrawal_btn.place(x=815, y=350)

mini_statement_btn = Button(root, text="Mini Statement", width=15, height=2, font={"arial", 30, "bold"}, bd=1,
                            fg="#fff", bg="#3697f5", state=DISABLED, command=lambda: mini_statement())

mini_statement_btn.place(x=10, y=450)

cash_deposit_btn = Button(root, text="Cash Deposit", width=15, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff",
                          bg="#3697f5", state=DISABLED, command=lambda: cash_deposit())

cash_deposit_btn.place(x=815, y=450)

mobile_recharge_btn = Button(root, text="Mobile Recharge", width=15, height=2, font={"arial", 30, "bold"}, bd=1,
                             fg="#fff", bg="#3697f5", state=DISABLED, command=lambda: mobile_recharge())

mobile_recharge_btn.place(x=10, y=550)

pin_change_btn = Button(root, text="Pin Change", width=15, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff",
                        bg="#3697f5", state=DISABLED, command=lambda: change_pin())

pin_change_btn.place(x=815, y=550)

one_btn = Button(root, text="1", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                 command=lambda: show("1"))

one_btn.place(x=300, y=300)

two_btn = Button(root, text="2", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                 command=lambda: show("2"))

two_btn.place(x=400, y=300)

three_btn = Button(root, text="3", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                   command=lambda: show("3"))

three_btn.place(x=500, y=300)

delete_btn=Button(root, text="Delete", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#FFC000",
       command=lambda: delete())

delete_btn.place(x=600, y=300)

four_btn = Button(root, text="4", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                  command=lambda: show("4"))

four_btn.place(x=300, y=370)

five_btn = Button(root, text="5", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                  command=lambda: show("5"))

five_btn.place(x=400, y=370)

six_btn = Button(root, text="6", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                 command=lambda: show("6"))

six_btn.place(x=500, y=370)

cancel_btn=Button(root, text="Cancel", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#D70040",
       command=lambda: exit())

cancel_btn.place(x=600, y=370)

seven_btn = Button(root, text="7", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                   command=lambda: show("7"))

seven_btn.place(x=300, y=440)

eight_btn = Button(root, text="8", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                   command=lambda: show("8"))

eight_btn.place(x=400, y=440)

nine_btn = Button(root, text="9", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                  command=lambda: show("9"))

nine_btn.place(x=500, y=440)

enter_btn=Button(root, text="Enter", width=8, height=5, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#009E60",
       command=lambda: enter())

enter_btn.place(x=600, y=440)

Button(root, text="", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36").place(x=300, y=510)

zero_btn = Button(root, text="0", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36",
                  command=lambda: show("0"))

zero_btn.place(x=400, y=510)

Button(root, text="", width=8, height=2, font={"arial", 30, "bold"}, bd=1, fg="#fff", bg="#2a2d36").place(x=500, y=510)

label_date = Label(root, text=f"{date:%A, %B %d, %Y}", font=font, fg="#fff", bg='#171618')
label_time = Label(root, font=font, fg="#fff", bg='#171618')
time()

root.mainloop()





