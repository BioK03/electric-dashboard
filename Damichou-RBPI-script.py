import os
import urllib

try:
    json_data = urllib.urlopen("http://192.168.20.104/api/xdevices.json?cmd=10").read();
    print json_data;
    os.system("mosquitto_pub -h 192.168.20.99 -t damichou -m '"+json_data+"'");
    ## error
except: 
    print "error"
