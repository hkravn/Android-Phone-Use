import os
import time
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, bg='gray50', relief='raised')
canvas1.pack()


def unlock():
    key = input11.get()
    comm = "adb shell input keyevent 3 && adb shell input keyevent 82 && " \
           "adb shell input text " + key + " && adb shell input keyevent 66"
    os.system('cmd /c' + comm)


def call():
    mob_no = input21.get()
    time_to_dis = input22.get()
    comm = "adb shell am start -aandroid.intent.action.CALL -d " \
           "tel:" + mob_no
    os.system('cmd /c' + comm)
    time.sleep(int(time_to_dis))
    os.system('cmd /c adb shell input keyevent 6')


def sms():
    mob_no = input31.get()
    message = input32.get()
    comm = "adb shell am start -aandroid.intent.action.SENDTO -d " \
           "sms:" + mob_no + " --es sms_body \"" + str(message) + "\" --ez exit_on_sent true " \
            "&& adb shell input keyevent 61 && adb shell input " \
            "keyevent 61 && adb shell input keyevent 66"
    os.system('cmd /c' + comm)


def lock():
    comm = "adb shell input keyevent 26"
    os.system('cmd /c' + comm)


def home():
    comm = "adb shell input keyevent 3"
    os.system('cmd /c' + comm)



input11 = tk.Entry(root, show='*')
input21 = tk.Entry(root)
input22 = tk.Entry(root)
input31 = tk.Entry(root)
input32 = tk.Entry(root)

button1 = tk.Button(text='UNLOCK', command=unlock, bg='green',
                    fg='white', font=('helvetica', 12, 'bold'))

button2 = tk.Button(text='CALL', command=call, bg='green',
                    fg='white', font=('helvetica', 12, 'bold'))

button3 = tk.Button(text='SMS', command=sms, bg='green',
                    fg='white', font=('helvetica', 12, 'bold'))

button4 = tk.Button(text='LOCK', command=lock, bg='green',
                    fg='white', font=('helvetica', 12, 'bold'))

button5 = tk.Button(text='HOME', command=home, bg='green',
                    fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(50, 50, window=button1)
canvas1.create_window(160, 50, window=input11)

canvas1.create_window(50, 120, window=button2)
canvas1.create_window(160, 120, window=input21)
canvas1.create_window(320, 120, window=input22)

canvas1.create_window(50, 190, window=button3)
canvas1.create_window(160, 190, window=input31)
canvas1.create_window(320, 190, window=input32)

canvas1.create_window(250, 260, window=button4)
canvas1.create_window(150, 260, window=button5)

root.mainloop()
