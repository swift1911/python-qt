import _winreg
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",0,_winreg.KEY_ALL_ACCESS) 
l=_winreg.QueryValueEx(key,"ProxyEnable")
if l[0]==0:
    _winreg.SetValueEx(key,"ProxyEnable",0, _winreg.REG_DWORD, 1)  
    _winreg.SetValueEx(key,"ProxyServer",0, _winreg.REG_SZ, "127.0.0.1:1041") 
    print ("start proxy")
else :
    print("disable proxy")
    _winreg.SetValueEx(key,"ProxyEnable",0, _winreg.REG_DWORD, 0)  
