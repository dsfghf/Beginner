class ozon:

    def hi(self):
        print("Welcome to OZON!\n")

    def __init__(self):
        self.users=[{"name":"Basma","age":23,"email":"basma@gmail.com"},
                    {"name":"Nasma","age":21,"email":"nasma@gmail.com"},
                    {"name":"Hamsa","age":19,"email":"hamsa@gmail.com"}
        ]
        self.current_user=None

    def n_data(self):
      
        while True:
            
            name = input("Please enter your name: ")
              
            if name.isalpha():
               return name
            else:
                print("your name must contain letteres only , Try again Please !\n")
    def e_data(self):
        while True:
           try:  
              age=int(input("Enter your age: \n"))
              
              if age <18 :
                  print(f"You are too young to register on the site ! Try again\n")
                  
                  continue
              else:
                  return age
                 
           except ValueError:
               print("Please Enter a valid number for age! \n")
    def em_data(self):
        while True:
            email=input("Enter your email: ").strip()
            if email=="":
                print("Email cannot be empty! Try again.\n")
                continue
            if '@' not in email or 'gmail.com'not in email:
                print("Invalid email format! Try again.\n")
                continue
            else:
                return email
    
               
    def register(self):
       print("\n ---- Register New Acount -----")
            
       name=self.n_data()
       age=self.e_data()
       email=self.em_data()
       for user in self.users:
           if user["email"]==email:
              print("Email already exists! Please login instead .\n")
              return False
         
               
       user={"name":name,"age":age,"email":email}
       self.users.append(user)
       self.current_user=user
       print(f"Hello {name} ,your account has been created! \n")
       return True
       
    def login(self):
        print("-----Login----- ")
        email=input("Enter your email: ").strip()
        for user in self.users:
            if user["email"]==email:
                self.current_user=user
                print(f" Welcome back {user['name']} !\n")
                return True
           
        print("Email not found .Please register first.\n")
        return False

    def check_out(self):
        required=["name","age","email"]
    #    if all(key in self.dt for key in["name","age","email"]):
        if self.current_user is None:
            print("No user logged in !\n")
            return False
        for k in required:
            if k not in self.current_user:
                
                print("Some data is missing. Please complete registration .\n")
                return False
           
        print("All data found! You are now logged in .\n")
        return True


# oz=ozon()
# oz.hi()

while True:
    choice=int(input ("Do you want to (1)Register or (2) Login ? Enter 1 or 2: "))
    if choice==1:
        # if oz.register():
           break
    elif choice==2:
        # if oz.login():
           break
    else:
        print("Invalid choice! Please enter 1 or 2 .\n")   
        
        
# oz.check_out()


class sales():
    def __init__(self):
      self.catalog=[{1:["shirt","Blouse","jacker","hoodie"]},
                  {2:["Laptop","Tablet","Smartphone","Smartwatch"]},
                  {3:["Meat","Chicken","Fish","Rice","Bread","Pasta"]}]
      current_product=None
        
    def search(self):
        print(f"This is our catalog{self.catalog}")
        choice=input("Enter the list number you want to search within :: ")
        for k,v in self.catalog:
          if choice==k:
              return self.catalog[v]
          
        
        
    def clothes(self):
        
        pass
    def technic(self):
        pass
    def food(self):
         pass