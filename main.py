import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from airplain_form import AirplaneForm
from buss_form import BussForm
from form_helper import FormHelper
from ticket import TicketForm
from train_form import TrainForm



# =============================================================================
# Functions
# =============================================================================

op=False
def login_operator():

    # f = form.Form(vehicle_tab, operator_window, v,"operator")
    # f.create_register_form_form()
    global op
    op=True
    select_vehicle()
    user=user_entry.get()
    password=pass_entry.get()
    if user=="admin" and password=="admin":
        operator_window.deiconify()
    else:
        if user!="admin" and password=="admin":
            warning_label.config(text="The username is incorrect")
        elif user=="admin" and password!="admin":
            warning_label.config(text="The password is incorrect")
        elif user!="admin" and password!="admin":
            warning_label.config(text="The username and password is incorrect")

def select_vehicle():
    global op
    v = vehicle_radio.get()
    if v=="airplane":
        a=AirplaneForm(buy_frame,root)
        a.create_search_form()
        if op==True:
            a = AirplaneForm(vehicle_tab, operator_window)
            a.create_register_form()
    elif v=="train":
        t=TrainForm(buy_frame,root)
        t.create_search_form()
        if op==True:
            t = TrainForm(vehicle_tab, operator_window)
            t.create_register_form()
    elif v=="buss":
        t=BussForm(buy_frame,root)
        t.create_search_form()
        if op==True:
            b = BussForm(vehicle_tab, operator_window)
            b.create_register_form()
    t = TicketForm(ticket_tab, operator_window)
    t.create_register_form()

# =============================================================================
# Windows
# =============================================================================

root=Tk()
root.resizable(0,0)

operator_window=Toplevel()

# =============================================================================
# Create Main Tabs
# =============================================================================

root_tabs=ttk.Notebook(root)

buy_tab=ttk.Frame(root_tabs)
# refund_tab=ttk.Frame(root_tabs)
operator_tab=ttk.Frame(root_tabs)

root_tabs.add(buy_tab,text='Buy Ticket')
# root_tabs.add(refund_tab,text='Refund Ticket')
root_tabs.add(operator_tab,text='Operator')
root_tabs.pack(expand = 1, fill ="both")

# =============================================================================
# Create Operator Tabs
# =============================================================================

operator_window_tabs=ttk.Notebook(operator_window)

vehicle_tab=ttk.Frame(operator_window_tabs)
ticket_tab=ttk.Frame(operator_window_tabs)

operator_window_tabs.add(vehicle_tab,text='Register Vehicle')
operator_window_tabs.add(ticket_tab,text='Register Ticket')
operator_window_tabs.pack(expand = 1, fill ="both")

# =============================================================================
# Logo
# =============================================================================
img=Image.open("./logo.png")
img=img.resize((950,180))
img=ImageTk.PhotoImage(img)

logo=Label(buy_tab,image=img)
logo.grid(row=0,column=0,rowspan=6,columnspan=40)

# logo=Label(refund_tab,image=img)
logo.grid(row=0,column=0,rowspan=6,columnspan=40)

logo=Label(operator_tab,image=img)
logo.grid(row=0,column=0,rowspan=6,columnspan=40)
#
logo=Label(vehicle_tab,image=img)
logo.grid(row=0,column=0,rowspan=6,columnspan=40)

logo=Label(ticket_tab,image=img)
logo.grid(row=0,column=0,rowspan=6,columnspan=40)

# =============================================================================
# Buy Ticket Tab
# =============================================================================
vehicle_radio=StringVar()
vehicle_radio.set("airplane")

airplane_radio=Radiobutton(buy_tab,text="Airplane",variable=vehicle_radio,value="airplane",state="normal",font=("Times", 14),fg="green",command=select_vehicle)
airplane_radio.grid(row=7,column=0,padx=10,pady=10)

train_radio=Radiobutton(buy_tab,text="Train",variable=vehicle_radio,value="train",font=("Times", 14),fg="green",command=select_vehicle)
train_radio.grid(row=7,column=1,padx=10,pady=10)

bus_radio=Radiobutton(buy_tab,text="Bus",variable=vehicle_radio,value="buss",font=("Times", 14),fg="green",command=select_vehicle)
bus_radio.grid(row=7,column=2,padx=10,pady=10)


# ================
# Search Frame
# ================

buy_frame = Frame(buy_tab)
buy_frame.grid(row=8, column=0, columnspan=40, sticky="NWES", pady=10)

# ================
# Operator Frame
# ================

operator_frame = Frame(operator_tab)
operator_frame.grid(row=8, column=0, columnspan=40, sticky="NWES", padx=150,pady=50)

user_label=Label(operator_frame,text="UserName ")
user_label.grid(row=0,column=0,padx=30,pady=10)

user_entry=Entry(operator_frame)
user_entry.grid(row=0,column=1)

pass_label=Label(operator_frame,text="Password ")
pass_label.grid(row=1,column=0)

pass_entry=Entry(operator_frame)
pass_entry.grid(row=1,column=1)


operator_button=Button(operator_frame,text="Login",command=login_operator)
operator_button.grid(row=2,column=1,pady=10)

warning_label=Label(operator_frame)
warning_label.grid(row=3,column=1)



airplane_radio=Radiobutton(vehicle_tab,text="Airplane",variable=vehicle_radio,value="airplane",state="normal",font=("Times", 14),fg="green",command=select_vehicle)
airplane_radio.grid(row=7,column=0,padx=10,pady=10)

train_radio=Radiobutton(vehicle_tab,text="Train",variable=vehicle_radio,value="train",font=("Times", 14),fg="green",command=select_vehicle)
train_radio.grid(row=7,column=1,padx=10,pady=10)

bus_radio=Radiobutton(vehicle_tab,text="Bus",variable=vehicle_radio,value="buss",font=("Times", 14),fg="green",command=select_vehicle)
bus_radio.grid(row=7,column=2,padx=10,pady=10)


# ========================
# ticket Frame
# ========================

ticket_frame = Frame(ticket_tab)
ticket_frame.grid(row=8, column=0, columnspan=40, sticky="NWES", pady=10)

# =============================================================================

reset=FormHelper()
reset.reset_json()

select_vehicle()
operator_window.withdraw()
root.mainloop()