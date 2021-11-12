import socket, json ,sys , psutil ,time 
while True:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(('localhost', 5000 ))  
  #porcentaje de uso de disco  
  info = {'Info': str(psutil.disk_usage('/'))+"%"} 
  sock.send(str(json.dumps(info)).encode('utf-8'))
  time.sleep(35)
  sock.close()
sys.exit(0)
