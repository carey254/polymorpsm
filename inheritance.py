# Base Class - Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in percentage

    def display_info(self):
        print(f"Smartphone Information:\nBrand: {self.brand}\nModel: {self.model}\nStorage: {self.storage}GB\nBattery: {self.battery}%")

    def make_call(self, number):
        print(f"Calling {number}...")

    def browse_internet(self):
        print(f"Browsing the internet with {self.model}...")

    def charge_phone(self, charge_amount):
        self.battery += charge_amount
        if self.battery > 100:
            self.battery = 100
        print(f"Charging... Battery is now at {self.battery}%")

# Derived Class - SmartPhone with Camera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_quality):
        super().__init__(brand, model, storage, battery)
        self.camera_quality = camera_quality  # in MP (Megapixels)

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} MP camera...")

    def display_info(self):
        super().display_info()
        print(f"Camera Quality: {self.camera_quality} MP")

# Example usage
phone1 = Smartphone("Apple", "iPhone 13", 128, 85)
phone1.display_info()
phone1.make_call("123-456-7890")
phone1.browse_internet()
phone1.charge_phone(15)

print("\n--- Smartphone with Camera ---")
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 256, 75, 108)
phone2.display_info()
phone2.take_photo()
phone2.charge_phone(10)
