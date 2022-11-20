import httpx, requests
import colorama
from colorama import Fore, init
from pathlib import Path
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
cyan = Fore.CYAN

def cls(): #clears the terminal
    os.system('cls' if os.name=='nt' else 'clear')


def get_all_tokens(filename):
    all_tokens = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            token = line.strip()
            token = find_token(token)
            if token != None:
                all_tokens.append(token)

    return all_tokens

def checkEmpty(file):
    mypath = Path(file)

    if mypath.stat().st_size == 0:
        return True
    else:
        return False

def nitrochecker():

    three_m_working = 0
    one_m_working = 0

    three_m_used = 0
    one_m_used = 0

    three_m_nonitro = 0
    one_m_nonitro = 0

    three_m_invalid = 0
    one_m_invalid = 0

    three_m_locked = 0
    one_m_locked = 0

    three_m_tokens = get_all_tokens("3m_tokens.txt")
    one_m_tokens = get_all_tokens("1m_tokens.txt")
    print("Checking 3 Months Nitro Tokens")

    if checkEmpty("3m_tokens.txt"):
        print(red + "No Stock To Check" + white)

    else:

        for token in three_m_tokens:    
            file = "3m_tokens.txt"
            s, headers = get_headers(token)
            profile = validate_token(s, headers)

            if profile != False:
                boost_data = s.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers={'Authorization': token})

                if boost_data.status_code == 403:
                    print(red + f" ✗ {white}{token} - {profile}{red} [LOCKED]" + white)
                    removeToken(token, file)
                    three_m_locked += 1
                if len(boost_data.json()) != 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                    if boost_data.json()[0]['cooldown_ends_at'] != None:
                        print(red + f" ✗ {white}{token} - {profile}{red} [USED]" + white)
                        removeToken(token, file)
                        three_m_used += 1
                if len(boost_data.json()) == 0:
                    removeToken(token, file)
                    print(f"{red} ✗ {white}{token} - {profile}{red} [NO NITRO]" + white)
                    three_m_nonitro += 1
                else:
                    if len(boost_data.json()) != 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                        if boost_data.json()[0]['cooldown_ends_at'] == None:

                            print(f"{green} ✓ {white}{token} - {profile}{green} [WORKING]" + white)
                            three_m_working += 1
            else:
                print(red + f" ✗ {white}{token}{red} [INVALID]" + white)
                removeToken(token, file)
                three_m_invalid += 1
    print()
    print("Checking 1 Month Nitro Tokens")
    if checkEmpty("1m_tokens.txt"):
        print(red + "No Stock To Check" + white)  
    else:
        for token in one_m_tokens:    
            file = "1m_tokens.txt"
            s, headers = get_headers(token)
            profile = validate_token(s, headers)
            if profile != False:
                boost_data = s.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers={'Authorization': token})

                if boost_data.status_code == 403:
                    print(red + f" ✗ {white}{token} - {profile}{red} [LOCKED]" + white)
                    removeToken(token, file)
                    one_m_locked += 1
                if len(boost_data.json()) != 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                    if boost_data.json()[0]['cooldown_ends_at'] != None:
                        print(red + f" ✗ {white}{token} - {profile}{red} [USED]" + white)
                        removeToken(token, file)
                        one_m_used += 1
                if len(boost_data.json()) == 0:
                    removeToken(token, file)
                    print(f"{red} ✗ {white}{token} - {profile}{red} [NO NITRO]" + white)
                    one_m_nonitro += 1
                else:
                    if len(boost_data.json()) != 0 and boost_data.status_code == 200 or boost_data.status_code == 201:
                        if boost_data.json()[0]['cooldown_ends_at'] == None:

                            print(f"{green} ✓ {white}{token} - {profile}{green} [WORKING]" + white)
                            one_m_working += 1
            else:
                print(red + f" ✗ {white}{token}{red} [INVALID]" + white)
                removeToken(token, file)
                one_m_invalid += 1

    print(f"{green}WORKING (with nitro) : {white}{three_m_working}  |  {red}USED : {white}{three_m_used}  |  {red}NO NITRO : {white}{three_m_nonitro}  |  {red}LOCKED : {white}{three_m_locked}  |  {red}INVALID : {white}{three_m_invalid}")
    print(f"{green}WORKING (with nitro) : {white}{one_m_working}  |  {red}USED : {white}{one_m_used}  |  {red}NO NITRO : {white}{one_m_nonitro}  |  {red}LOCKED : {white}{one_m_locked}  |  {red}INVALID : {white}{one_m_invalid}")

cls()
nitrochecker()