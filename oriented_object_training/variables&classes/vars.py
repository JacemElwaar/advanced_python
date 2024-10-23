class User: 
    active_users = [] 
    # active is a class variable related to the class itself
    # there is only one active_user all over the class instances

    def __init__(self,  name, email): 
        self.name = name
        self.email = email
        # name is an instance variable  
    
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
        


me =  User("Jacem Elwaar", "test@test.com")  
print(f"Active : {me.is_active()}  activated users : {User.active_users}")
me.activate()
me.activate()
print(f"Active : {me.is_active()}  activated users : {User.active_users}")
me.deactivate()
print(f"Active : {me.is_active()}  activated users : {User.active_users}")
print('-'*50)
print(f"Active user off of 'me' : {me.active_users}, Class level {User.active_users}")
me.active_users = "Just me"
print(f"Active user off of 'me' : {me.active_users}, Class level {User.active_users}")