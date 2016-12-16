
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import paho.mqtt.client as mqtt
import json

def main(value1, value2, value3):
    USER = 'root'
    PASSWORD = 'root'
    DBNAME = 'db_damichou'
    DB_USER = 'damichou'
    DB_PASSWORD = 'damichou'
    host='192.168.20.99'
    port=8086
 
    now = datetime.datetime.today()
    series = []
 
    pointValues = {
            "time": now.strftime ("%Y-%m-%d %H:%M:%S"),
            "measurement": "capteur1",
            "fields":  {
                "value": value1,
            },
        }
    series.append(pointValues)
    pointValues = {
            "time": now.strftime ("%Y-%m-%d %H:%M:%S"),
            "measurement": "capteur2",
            "fields":  {
                "value": value2,
            },
        }
    series.append(pointValues) 

    pointValues = {
            "time": now.strftime ("%Y-%m-%d %H:%M:%S"),
            "measurement": "general",
            "fields":  {
                "value": value3,
            },
        }
    series.append(pointValues)

    
    client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
    client.switch_user(DB_USER, DB_PASSWORD)
    client.write_points(series)

def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("damichou")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    json_data = json.loads(msg.payload)
    main(json_data["INDEX_C1"], json_data["INDEX_C2"], json_data["INDEX_C2"])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.20.99", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a manual interface.
client.loop_forever()
