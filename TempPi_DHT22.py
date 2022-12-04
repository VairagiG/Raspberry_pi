import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity , temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
    print("Temperature = {0:0.1f}*C and Humidity = {1:0.1f}%".format(temperature,humidity))
else:
    print("Failed to retrive data from humidity sensor")