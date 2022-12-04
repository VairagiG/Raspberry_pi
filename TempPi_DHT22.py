import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class DHT22:
    def __init__(self):
        self.temperature
        self.humidity
    
    def read_temperature(self):
        self.temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)[1]
        return self.temperature

    def read_humidity(self):
        self.humidity = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)[0]
        return self.humidity

def main():
    # print("Temperature is {0:0.1f}*C ,and Humidity is {1:0.1f}%".format(temp,humid))
    print(f'Temperature is {DHT22.read_temperature}*C ,and Humidity is {DHT22.read_humidity}%')
    # return temp, humid

if __name__ == "__main__":
    main()