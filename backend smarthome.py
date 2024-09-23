class SmartPlug:
    def __init__(self, consumption_rate):
        self.switched_on = False
        self.consumption_rate = consumption_rate if 0 <= consumption_rate <= 150 else 0
    
    def toggle_switch(self):
        self.switched_on = not self.switched_on
    
    def get_switched_on(self):
        return self.switched_on
    
    def get_consumption_rate(self):
        return self.consumption_rate
    
    def set_consumption_rate(self, rate):
        if 0 <= rate <= 150:
            self.consumption_rate = rate
        else:
            print("Invalid consumption rate. Rate must be between 0 and 150.")

    def __str__(self):
        return f"Smart Plug: Switched {'On' if self.switched_on else 'Off'}, Consumption Rate: {self.consumption_rate}"

class CustomDevice:
    def __init__(self, option="Amazon"):
        self.switched_on = False
        self.option = option
    
    def toggle_switch(self):
        self.switched_on = not self.switched_on
    
    def get_switched_on(self):
        return self.switched_on
    
    def get_option(self):
        return self.option
    
    def set_option(self, option):
        if option in ["Amazon", "Apple", "Spotify"]:
            self.option = option
        else:
            print("Invalid option. Option must be 'Amazon', 'Apple', or 'Spotify'.")

    def __str__(self):
        return f"Smart Speaker: {self.option}, Status: {'On' if self.switched_on else 'Off'}"

class SmartSpeaker:
    def __init__(self, streaming_service="Amazon"):
        self.switched_on = False
        self.streaming_service = streaming_service

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    def get_switched_on(self):
        return self.switched_on

    def get_streaming_service(self):
        return self.streaming_service

    def set_streaming_service(self, streaming_service):
        if streaming_service in ["Amazon", "Apple", "Spotify"]:
            self.streaming_service = streaming_service
        else:
            print("Invalid streaming service. Choose from Amazon, Apple, or Spotify.")

    def __str__(self):
        return f"Smart Speaker: Streaming Service - {self.streaming_service}, Status - {'On' if self.switched_on else 'Off'}"

class SmartHome:
    def __init__(self):
        self.devices = []
    
    def get_devices(self):
        return self.devices
    
    def get_device_at(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            print("Index out of range.")
    
    def remove_device_at(self, index):
        if 0 <= index < len(self.devices):
            del self.devices[index]
        else:
            print("Index out of range.")
    
    def add_device(self, device):
        self.devices.append(device)
    
    def toggle_switch(self, index):
        if 0 <= index < len(self.devices):
            self.devices[index].toggle_switch()
        else:
            print("Index out of range.")
    
    def turn_on_all(self):
        for device in self.devices:
            device.switched_on = True
    
    def turn_off_all(self):
        for device in self.devices:
            device.switched_on = False
    
    def __str__(self):
        device_info = "\n".join([str(device) for device in self.devices])
        return f"Smart Home Devices:\n{device_info}"

def test_smart_home():
    home = SmartHome()
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    speaker = SmartSpeaker()
    home.add_device(plug1)
    home.add_device(plug2)
    home.add_device(speaker)
    print(home)
    home.toggle_switch(1)
    print(home)
    home.turn_on_all()
    print(home)
    home.remove_device_at(0)
    print(home)

if __name__ == "__main__":
    test_smart_home()
