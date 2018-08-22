# Raspberry Pi Tips & Tricks - https://raspberrytips.nl

import Adafruit_DHT
import subprocess

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

humidity = round(humidity, 2)
temperature = round(temperature, 2)

if humidity is not None and temperature is not None:

    print 'Temperatuur: {0:0.1f}*C'.format(temperature)
    print 'Luchtvochtigheid: {0:0.1f}%'.format(humidity)
  
    if temperature > 28:
        print 'draaien met die ventilator'
        subprocess.Popen(["bash", "/home/pi/Desktop/usbpoweron.sh"])
                    
    else:
                  
        subprocess.Popen(["bash", "/home/pi/Desktop/usbpoweroff.sh"])
                      
else:

  print 'Geen data ontvangen'

