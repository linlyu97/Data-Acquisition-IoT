import datetime as dt
import RPi.GPIO as GPIO
import time
import sys
import dht11
import matplotlib
matplotlib.use("Pdf")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# Initialise display
# lcd_init()
Temp_sensor = 14

def animate(i, xs, ys):

    # Draw x and y lists
    tempGraph.clear()
    humidityGraph.clear()
    tempGraph.plot(xs, ts)
    humidityGraph.plot(xs, hs)

    # Format plot
    tempGraph.xticks(rotation=45, ha='right')
    tempGraph.ylabel('Temperature (deg C)')
    tempGraph.title('DHT11 Temperature over Time')
    humidityGraph.xticks(rotation=45, ha='right')
    humidityGraph.ylabel('Humidity (percentage)')


def main():
    # Main program block
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Use BCM GPIO numbers
    instance = dht11.DHT11(pin = Temp_sensor)

    while True:
        result = instance.read()
	fig = plt.figure()
	tempGraph = fig.add_subplot(2,1,1)
	humidityGraph = fig.add_subplot(2,1,2)
	xs = []
	ts = []
	hs = []

        if(result.temperature != 0):

        # The sampling rate is still 1hz, but due to latency issue, only print out meaning
        # none zero value
                        # Add x and y to lists
            xs.append(dt.datetime.now().strftime('%H:%M:%S'))
            if(result.temperature != 0):
                ts.append(result.temperature)
            if(result.humidity != 0):
                hs.append(result.humidity)
            # Limit x and y lists to 20 items
            xs = xs[-20:]
            ts = ts[-20:]
            hs = hs[-20:]

            ani = animation.FuncAnimation(fig, animate, fargs=(xs, ts), interval=1000)
            matplotlib.pyplot.show()
	        print"Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%"
            time.sleep(1)


if __name__ == '__main__':

  try:
    main()
    # Set up plot to call animate() function periodically
  except KeyboardInterrupt:
    plt.savefig("test.png")
    GPIO.cleanup()
    plt.close('all')
    sys.exit(0)
    pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)


