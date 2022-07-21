from colorama import Fore, init
import time
import random
import string

init()

import os
from os import system
system("title " + "Fake BTC Or ETH Wallet Miner,   Made By Thraxx#1402,   Discord: https://discord.gg/49YAGUEcMf") #title

wa = input(Fore.MAGENTA + "Enter your address: ")
time.sleep(1)
print(Fore.MAGENTA + "Connecting to " + wa)
time.sleep(3)
print(Fore.GREEN + "Success")
time.sleep(1)
print(Fore.MAGENTA + "Proceeding")

BE = input("Would you like to mine ETH or BTC wallets?: ")

def Eth_Btc():

    def id_gen(size = 35, chr = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.ascii_letters):
        return "".join(random.choice(chr) for _ in range(size))

    ae = ['0.000537', '0.008735', '0.000046', '0.001755', '0.028934', '0.000005', '0.054482', '0.173846', '0.000286', '0.008463', '0.000007', '0.009324'] #diffrent ammounts to get

    luck = 0
    
    init()
    if (BE == "ETH"):
        while True:
            if (luck > random.randint(100000, 100000)): #chance of getting vaild
                aer = random.choice(ae)
                print(Fore.GREEN + "[+] " + "0X" + id_gen() + " |  Vaild  | " + "+ " + aer + " ETH")
                time.sleep(1)
                print("Transfeing the " + aer + "ETH to " + wa)
                luck = 0
                time.sleep(2)
                print("Proceeding")
                time.sleep(1)
            else:    
                print(Fore.RED + "[-] " + "0X" + id_gen() + " | Invaild | " + "+ 0.000000 ETH")
                time.sleep(0.001)
                luck += 1

    init()
    if (BE == "BTC"):
        while True:
            if (luck > random.randint(100000, 1000000)):
                aer = random.choice(ae)
                print(Fore.GREEN + "[+] " + "0X" + id_gen() + " |  Vaild  | " + "+ " + aer + " BTC")
                time.sleep(1)
                print("Transfeing the " + aer + "BTC to " + wa)
                luck = 0
                time.sleep(2)
                print("Proceeding")
                time.sleep(1)
            else:    
                print(Fore.RED + "[-] " + "0X" + id_gen() + " | Invaild | " + "+ 0.000000 BTC")
                time.sleep(0.001)
                luck += 1

if BE == "ETH" or 'BTC':
    Eth_Btc()

print(Fore.RED + "Incorrect Option")
print(Fore.RED + "Closing")
time.sleep(5)
