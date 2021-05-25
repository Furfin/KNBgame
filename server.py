import socket
import json
import pickle
#0 - k
#1 - n
#2 - b
data = {'field':[0,0,0],'command':'',"msg":''}
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.1.22',8000))
info = socket.gethostname()
sock.listen(5)
print(f'server is running at {info}')

cons = 1
turn=0
pln=[False,False]
pl = [-1,-1]
while True:
  print(pl,pln,turn)
  clientsocket, address = sock.accept()
  print(f"connection with {address} has been established!")
  data['command'] = 'yt'
  if turn == 2:
    data['command']='go'
  print(data,':sended data',cons)
  clientsocket.sendall(pickle.dumps(data))
  if data['command']=='go':
    break
  data = pickle.loads(clientsocket.recv(1024))
  print(data,':recevied data')
  if not pln[data['field'][0] - 1]:
    pl[data['field'][0] - 1] = data['msg']
    pln[data['field'][0] - 1] = True
    turn+=1
  else:
    continue
  if turn==2:
    print(pl)
    if pl[0]==pl[1]:
      turn=0
      continue
    elif (pl[0]==0 and pl[1]==1) or (pl[0]==1 and pl[1]==2) or (pl[0]==2 and pl[1]==0):
      data['msg'] =  'player 1 wins'
      continue
    else:
      data['msg'] =  'player 2 wins'
      continue
       


  
  