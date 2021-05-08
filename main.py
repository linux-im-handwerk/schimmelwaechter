from machine import Pin, I2C
#from time import sleep
import time, math
from bme280 import BME280
from ssd1306 import SSD1306_I2C
import onewire, ds18x20

def ps(T):
    T = float(T)
    P = 0.61121 * math.exp((18.678 - (T / 234.5)) * (T / (257.14 + T)))
    P = round(P * 1000,1)
    return P
    
def linien():
    print('*'*45)

#setup BME280
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
bme = BME280(i2c = i2c)

#setup Display
WITDH = 128
HEIGHT = 64

i2c_oled = I2C(1, sda = Pin(14), scl = Pin(15), freq = 400000)
oled = SSD1306_I2C(WITDH, HEIGHT, i2c_oled)

#setup DS18B20
ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found a ds18x20 device')

#oled.fill(0)
#oled.text('ds18x20 gefunden',0,0)
#oled.show()

while True:
    
    
    print(bme.values)
    linien()
    #print(bme.values[0])
    bme_temp = bme.values[0]
    bme_temp = bme_temp.replace('C','')
    bme_hum = bme.values[2]
    bme_hum = bme_hum.replace('%','')
    
    print('BME Temperatur: \t\t',bme_temp)
    bme_ps = round(ps(bme_temp))
    bme_ps = str(bme_ps)
    #bme_ps = str(ps((bme_temp)))
    print('BME Ps: \t\t\t',bme_ps)
    bme_Pt = ps(bme_temp)*float(bme_hum)/100
    bme_Pt = str(round(bme_Pt))
    #bme_Pt = str(round(ps(bme_temp)*float(bme_hum)/100,1))
    print('BME Pt: \t\t\t',bme_Pt)
    
    print('BME Luftfeuchtigkeit: \t\t',bme_hum)
    linien()
    
    #Daten an OLED ausgeben
    #oled.fill(0)
    #oled.text('T '+ bme_temp + ' C',0,0)
    #oled.text('H '+ bme_hum + ' %',0,15)
    #oled.text('Ps ' + bme_ps + ' Pa',0,30)
    #oled.text('Pt ' + bme_Pt + ' Pa',0,45)
    #oled.show()
    
    #roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        #print(ds_sensor.read_temp(rom))
        print('DS Temperatur: \t\t\t',round(ds_sensor.read_temp(rom),2))
        ds_temp = round(ds_sensor.read_temp(rom),2)
        ds_temp = str(ds_temp)
        T_DS = ds_sensor.read_temp(rom)
        #print(T_DS)
        print('Ps am Sensor DS: \t\t',ps((T_DS)))
        ds_ps = str(round(ps(T_DS)))
        #DS_Pt = round(ps(T_DS)*float(bme_hum)/100,1)
        #print('Pt am Sensor DS: \t\t',str(DS_Pt))
        rlf_DS = round(float(bme_Pt)/ps(T_DS)*100,2)
        ds_hum = str(rlf_DS)
        print('\t\t\t\t',str(rlf_DS))
        linien()
    
    #Daten an OLED ausgeben
    oled.fill(0)
    oled.text('T '+ bme_temp + '/' + ds_temp,0,0)
    oled.text('H '+ bme_hum + '/' + ds_hum,0,15)
    oled.text('Ps ' + bme_ps + '/' + ds_ps,0,30)
    oled.text('Pt ' + bme_Pt + ' Pa',0,45)
    oled.show()
    
    time.sleep(3)

