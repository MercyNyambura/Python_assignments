# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        # Encapsulation: private attribute
        self.__storage = storage
        self.battery = battery

    # Getter (to access private attribute)
    def get_storage(self):
        return self.__storage
    
    # Setter (to safely modify private attribute)
    def upgrade_storage(self, extra_gb):
        self.__storage += extra_gb
        print(f"Storage upgraded! New capacity: {self.__storage} GB")

    # Polymorphism: Overriding method
    def device_info(self):
        return f"Smartphone: {self.brand} {self.model}, Storage: {self.__storage} GB, Battery: {self.battery}mAh"


# Another child class for Polymorphism
class SuperSmartphone(Smartphone):
    def device_info(self):
        return f"Super Smartphone: {self.brand} {self.model} with AI features!"


# Usage
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
phone2 = SuperSmartphone("Apple", "iPhone 15 Pro", 256, 4200)

print(phone1.device_info())       # Calls overridden method
print(phone1.get_storage())       # Accessing private storage
phone1.upgrade_storage(64)        # Modify private storage safely

print(phone2.device_info())       # Polymorphism in action
