import requests, base64, random, string, itertools

toUser = input("User to Bomb: ")

# Stuff you should NOT edit.
def xor(string: str, key: str) -> str: # Xor encoding
    return ("").join(chr(ord(x) ^ ord(y)) for x, y in zip(string, itertools.cycle(key)))
def base64_encode(string: str) -> str: # Encode Base64
    return base64.urlsafe_b64encode(string.encode()).decode()
def base64_decode(string: str) -> str: # Decode Base64
    return base64.urlsafe_b64decode(string.encode()).decode()
def generate_gjp(data): # Generate GJP for some requests
	return base64.b64encode(xor(data,"37526").encode()).decode()
def skedoosh(data): # the two lines of code @cv003 has been bugging me about for so long! :-)
	return xor(base64.b64decode(data.encode()).decode(),"37526") # har har har

# Get Account Info of You and the Victim
def getGJUsers(target):
    data={
        "secret":"Wmfd2893gb7",
        "str":target
    }
    hate = requests.post("http://www.boomlings.com/database/getGJUsers20.php",data=data,headers={"User-Agent": ""}).text.split(":")[1::2]
    username = hate[0]
    uuid = hate[2]
    accountid = hate[10]
    return (username, accountid, uuid)
  
# Upload Message
def uploadGJMessage(user, passw, sendto):
    msgdata = {
        "accountID": getGJUsers(user)[1],
        "gjp": generate_gjp(passw),
        "toAccountID": getGJUsers(sendto)[1],
        "subject": base64.b64encode(b"test").decode(),
        "body": base64.b64encode(b"hello kind sir").decode(),
        "secret": "Wmfd2893gb7",
    }
    msg = requests.post('http://www.boomlings.com/database/uploadGJMessage20.php', data=msgdata, headers={"User-Agent":""})
    print(msg.text)
 

# Read accounts.txt for accounts. 
with open("accounts.txt", "r") as file:
    lines = file.readlines()
accounts = []
for line in lines:
    username, password = line.strip().split(":")
    accounts.append((username, password))
    
# Cowabunga
for username, password in accounts:
    print(f"Using Account: {username}")
    
    # Increase this if you want, I dont know how much you can do.
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
    uploadGJMessage(username, password, toUser)
