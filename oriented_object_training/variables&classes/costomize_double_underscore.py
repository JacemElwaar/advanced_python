class User: 
    active_users = [] 
    # active is a class variable related to the class itself
    # there is only one active_user all over the class instances

    def __init__(self,  name, email): 
        self.name = name
        self.email = email
        # name is an instance variable 
        # 
    def __str__(self):
        return f"{self.name} with email {self.email}" 
    
    def __del__(self):
        print(f"{self.name} is deleted")
        self.__class__.deactivate(self)
        return True 
    
    
    def activate(self):
        # add the current instance to the active_users list if it's not already there
        if not self.is_active():
            self.__class__.active_users.append(self)
        

    def deactivate(self):
        # remove the current instance from the active_users list if it's there
        if self.is_active():
            self.__class__.active_users.remove(self)

    def is_active(self):
        return self in self.__class__.active_users 
    
    

    

me = User(name="Jacem Elwaar", email="hello@test.com")


print(f"Name is {me.name} and the email is {me.email}")