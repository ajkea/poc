# poc

# Proof of concept: cool sleep buddy

## Concept:

Een ventilator (+ eventuele extra’s) die enkel opstaat vanaf een bepaalde temperatuur met een timer. Zo word je ’s nachts niet wakker van een ventilator die nog opstaat en/of werkt de ventilator enkel nog als het te warm is. Hierdoor springt hij dus af als het ’s nachts genoeg is afgekoeld.

### Nodig:

-Raspberry Pi
-Ventilator
-Temperatuur sensor (DHT22 of AM2302)

### Werking:


-Installeren van raspbian
-Installeren van libusb-dev
sudo apt-get install libusb-dev
-dit is een software pakket om nadien hub-ctrl.c te draaien.
git project hub-ctrl.c binnenhalen
git clone https://github.com/codazoda/hub-ctrl.c.git
-Compilen van hub-ctrl.c naar een uitvoerbaar bestand
gcc -o hub-ctrl hub-ctrl.c -lusb
-Juiste USB poort zoeken
dmesg
lsusb

-script maken voor usb te deactiveren en activeren

sudo ~/Documents/hub-ctrl.c/hub-ctrl -b 001 -d 002 -P 2 -p 0
-In dit script maak je gebruik van hub-ctrl (het git project dat je moet binnenhalen). Daarbij gaat hij op bus 1 (-b), device 2 (-d), poort 2 (-P), de power (-p) op 0 gezet.

sleep 10
-Hier wacht hij 10 seconden (testfase).

sudo ~/Documents/hub-ctrl.c/hub-ctrl -b 001 -d 002 -P 2 -p 1
-Hier wordt op bus 1 (-b), device 2 (-d), poort 2 (-P), de power (-p) op 1gezet.

-Scripts uitvoerbare rechten geven anders werken ze niet.
-In terminal in de map van de scripts:
chmod +x usbpoweron.sh
chmod +x usbpoweroff.sh

-Crontab instellen voor start- en einduur van script.
-In terminal:
crontab -e





-Aansluiten temperatuursensor 
-Installeren van Raspbian, een simpel OS voor de raspberry pi

## Problemen
-poorten op een raspberry pi kunnen niet apart gedeactiveerd worden, indien je de poort dus af zet werkt geen enkele USB poort nog.
-mogelijke oplossing:
--script schrijven dat blijft lopen en de usb poorten terug kan activeren (op interval bijvoorbeeld)

-temperatuur en luchtvochtigheid sensor geeft/gaf geen resultaten terug (connectiefout?)

-USB stopt maar start daarna direct terug op. (soms wel soms niet)

## Bronnen:

https://raspberrytips.nl/dht22-temperatuursensor-raspberry-pi/

https://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/

USB controll:
https://github.com/codazoda/hub-ctrl.c

https://github.com/mvp/uhubctl

Crontabs:
https://crontab.guru/

## Logboek:

12/3/18: Aankoop Raspberry Pi 2 model B
20/4/18: Bestellen temperatuur en vochtigheidsensor DHT22 AM2303
14/8/18: Uitdenken idee voor POC
18/8/18: Aansluiten sensor research + aansluiten + script om temperatuur en vochtigheid terug te krijgen.
19/8/18: Research hoe USB poorten uit te schakelen op linux/raspberry pi + toepassen van techniek.
20/8.18: Python script bijwerken om gegevens van temperatuur te gebruiken. 
22/8/18: Cronjobs aanmaken voor dagelijks loopen van het script tussen 22u en 4u.