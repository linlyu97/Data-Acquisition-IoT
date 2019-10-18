#!/usr/bin/python
import sys
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import dht11
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from datetime import datetime
import pygame

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

# Modify here based on your own device
username = '5da3777a466cc60c381e0cab' # Use Device ID as Username
password = 'yUkXdJccOU15h0D2ptmA4N1o6dpjKI3o' # Use Token as Password

smart_device = Device(username, password)

# Sensor pin out
Temp_sensor = 14
red_led = 18
blue_led = 23
fan2 = 12

summer = False
winter = False
currentMonth = datetime.now().month

if currentMonth < 10 and currentMonth > 3:
    summer = True
else:
    winter = True


# Set up communication between light and raspberrry pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(fan2, GPIO.OUT)
GPIO.output(fan2, 1)


def main():
    # Main program block
    instance = dht11.DHT11(pin = Temp_sensor)

    # Openchirp remote transducer name
    sensorT = "temperature"
    sensorH = "humidity"
    actuatorLedR = "red_led"
    actuatorLedB = "blue_led"
    actuatorFan = "fan"
    smart_device.device_state[actuatorLedR] = 0
    smart_device.device_state[actuatorLedB] = 0
    smart_device.device_state[actuatorFan] = 1

    # Two methods: 'Self Control IOT' OR 'Automatic'
    askforchoice = input("How do you want to test? Self control over IOT or automatic? ")

    while True:
        result = instance.read()

        # Update the sensor reading
        temp = result.temperature
        hum = result.humidity
        count = 0

        # if choose the 'self control IOT method'
        if (askforchoice == 'self control'):

            if(hum > 40):
                pygame.mixer.init()
                pygame.mixer.music.load("SchenleyPark.wav")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                time.sleep(10)

            # OpenChirp output
            GPIO.output(red_led, int(smart_device.device_state[actuatorLedR]))
            GPIO.output(fan2, int(smart_device.device_state[actuatorFan]))
            GPIO.output(blue_led, int(smart_device.device_state[actuatorLedB]))

        # if choose the 'automatic method'
        if (askforchoice == 'automatic'):

            # Due to the sensor output latency, there are values measured to be 0s
            if (temp != 0 and hum != 0):
                # Save the reading to cloud server
                smart_device.publish("openchirp/device/"+username+"/"+sensorT, payload=temp, qos=0, retain=True)
                smart_device.publish("openchirp/device/"+username+"/"+sensorH, payload=hum, qos=0, retain=True)

                if winter:
                    if (temp < 20):
                        GPIO.output(blue_led, GPIO.HIGH)
                        GPIO.output(fan2, 1)
                    elif(temp > 23.5):
                        GPIO.output(red_led, GPIO.HIGH)
                        # fan2 0 is fan on
                        GPIO.output(fan2, 0)
                    else:
                        GPIO.output(blue_led, GPIO.LOW)
                        GPIO.output(red_led, GPIO.LOW)
                        GPIO.output(fan2, 1)

                if summer:
                    if (temp < 23):
                        GPIO.output(blue_led, GPIO.HIGH)
                        GPIO.output(fan2, 1)
                    elif(temp > 26):
                        GPIO.output(red_led, GPIO.HIGH)
                        GPIO.output(fan2, 0)
                    else:
                        GPIO.output(blue_led, GPIO.LOW)
                        GPIO.output(red_led, GPIO.LOW)
                        GPIO.output(fan2, 1)

                # if(hum >= 60):
                #     GPIO.output(blue_led, GPIO.HIGH)
                # else:
                #     GPIO.output(blue_led, GPIO.LOW)

                # print"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%"


if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    GPIO.output(fan2, 1)
    GPIO.output(red_led, GPIO.LOW)
    GPIO.output(blue_led, GPIO.LOW)
    # GPIO.cleanup()
    sys.exit(0)
    pass

