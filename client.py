import socket
import time
import json
import pickle
import random

pl = int(input('enter player num'))

while True:
  try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((input('enter host address'),8000))
    msg = pickle.loads(s.recv(1024))

    if msg['command'] == 'e':
      s.sendall(pickle.dumps(msg))
      s.close()
      time.sleep(5)
    elif msg['command'] == 'go':
      print(f"player {msg['msg']} wins !")
      print(f'and youre player {pl}!')
      break
    elif msg['command'] == 'yt' and msg['field'][0]!=pl:
      msg['msg'] = int(input('your turn >>'))
      msg['field'][0]=pl
      s.sendall(pickle.dumps(msg))
      time.sleep(5)
    else:
      s.sendall(pickle.dumps(msg))
      time.sleep(5)
  except:
    print('Seems like you lost that game mate')
    break
