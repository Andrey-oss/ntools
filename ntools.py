# Import modules

print ("[\x1B[1mDEBUG] Running NTools v1.2-5")
print ("[\x1B[1mDEBUG] Loading modules")
try:
    import tkinter as tk
    print ("[\x1B[1mDEBUG] Loaded tkinter module")
except Exception:
    print("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot import tkinter module")
    sys.exit()

try:
    from tkinter import *
    from tkinter import messagebox
    print ("[\x1B[1mDEBUG] Loaded all tkinter submodules")
except Exception:
    print("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot import tkinter module")
    sys.exit()

try:
    import requests
    print ("[\x1B[1mDEBUG] Loaded requests module")
except Exception:
    print("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot import requests module")
    sys.exit()

try:
    print ("[\x1B[1mDEBUG] Checking internet connection")
    r = requests.get("https://github.com", timeout=9)
    print ("[\x1B[1mDEBUG] Internet connection has been detected!")
except Exception:
    print("[\x1B[31mFATAL\x1B[0m] \x1B[1mInternet connection is unavailable")
    messagebox.showwarning("Warning","Internet connection is unavailable! NTools work will be incorrect")

import sys
import time

# Creating raw GUI (UI)

root = tk.Tk()
root.geometry('1000x900')
root.title("NTools 1.2-5")
root.configure(background='#242526')

# Creating function commands

def exit():
    print ("[\x1B[1mDEBUG] Printing messagebox 'Exit' 'Thanks for using this app'")
    messagebox.showinfo("Exit","Thanks for using this app")
    time.sleep(0.5)
    print ("[\x1B[1mDEBUG] Exiting...")
    sys.exit()

def myip():
    try:
        print ("[\x1B[1mDEBUG] \x1B[1mRequesting to api64.ipify.org")
        myip = requests.get("http://api64.ipify.org").text
        print ("[\x1B[1mDEBUG] Connection accepted! IP will be "+str(myip))
    except Exception:
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot connect to api64.ipify.org")
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mIP will be 'Unknown' by default")
        myip = ("Unknown")

    clearable_square = Canvas(root, width=800, height=800, background='#242526', relief=SUNKEN).place(x=300, y=100)
    Label(bg='#242526', fg='white', text="Your IP - "+str(myip), font=('Mystical', 15)).place(x=400, y=400, width=500, height=50)

def help():
    square = Canvas(root, width=800, height=800, background='#242526', relief=SUNKEN).place(x=300, y=100)
    print ("[\x1B[1mDEBUG] \x1B[1mCreating 'About' title for help command as about")
    help_0 = Label(bg='#242526', fg='white', text="About", font=('Arial', 20)).place(x=400, y=120, width=500, height=50)
    print ("[\x1B[1mDEBUG] \x1B[1mCreating 'NTools - Network Tools' for help/About as description")
    help_1 = Label(bg='#242526', fg='white', text="NTools - Network Tools", font=('Arial', 20)).place(x=400, y=300, width=500, height=50)

def ip_forwarding():
    try:
        print ("[\x1B[1mDEBUG] \x1B[1mRequesting to ifconfig.me")
        ip_forwarding = requests.get("http://ifconfig.me/forwarded", timeout=9).text
        print ("[\x1B[1mDEBUG] Connection accepted! IP forwarding will be "+str(myip))
    except Exception:
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot connect to ifconfig.me")
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mIP Forwarding will be 'Unknown' by default")
        ip_forwarding = ("Unknown")

    clearable_square = Canvas(root, width=800, height=800, background='#242526', relief=SUNKEN).place(x=300, y=100)
    Label(bg='#242526', fg='white', text="IP Forwarding - "+str(ip_forwarding), font=('Mystical', 12)).place(x=310, y=400, width=700, height=50)
def my_isp():
    try:
        print ("[\x1B[1mDEBUG] \x1B[1mRequesting to ifconfig.co with JSON standart")
        r = requests.get("http://ifconfig.co/json", timeout=9)
        print ("[\x1B[1mDEBUG] Connection accepted!")
        print ("[\x1B[1mDEBUG] Decoding JSON format")
        data = r.json()
        print ("[\x1B[1mDEBUG] Getting 'asn_org' row in JSON")
        my_isp = data['asn_org']
        print ("[\x1B[1mDEBUG] All done! ISP will be "+data['asn_org'])
    except Exception:
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot connect to ifconfig.co")
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mISP will be 'Unknown' by default")
        my_isp = ("Unknown")

    clearable_square = Canvas(root, width=800, height=800, background='#242526', relief=SUNKEN).place(x=300, y=100)
    Label(bg='#242526', fg='white', text="Your ISP - "+str(my_isp), font=('Mystical', 15)).place(x=400, y=400, width=500, height=50)

def isp_hostname():
    try:
        print ("[\x1B[1mDEBUG] \x1B[1mRequesting to ifconfig.co with JSON standart")
        r = requests.get("http://ifconfig.co/json", timeout=9)
        print ("[\x1B[1mDEBUG] Connection accepted!")
        print ("[\x1B[1mDEBUG] Decoding JSON format")
        data = r.json()
        print ("[\x1B[1mDEBUG] Getting 'hostname' row in JSON")
        isp_hostname = data['hostname']
        print ("[\x1B[1mDEBUG] All done! ISP will be "+isp_hostname)
    except Exception:
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mCannot connect to ifconfig.co")
        print ("[\x1B[31mFATAL\x1B[0m] \x1B[1mISP hostname will be 'Unknown' by default")
        isp_hostname = ("Unknown")

    clearable_square = Canvas(root, width=800, height=800, background='#242526', relief=SUNKEN).place(x=300, y=100)
    Label(bg='#242526', fg='white', text="ISP Hostname - "+str(isp_hostname), font=('Mystical', 15)).place(x=400, y=400, width=500, height=50)

# Creating GUI

square = Canvas(root, width=800, height=800, background='#242526', relief=SUNKEN).place(x=300, y=100)
middlemenu = Label(bg='#333333', fg='#333333', relief=GROOVE).place(x=-1, y=98, width=300, height=900)
motd_text = Label(bg='#242526', fg='white', text="Choose something from the menu and your choice will appear here", font=('Mystical', 10)).place(x=400, y=400, width=500, height=50)
help_button = Button(text='Help', activebackground='#333333', command=help, activeforeground='white', bg='#333333', relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=170, width=250)
exit_button = Button(text='Exit', activebackground='#333333', activeforeground='white', command=exit, bg='#333333', relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=240, width=250)
default_menu = Label(text='Default options', activebackground='#333333', activeforeground='white', bg='#333333', relief=GROOVE, fg='white', font=('Oracle', 16)).place(x=-1, y=97, height=50, width=300)
upmenu = Label(bg='#4169e1', fg='#4169e1', relief=GROOVE).place(x=-1, y=-1, width=1005, height=100)
ntools_menu = Label(text='IP Tools', activebackground='#333333', activeforeground='white', bg='#333333', relief=GROOVE, fg='white', font=('Oracle', 16)).place(x=-1, y=310, height=50, width=300)
myip = Button(text='My IP', activebackground='#333333', activeforeground='white', command=myip, bg='#333333', relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=390, width=250)
ip_forward = Button(text='IP Forwarding', activebackground='#333333', activeforeground='white', bg='#333333', command=ip_forwarding, relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=460, width=250)
isp_menu = Label(text='ISP Tools', activebackground='#333333', activeforeground='white', bg='#333333', relief=GROOVE, fg='white', font=('Oracle', 16)).place(x=-1, y=540, height=50, width=300) # oter_menu
myisp = Button(text='My ISP', activebackground='#333333', activeforeground='white', bg='#333333', command=my_isp, relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=620, width=250)
myisp = Button(text='ISP Hostname', activebackground='#333333', activeforeground='white', bg='#333333', command=isp_hostname, relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=700, width=250)
#version = Label(text="NTools v1.2-5 by Andreyoss", bg='#4169e1', fg='white', font=('Arial', 20)).place(x=320, y=30)
#donate_button = Button(text='Donate', activebackground='#333333', activeforeground='white', bg='#333333', relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=610, width=250)
#aboutauthor_button = Button(text='About creator', activebackground='#333333', activeforeground='white', bg='#333333', relief=FLAT, fg='white', font=('Oracle', 20)).place(x=20, y=690, width=250)

root.mainloop()
