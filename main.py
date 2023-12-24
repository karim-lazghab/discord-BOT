from http.client import HTTPSConnection
from keep_alive import keep_alive
import requests
import time
import random
import json
import urllib.request
from bs4 import BeautifulSoup
import datetime

headers = {
  'authorization':'' # Your authorization token
}


def keeping_alive():
  keep_alive()
  time.sleep(3500)
  keep_alive()
  return

def URL_aleatoire():
    global server_id
    global server
    global URL
    global act_URL
    alea_URL = random.randrange(4) + 1
    alea_URL=8
    general_msg_URL="https://discord.com/api/v9/channels/"
    general_URL="https://discord.com/channels/"

    #DMC SERVER
    if alea_URL in [1,3,2] or alea_URL == 8 :
        server_id ="682809584985178135/"
        alea_list = random.randrange(15)
        if alea_list in [1,3,5,7,9]:
          time.sleep(10)
        alea_list=0
        channel_list = ["754476152210587758","754477169572315226","754477397348188170","755063241515728946","755063349313536001","756127665592860743","756127972297146429","756128036327260240","756128102823886958","756128173581664286","756988497197531257","756988555271864460","756992787576258720","756993724013215744","821534553336315934"]
        act_URL =general_URL+server_id+channel_list[alea_list]
        URL =f"{general_msg_URL}{channel_list[alea_list]}/messages"
        print(act_URL)
        server='DMC channel '+str(alea_list+1)
    #PEPE CITY SERVER
    elif alea_URL == 4:

        server_id ="771673695613091840/"
        alea_list = random.randrange(3)
        channel_list=["847192375129800774","847192351301959711","847192301339148348"]

        act_URL = general_URL+server_id+channel_list[alea_list]
        URL = f"{general_msg_URL}{channel_list[alea_list]}/messages"
        print(act_URL)
        server='PEPE CITY channel '+str(alea_list+1)
    #DANK REVIVAL
    elif alea_URL == 5:
        server_id ="796236163681091594/"
        alea_list = random.randrange(3)
        channel_list=["796236164603707396","796236164603707397","796254203659681832"]
        act_URL = general_URL+server_id+channel_list[alea_list]
        URL = f"{general_msg_URL}{channel_list[alea_list]}/messages"
        print(act_URL)
        server='DANK REVIVAL channel '+str(alea_list+1)
    #DANK CAFE
    elif alea_URL == 5:
        server_id = "798822518571925575/"
        alea_list = random.randrange(3)
        channel_list=["825804542301044778","808516141886079026","808516159464144926"]
        act_URL = general_URL+server_id+channel_list[alea_list]
        URL = f"{general_msg_URL}{channel_list[alea_list]}/messages"
        print(act_URL)
        server='DANK CAFE channel '+str(alea_list+1)
    #THE FARM
    elif alea_URL == 4:
        server_id ="645753561329696785/"
        alea_list = random.randrange(6)
        if alea_list in [1,3]:
          time.sleep(10)
        channel_list=["658773737436479498","714295890310987787","714314043950759966","689175977410297947","748062748331606017","748063323672805456"]
        act_URL = general_URL+server_id+channel_list[alea_list]
        URL = f"{general_msg_URL}{channel_list[alea_list]}/messages"
        print(act_URL)
        server = 'THE FARM channel '+str(alea_list+1)
    #DANK DIMENSION
    elif alea_URL == 5 :
        server_id ="645753561329696785/"
        alea_list = random.randrange(3)
        if alea_list in [1,3]:
          time.sleep(10)
        channel_list=["805878227909607434","805878456906285116","805878693297127515"]
        act_URL = general_URL+server_id+channel_list[alea_list]
        URL = f"{general_msg_URL}{channel_list[alea_list]}/messages"
        print(act_URL)
        server = 'DANK DIMENSION '+str(alea_list+1)
    #DANK DIMENSION
    else:
      server_id ="645753561329696785/"
      alea_list = random.randrange(3)
      if alea_list in [1,3]:
        time.sleep(10)
      channel_list=["805878227909607434","805878456906285116","805878693297127515"]
      act_URL = general_URL+server_id+channel_list[alea_list]
      URL = f"{general_msg_URL}{channel_list[alea_list]}/messages"
      print(act_URL)
      server = 'DANK DIMENSION '+str(alea_list+1)
    f = open("file.txt", "a")
    f.write(f"{server}\n")
    f.close()
    print(server)
    return URL

def communication():
    f = open("file.txt", "a")
    write_messages()
    check_for_mentions()
    while len(value["embeds"])==0:
      check_for_mentions()
    sort_mentions()
    print('------------------------------------------')
    f.write("------------------------------------------\n")
    f.close()
    return

def write_messages():
    URL_aleatoire()
    global payload
    payload = {
        'content': f"{content}"
    }
    requests.post(URL, data=payload, headers=headers)
    return


def check_for_mentions():
    global jsonn
    global message
    global name
    global head_data
    global value
    global message_id
    global custom_id
    global mentioned
    time.sleep(2)
    connection = HTTPSConnection("discordapp.com", 443)
    read = requests.get(URL, headers=headers)
    jsonn = json.loads(read.text)
    f=open("supermisc.txt","a")
    f.write(f"this is the first jsonn\n\n{jsonn}\n\nthis was the first jsonn")
    f.close()
    for value in jsonn:
        name = value['author']['username']
        if len(name)==0:
          name ='null'
        mentioned = 'null'
        message= value['content']
        message_id = value['id']
        if len(message)==0 :
          message_id = ''
        
        if len(value['mentions']) == 1:
            if value['mentions'][0]['username'] == 'Karim' or value["author"]["username"]=="Karim":
                mentioned = 'Karim'
                #dank memer mentioned me
                if name == 'Dank Memer':
                    message = value['content']
                    if content == 'pls beg': 
                      if len(value['embeds']) !=0:
                        message = value['embeds'][0]['description']
                      else:
                        message='can not get the beg message'
                    print(name)
                    f = open("file.txt", "a")
                    f.write(f"{name}\n")     
                    if len(message)!=0 and not(content =='pls search') and not(content =='pls crime'):
                      print(message)
                      f.write(f"{message}\n")
                    f.close()

                    return name, mentioned, message

                elif 'Work for' in message:
                    f=open("misc.txt","a")
                    f.write(f"this is the fist value \n\n {value}\n\nthis was the first value\n")
                    f.close()
def sort_mentions():
    global index
    global intmoney
    global message1
    f=open("misc.txt","a")
    f.write("now at  sorting \n")
    f.close
    msg=''
    button_options_id=[]
    button_options_label=[]
    if '`' in message or "Emoji Match" in message:
      time.sleep(5)
    if len(value["embeds"]) !=0 :
      for x in range(len(value["embeds"])-1):
        button_options_id.append(value['components'][0]['components'][x]['custom_id'])
        button_options_label.append(value['components'][0]['components'][x]['label'])
        print(x)
    if "Soccer" in message :
      f=open("misc.txt","a")
      f.write("now at soccer sorting \n")
      f.close
      p1 = message.find(':\n')
      for i in range (p1+2,len(message)):
        if message[i] ==' ':
            msg += '_'
        else:
            msg += message[i]
      print('this is the msg:')
      print(msg)
      lev_pos=msg.find('levitate:')
      if lev_pos in[0,1,2]:
        print('\nthis is the print ":levitate:" message \n',lev_pos)
        index = button_options_id[0]

      elif lev_pos in[7,8,9]:
        index=button_options_id[1]
      elif lev_pos in [13,14,15]:
        index=button_options_id[2]
      else:
        index = random.randrange(3)
        f=open("misc.txt","a")
        f.write("got the index from randrange \n")
        f.close
    else:
        index = random.randrange(3)
        f=open("misc.txt","a")
        f.write(f"got the index from randrange cause game is not soccer\n")
        f.close
    f=open("misc.txt","a")
    f.write(f"\nthis is index '{index}'\n button_options_id is : {button_options_id} \n and button_options_label is : {button_options_label}\n")
    f.close()
    
    
    read = requests.get(URL, headers=headers)
    jsonn = json.loads(read.text)
    f=open("supermisc.txt","a")
    f.write(f"this is the second jsonn\n\n{jsonn}\n\nthis was the second jsonn")
    f.close()
    if len(value["embeds"]) !=0 :
      Press_button(index)
def Press_button(index):
  connection=HTTPSConnection("discordapp.com", 443)
  guild_id=''
  for i in range(len(server_id)-1):
    guild_id += server_id[i]
  channel_id=value["channel_id"]
  message_id = value["id"]
  button_id = value["components"][0]["components"][index]["custom_id"]
  button_hash= value["components"][0]["components"][0]["hash"]

  button_data = {
        "type": 3,
        "guild_id": guild_id,
        "channel_id": channel_id,
        "message_id": message_id,
        "message_flags": 0,
        "application_id": "270904126974590976",
        "data": {"component_type": 2, "custom_id": button_id, "hash": button_hash},
  }
  header_data = {
          "content-type": "application/json",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
          "authorization": "NjI3ODQ2MDQxODMxNDczMTUy.YUoS5A.Mm76eCS1ndrdHzrjGmfqk9Bus_s",
          "host": "discordapp.com",
          "referrer": f"{act_URL}"
          }       
  try:
      connection.request("POST", "/api/v9/interactions", json.dumps(button_data), header_data)
      response = connection.getresponse()
      time.sleep(1)
      if 199 < response.status < 300: #everything is alright
          pass
      else:
          print(f"While pressing button, received HTTP {response.status}: {response.reason}")
  except:
      print("Failed to press button")     
j=0
k=0
l=0
keep_alive()
time.sleep(3)
TIME_NOW = datetime.datetime.now() + datetime.timedelta(hours=1)
f = open("file.txt", "a")
TIME_aftr_12hr = TIME_NOW + datetime.timedelta(hours=12)
print('will us luck at ',TIME_aftr_12hr.strftime("%H:%M:%S") )
print(TIME_NOW.strftime("%H:%M:%S"))
running=True
print('running is now',running)
while running:
    print('------------------------------------------')
    f = open("file.txt", "a")
    f.write("------------------------------------------\n")
    f.close()
    for i in range (12):
      content = 'pls work'
      f=open("file.txt","a")
      f.write("work\n")
      f = open("file.txt", "a")
      print('work')
      communication()
      keeping_alive()
      time.sleep(200)

    content = 'pls daily'
    f = open("file.txt", "a")
    f.write("daily\n")
    f = open("daily.txt", "a")
    f.close()
    print('daily')
    communication()
    keeping_alive()