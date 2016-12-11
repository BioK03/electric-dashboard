# electric-dashboard

The electric dashboard is an IOT schol project.
We had to use some imposed techologies and to develop interface parts.

# Hardware

The hardware consists of an electric meter with an impulsion counter X-Devices.
This counter has an HTTP interface to request counter numbers.
The final product is also composed of a web interface built with Grafana on an InfluxDB database.
The middlehardware is a Raspberry Pi B+, which requests the HTTP interface of the counter and push the data on the server with a MQTT Topic (driven by Mosquitto).

# Technology choices

The mandatory parts of the project (Database, Customer views, transfer to server) are pretty adapted to the project :
* The database, InfluxDB, is perfect to store data that don't need to be change. For an electric consumption monitoring, that's perfectly that we needed to insert new reports from the electric meter.
* The customer interfaces were made with Grafana. It's a powerful tool to build graphs, derivated functions and monitor data.
* The middle communication, Mosquitto, is the perfect tool to push to a public server data from local network. It's also an efficient tool that don't store data (it transmits directly message from sender to subscribers).

# Implementation

On InfluxDB, we opened an account with a database.
Next, we created an admin user and a dashboard on Grafana.
After the opening of a new Mosquitto topic, we developed a Python program which suscribes to our Mosquitto topic and insert new lines to the database.
Also, we developed a Python script that fetch the HTTP service from the electric counter and publish it in the Mosquitto topic. This script is launched every minute with Cron.
