import time
import playsound

ip = input('Enter time in the format HH.MM.SS-- ' )
s = ip.split('.')
a,b,c = [s[i] for i in (0,1,2)]
sec = int(a)*3600 + int(b)*60 + int(c)

ring = False
start_time = time.time()
y = sec - int(time.time() - start_time)

while not ring:
  if y != int(sec - int(time.time() - start_time)):
    p,s = divmod(y,60)
    hr,m = divmod(p,60)
    # print(str(hr).zfill(2),':',str(m).zfill(2),':',str(s).zfill(2),end='\r')
    print(f'{hr}:{m}:{s}',end ='\r')
    y = sec - int(time.time() - start_time)

  if sec - int(time.time() - start_time ) == 0:
    ring = True
    print('Music')
    playsound.playsound('F:\songs\guitars.mp3')