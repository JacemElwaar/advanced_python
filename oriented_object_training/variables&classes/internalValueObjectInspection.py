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



#access to the internal variable of the a python file 
# command python -i  <file_name.py>
# represent the atributes that exist on one instance   : me.__dict__ 
# Also an important use of dict is when we want to see the internal variables of a class User.__dict__
# what about functionnality and things that we can actually call on the instance command: dir(me)
# the last one will show us the function that we can call on that instance 
# we can applicate this on the class also dir(User)#
# we can test it also to verify wha
#>>> User.activate 
#<function User.activate at 0x104f099e0>
# 
# isinstance function isinstance(me, User) this will check if me is an instance of User
# 
# help we can also demand the help function that will give us the documentation of the class or the instance
# # 
