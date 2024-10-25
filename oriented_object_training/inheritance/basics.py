class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def greet(self):
        print(f"Hello, my name is {self.name}")
    

class TeleMarketer(Person): 
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone_number = phone
    

    def call(self):
        print(f"Calling {self.phone_number}") 


