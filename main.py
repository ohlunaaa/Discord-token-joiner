import requests
from threading import Thread
import random
from colorama import Fore



tokens = []

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def joiner(token,inv):
    headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US",
                    "Authorization": token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk1NzU5NTAwODQxOTEyNzMwNiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5NTc1OTUwMDkyNTc5NjM1NzMiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiIxMDE2NzY1Mjc1ODUwNDEyMDkyIn0=",
                    "x-debug-options": "bugReporterEnabled",
                    "x-discord-locale": "en-US",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2dpdGh1Yi5jb20vTElMLUpBQkEvdmFsY2hlY2tlciIsInJlZmVycmluZ19kb21haW4iOiJnaXRodWIuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDU0MjksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
                }

    r = requests.post(f"https://discord.com/api/v9/invites/{inv}",headers=headers)
    if r.status_code in (204,200,201):
        print(f"{Fore.GREEN}[+] {Fore.RESET}Joined ")
        return
    else:
        print(f"{Fore.RED}[-] {Fore.RESET}Failed")
        return 

def load_file():
        try:
            data = open("tokens.txt", encoding="utf8", errors="ignore").readlines()
            for x in data:
                token = x.replace("\n", "")
                tokens.append(token)
        except:
            print("Failed")
            input()


def main():
        print(f"""{Fore.LIGHTMAGENTA_EX}
▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ▄▄▄██▀▀▀▒█████   ██▓ ███▄    █ ▓█████  ██▀███  
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌      ▒██  ▒██▒  ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌      ░██  ▒██░  ██▒▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▓██▄██▓ ▒██   ██░░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓     ▓███▒  ░ ████▓▒░░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ▒▓▒▒░  ░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒     ▒ ░▒░    ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░     ░ ░ ░  ░ ░ ░ ▒   ▒ ░   ░   ░ ░    ░     ░░   ░ 
   ░     ░        ░  ░ ░          ░ ░     ░        ░        ░   ░      ░ ░   ░           ░    ░  ░   ░     
 ░                   ░                           ░{Fore.RESET}""")
        load_file()
        inv = input("Invite: ")
        running = []
        for data in tokens:
            if ":" in data:
                token = data.split(":")[1]
            else:
                token = data
            t = Thread(target=joiner, args=(token,inv))
            t.start()
            running.append(t)

        for x in running:
            x.join()
main()

