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
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler

SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
mq2_dpin = 26
mq2_apin = 0
buzzer = 20
fan1 = 21

#port init
def init():
    GPIO.setwarnings(False)
    GPIO.cleanup()      #clean up at the end of your script
    GPIO.setmode(GPIO.BCM)    #to specify whilch pin numbering system
    # set up the SPI interface pins
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    GPIO.setup(mq2_dpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
     #Setup Buzzer
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.output(buzzer, 1)
    # Setup the fan
    GPIO.setup(fan1, GPIO.OUT)


#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
#main ioop
def main():
         init()
         print("please wait...")
         time.sleep(15)
         while True:
                  COlevel=readadc(mq2_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
                  sensorS = "level_of_combustible_gas"
                  gas_level = round(((COlevel/1024.)*3.3), 2)
                  smart_device.publish("openchirp/device/"+username+"/"+sensorS, payload=gas_level, qos=0, retain=True)
                  if GPIO.input(mq2_dpin):
                    print("Gas not leak")
                    # Set fan and buzzer to be off when gas is not leak
                    GPIO.output(fan1, 1)
                    GPIO.output(buzzer, 1)
                    #print"Current Gas AD vaule = " +str("%.2f"%((COlevel/1024.)*3.3))+" V"
                    time.sleep(0.5)
                  else:
                    print("Gas leakage")
                    # Turn on the fan and buzzer
                    GPIO.output(buzzer, 0)
                    GPIO.output(fan1, 0)
                    print("Current Gas AD vaule = " +str("%.2f"%((COlevel/1024.)*3.3))+" V")
                    time.sleep(0.5)

if __name__ =='__main__':
         try:
            main()
         except KeyboardInterrupt:
            GPIO.output(fan1, 1)
            GPIO.output(buzzer, 1)
            # GPIO.cleanup()
            sys.exit(0)
            pass

