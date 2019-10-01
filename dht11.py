import RPi.GPIO as GPIO
import time
import dht11

# Main program block
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
# Initialise display
# lcd_init()

Temp_sensor = 14
instance = dht11.DHT11(pin = Temp_sensor)

red_led = 18
blue_led = 23

# Set up communication between light and raspberrry pi
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)


def main():
  while True:
    #get DHT11 sensor value
    result = instance.read()

    #Set sensor threshold value to be 30 degree, subject to change.
    if(result.temperature >= 30):
        GPIO.output(red_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(red_led, GPIO.LOW)
        time.sleep(1)

    if(result.humidity >= 40):
        GPIO.output(red_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(red_led, GPIO.LOW)
        time.sleep(1)

    if(result.temperature != 0):
    # The sampling rate is still 1hz, but due to latency issue, only print out meaning 
    # none zero value
        print"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%"
        time.sleep(1)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)