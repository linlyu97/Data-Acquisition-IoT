#!/usr/bin/python
import sys
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import os
import glob
import time
import dht11
import RPi.GPIO as GPIO
import numpy as np

# for reference data (DS18B20)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = base_dir + '28-05178079b7ff'
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

# change raw temperature to real temperature
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

# for sensor data (DHT11)
# define GPIO 14 as DHT11 data pin
Temp_sensor=14

# get accuracy of temperature
def accuracy():
    # Main program block
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    # Initialise display
    instance = dht11.DHT11(pin = Temp_sensor)
    data = []

    sensorData = np.array([])
    referenceData = np.array([])

    for i in range(10):
        result = instance.read()
        T1 = result.temperature
        T2 = read_temp()
        while T1 == 0 or T2 == 0:
            time.sleep(1)
            result = instance.read()
            T1 = result.temperature
            T2 = read_temp()
        sensorData = np.append(sensorData, result.temperature)
        print("the sensor data is " + str(sensorData))
        referenceData = np.append(referenceData, read_temp())
        print("the reference sensor data is " + str(referenceData))
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(10):
        signOfSensor = 20 <= sensorData[i] <= 24
        signOfRefer = 20 <= referenceData[i] <= 24
        if signOfSensor == True and signOfRefer == True:
            TP += 1
        elif signOfSensor == False and signOfRefer == False:
            TN += 1
        elif signOfSensor == True and signOfRefer == False:
            FP += 1
        else:
            FN += 1

    precision = TP / (TP+FP) * 100
    recall = TP / (TP+TN) * 100

    return precision, recall


class Device(mqtt.Client):
    def __init__(self, username, password):
        super(Device, self).__init__()
        self.host = "mqtt.openchirp.io"
        self.port = 8883
        self.keepalive = 300
        self.username = username
        self.password = password

        # Set access credential
        self.username_pw_set(username, password) #set username and pass
        self.tls_set('cacert.pem')

        # Create a dictionary to save all transducer states
        self.device_state = dict()

        # Connect to the Broker, i.e. the OpenChirp server
        self.connect(self.host, self.port, self.keepalive)
        self.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connection Successful")
        else:
            print("Connection Unsucessful, rc code = {}".format(rc))
        # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
        self.subscribe("openchirp/device/"+self.username+"/#") # Subscribe to all tranducers

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload.decode()))
        # Save device state
        transducer = msg.topic.split("/")[-1]
        self.device_state[transducer] = msg.payload.decode()

    def on_publish(self, client, userdata, result):
        print("Data published")

username1 = '5da3777a466cc60c381e0cab'
password1 = 'yUkXdJccOU15h0D2ptmA4N1o6dpjKI3o'

# Instantiate your own device
precision_of_temperature = Device(username1, password1)
recall_of_temperature = Device(username1, password1)

def main():
    sensor = "precision_of_temperature"
    sensor1 = "recall_of_temperature"

    while True:
        # Read from sensor
        precision_reading = accuracy()[0]
        recall_reading = accuracy()[1]
        print("current sensor precision is " + str(precision_reading))
        print("current sensor recall is " + str(recall_reading))
        precision_of_temperature.publish("openchirp/device/"+username1+"/"+sensor, payload=precision_reading, qos=0, retain=True)
        recall_of_temperature.publish("openchirp/device/"+username1+"/"+sensor1, payload=recall_reading, qos=0, retain=True)
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
    except ZeroDivisionError:
        print('There are something wrong with your DHT-11 sensor')

