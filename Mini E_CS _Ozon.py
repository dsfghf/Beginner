class ozon:

    def hi(self):
        print("Welcome to OZON!\n")

    def __init__(self):
        self.dt = {}

    def n_data(self):
      
        while True:
            
            name = input("Please enter your name: ")
              
            if name.isalpha():
                self.dt["name"] = name
                print(f"Welcome {name}\n")
                break
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
                  self.dt["age"]=age
                  return True
                 
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
                self.dt["email"]=email
                print(f" Hello {self.dt['name']} your acount has been created! \n")
                break
    def register(self):
        if "name" in self.dt and "age" in self.dt:
            print("Your Data already exists!\nTo complete the login Enter your email\n")
            
       

    def check_out(self):
        required=["name","age","email"]
    #    if all(key in self.dt for key in["name","age","email"]):
        for i in required:
            if i not in self.dt:
                
                print("Some data is missing. Please register first.\n")
                return False
            else:
                print("All data found! You are now logged in .\n")
            return True


oz = ozon()
oz.hi()
oz.n_data()
oz.e_data()
oz.em_data()
oz.register()
oz.check_out()