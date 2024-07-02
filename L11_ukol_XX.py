class ElectricalDevice:
    def turn_on(self):
        print("Device turned on")

    def turn_off(self):
        print("Device turned off")

class WaterResistantDevice:
    def waterproof(self):
        print("The device is waterproof")

class SmartWatch(ElectricalDevice, WaterResistantDevice):
    def display_time(self):
        print("The current time is: 12:00")


watch = SmartWatch()
watch.turn_on()
watch.turn_off()
watch.waterproof()
watch.display_time()

r3 = minus(100, 30)
print(r3)