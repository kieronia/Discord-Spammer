import requests,os,threading,time,webbrowser
from colorama import Fore, init, Style
init(convert = True)
os.system("title Discord AIO Spammer")
tokenfile = "tokens.txt"
i = 0
valid = 0
invalid = 0
cooltitles = "menu"
validsend = 0
os.system("cls")
print(f"""\033[95m
      _ _                       _         _            
     | (_)                     | |       (_)           
   __| |_ ___  ___ ___  _ __ __| |   __ _ _  ___       
  / _` | / __|/ __/ _ \| '__/ _` |  / _` | |/ _ \      
 | (_| | \__ \ (_| (_) | | | (_| | | (_| | | (_) |     
  \__,_|_|___/\___\___/|_|  \__,_|_ \__,_|_|\___/ 
         {Fore.WHITE}[{Fore.RED}AGAINST TOS - DO NOT USE!{Fore.WHITE}]
""")

with open(tokenfile) as f:
    for i, l in enumerate(f):
        pass
linecount = i + 1
print(f"{Fore.CYAN} > Tokens should be loaded to {Fore.WHITE}[{Fore.RED}{tokenfile}{Fore.WHITE}]\n {Fore.CYAN}> Token Count {Fore.WHITE}[{Fore.RED}{linecount}{Fore.WHITE}]")
print("\033[95m > Continuing...")
time.sleep(1.5)
os.system("cls")
def cooltitlelel():
	global validsend
	global invalid
	global valid
	while cooltitles == "menu":
		os.system("title Menu -- Work from github.com/kieronia")
		time.sleep(2)
		os.system('title Type "1" To Make Tokens Dm / Server Spam')
		time.sleep(1)
		os.system('title Type "2" To Make Tokens Join Server ')
		time.sleep(1)
		os.system('title Type "3" To Make Tokens Leave Server ')
		time.sleep(1)
		os.system('title Type "4" To Make Tokens Add Someone ')
		time.sleep(1)
		os.system('title Type "5" To Make Tokens Type')
		time.sleep(1)
		os.system('title Type "6" To See My Website')
		time.sleep(1)
		os.system('title Type "7" To Validate Tokens')
		time.sleep(1)
		os.system('title Type "8" To Exit')
		time.sleep(1)
		os.system(f'title Tokens Loaded : [{linecount}]')
		time.sleep(1)
	while cooltitles == "dm":
		os.system(f'title Input Amount to spam')
		time.sleep(1)
		os.system(f'title Input ID of server/user to spam')
		time.sleep(1)
		os.system(f'title Input Message to spam')
		time.sleep(1)
		os.system(f'title Tokens Loaded : [{linecount}]')
		time.sleep(1)
	while cooltitles == "dmprog":
		os.system(f'title Spamming Messages : [{validsend}]')
	while cooltitles == "typing":
		os.system(f'title Typing.')
		time.sleep(0.1)
		os.system(f'title Typing..')
		time.sleep(0.1)
		os.system(f'title Typing...')
		time.sleep(0.2)
		os.system(f'title Several People Are Typing.')
		time.sleep(0.1)
		os.system(f'title Several People Are Typing..')
		time.sleep(0.1)		
		os.system(f'title Several People Are Typing...')
		time.sleep(0.2)		

	while cooltitles == "website":
		os.system(f'title kieronia.com')
		time.sleep(2)
		os.system(f'title github.com/kieronia')
		time.sleep(2)

	while cooltitles == "friend":
		os.system(f'title Add Friend')
		time.sleep(2)
		os.system(f'title Remove Friend')
		time.sleep(2)




	while cooltitles == "friendinprog":
		os.system(f'title Success : [{validsend}]')
		time.sleep(1)
		os.system(f'title Tokens Loaded : [{linecount}]')
		time.sleep(1)


	while cooltitles == "validating":
		os.system(f'title Valids : [{valid}] Invalids : [{invalid}]')
		time.sleep(1)
		os.system(f'title Tokens Loaded : [{linecount}]')
		time.sleep(1)



def spamming(line):

	global validsend
	global totalnumber
	global idofuser
	global msg
	try:
		token = line.strip()
		for i in range(totalnumber):
		
				headers = {'Authorization': token}
				messagesend = requests.post(f"https://discord.com/api/v8/channels/{idofuser}/messages",json={'content': msg}, headers=headers)
				if messagesend.status_code == 200:
					print(f"{Fore.GREEN} > Message Sent")
					validsend = validsend + 1

	except:
		pass
	

def friendadd(line):

	global validsend
	global idofuser
	try:
		token = line.strip()
		
		headers = {'Authorization': token}
		messagesend = requests.put(f"https://discord.com/api/v8/users/@me/relationships/{idofuser}",json={}, headers=headers)
		if messagesend.status_code == 204:
			print(f"{Fore.GREEN} > Request Sent")
			validsend = validsend + 1

	except:
		pass


def friendremove(line):

	global validsend
	global idofuser
	try:
		token = line.strip()
		
		headers = {'Authorization': token}
		messagesend = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{idofuser}", headers=headers)
		if messagesend.status_code == 204:
			print(f"{Fore.GREEN} > Request Deleted")
			validsend = validsend + 1

	except:
		pass




def typing(line):


	global idofuser
	try:
		token = line.strip()
		while True:
		
				headers = {'Authorization': token}
				messagesend = requests.post(f"https://discord.com/api/v8/channels/{idofuser}/typing", headers=headers)
				if messagesend.status_code == 204:
					print(f"{Fore.GREEN} > Typing")

	except:
		pass
	


def join(line):


	global server
	try:
		token = line.strip()
		while True:
		
				headers = {'Authorization': token}
				leave = requests.post(f'https://discord.com/api/v6/invites/{server}', headers=headers, timeout=10).status_code
				if messagesend.status_code == 200:
					print(f"{Fore.GREEN} > Joined!")

	except:
		pass



def leave(line):


	global serverid
	try:
		token = line.strip()
		while True:
		
				headers = {'Authorization': token}
				leave = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{serverid}', headers=headers, timeout=10).status_code
				if messagesend.status_code == 204:
					print(f"{Fore.GREEN} > Left!")

	except:
		pass



def tokenkek(line):
    global invalid
    global valid
    try:
        token = line.strip()
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get("https://discordapp.com/api/v6/users/@me/library", headers=headers)
        if r.status_code == 200:
            print(f"{Fore.GREEN}{token}")
            f = open("valid.txt",'a')
            f.write(token + "\n")
            valid = valid + 1
        else:
            print(f"{Fore.RED}{token}")
            invalid = invalid + 1
    except:
        pass


logo = f"""
			   {Fore.WHITE}> {Fore.RED}kieronia.com {Fore.WHITE}>{Fore.RED} github.com/kieronia

	\033[95m	    	   ╔══════════════════════════════════════════════════════╗
			   ║{Fore.WHITE} [1] {Fore.RED}Dm/Server Spam             \033[95m                      ║         
			   ║{Fore.WHITE} [2] {Fore.RED}Joiner              \033[95m                             ║               
			   ║{Fore.WHITE} [3] {Fore.RED}Leaver       \033[95m                                    ║                  
			   ║{Fore.WHITE} [4] {Fore.RED}Friend Spammer \033[95m                                  ║
			   ║{Fore.WHITE} [5] {Fore.RED}Typing Spammer            \033[95m                       ║
			   ║{Fore.WHITE} [6] {Fore.RED}Website \033[95m                                         ║
			   ║{Fore.WHITE} [7] {Fore.RED}Validate   \033[95m                                      ║
			   ║{Fore.WHITE} [8] {Fore.RED}Exit       \033[95m                                      ║
			   ╚══════════════════════════════════════════════════════╝
"""

print(logo)
threading.Thread(target = cooltitlelel).start()

validsend = 0

options = input(" ═> Option?\n ═> ")


	

if "1" in options:
		cooltitles = "dm"
		totalnumber = int(input(" ═> Number of messages to send PER TOKEN?\n ═> "))
		idofuser = int(input(" ═> ID of User/Server CHANNEL to Spam?\n ═> "))
		msg = input(" ═> Message To Spam?\n ═> ")
		cooltitles = "dmprog"
		with open(tokenfile, 'r') as f:
				for line in f.readlines():
						try:
								threading.Thread(target = spamming, args = (line,)).start()
						except:
								pass


if "2" in options:
		cooltitles = "join"
		server = input(" ═> Invite, eg discord.gg/kieronia, you'd type kieronia?\n ═> ")
		with open(tokenfile, 'r') as f:
				for line in f.readlines():
						try:
								threading.Thread(target = join, args = (line,)).start()
						except:
								pass





if "3" in options:
		cooltitles = "leave"
		serverid = int(input(" ═> Server ID?\n ═> "))
		with open(tokenfile, 'r') as f:
				for line in f.readlines():
						try:
								threading.Thread(target = leave, args = (line,)).start()
						except:
								pass






elif "4" in options:
		cooltitles = "friend"
		idofuser = int(input(" ═> ID of User?\n ═> "))
		typeoffriend = input(" ═> 1 = Add , 2 = Remove?\n ═> ")
		time.sleep(1)
		cooltitles = "friendinprog"
		#over complicated but meh
		if typeoffriend == "1":
				with open(tokenfile, 'r') as f:
						for line in f.readlines():
								try:
										threading.Thread(target = friendadd, args = (line,)).start()
								except:
										pass
		elif typeoffriend == "2":

				with open(tokenfile, 'r') as f:
						for line in f.readlines():
								try:
										threading.Thread(target = friendremove, args = (line,)).start()
								except:
										pass

		else:
				print(f"{Fore.RED}X Invalid Option :|")


elif "5" in options:
		cooltitles = "typing"
		idofuser = int(input(" ═> ID of Server CHANNEL to Spam?\n ═> "))
		print(" ═> Typing!")
		time.sleep(1)
		cooltitles = "dmprog"
		with open(tokenfile, 'r') as f:
				for line in f.readlines():
						try:
								threading.Thread(target = typing, args = (line,)).start()
						except:
								pass








elif "6" in options:
		cooltitles = "website"
		typeofsite = input(" ═> 1 = Github , 2 = My Website.\n ═> ")
		if typeofsite == "1":
				webbrowser.open("https://github.com/kieronia?tab=repositories")
				input(" ═>")
		elif typeofsite == "2":
				webbrowser.open("http://kieronia.com")
				input(" ═>")
		else:
				print(f"{Fore.RED} > Invalid Input")


elif "7" in options:
		cooltitles = "validating"

		input(" ═> Checking off tokens.txt , press enter to continue!\n ═> ")
		print(" ═> Checking...!")
		with open(tokenfile, 'r') as f:
				for line in f.readlines():
						try:
								threading.Thread(target = tokenkek, args = (line,)).start()
						except:
								pass


                  



elif "8" in options:
		os._exit(0)


	
