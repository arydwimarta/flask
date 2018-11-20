
import datetime


dt = datetime.datetime.now()
d = time.strptime(dt, '%d %B, %Y')
print (d)