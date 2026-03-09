import network
import time
import urequests
import json
import gc
import machine
import onewire
import ds18x20
import time
import random

SSID = "Mauro Montoya"
PASSWORD = "04021999"

URL = "https://sd-iotcoldchain-476012992267.us-central1.run.app"

# ----------------------
# WIFI
# ----------------------

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Conectando WiFi...")
    time.sleep(1)

print("WiFi conectado")


# ----------------------
# Sincronizacion hora
# ----------------------
import ntptime
ntptime.settime()
print("Hora sincronizada")

def get_timestamp():
    t = time.gmtime()
    return "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z".format(
        t[0], t[1], t[2], t[3], t[4], t[5]
    )

# ----------------------
# SENSOR DS18B20
# ----------------------

dat = machine.Pin(4)
ow = onewire.OneWire(dat)
ds = ds18x20.DS18X20(ow)

roms = ds.scan()

if not roms:
    print("No se detecto sensor DS18B20")
else:
    print("Sensor detectado")

# ----------------------
# LOOP PRINCIPAL
# ----------------------

while True:

    ds.convert_temp()
    time.sleep(1)

    temp = ds.read_temp(roms[0])

    payload = {
        "device_id": "sensor_01",
        "temperature": temp,
        "timestamp": get_timestamp(),
        "location": "warehouse_lima",
        "battery_level": random.randint(60, 100)
    }

    #print(temp)

    try:

        gc.collect()

        r = urequests.post(URL, json=payload)

        print("Enviado:", json.dumps(payload))
        print("Respuesta:", r.text)

        r.close()

    except Exception as e:
        print("Error:", e)

    time.sleep(20)


