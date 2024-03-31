class showroom:
    def __init__(self):
        self.cgst=50000
        self.sgst=40000
        self.insurance=100000
    def company(self):
        while True:
            self.c=input("enter companyname" )
            if self.c =="toyota":
                print("welcome to toyota family")
                self.model()
                break
            elif self.c=="mahindra":
                print("welcome to mahindra family")
                self.model()
                break
            elif self.c=="mercedes":
                print("welcome to mercedes family")
                self.model()
                break
            else:
                print("enter valid company")
                
    def model(self):
        # while True:
        if self.c=="toyota":
            while True:
                print("select from fortuner and innova")
                self.m=input("enter the car model")
                if self.c=="fortuner":
                    self.price(self.m)
                    break
                elif self.c=="innova":
                    self.price(self.m)
                    break
                else:
                    print("valid model")
                        
        elif self.c=="mahindra":
            while True:
                print("select from scorpia and thar")
                self.m=input("enter the car model")
                if self.m=="scorpia":
                    self.price(self.m)
                    break
                elif self.c=="thar":
                    self.price(self.m)
                    break
                else:
                    print("valid model")
        elif self.c=="mercedes":
            while True:
                print("select from gvagan and amg")
                self.m=input("enter the car model")
                if self.m=="gvagan":
                    self.price(self.m)
                    break
                elif self.m=="amg":
                    self.price(self.m)
                    break
                else:
                    print("valid model")
                        
         
    def price(self,m):
        if self.m=="innova":
            self.price=100000
        if self.m=="forture":
            self.price=1000000
        if self.m=="scorpia":
            self.price=150000
        if self.m=="thar":
            self.price=180000
        if self.m=="gvagan":
            self.price=100000
        if self.m=="amg":
            self.price=150000
        # else:
        #     print("valid amount")
        self.totalprice=self.price+self.sgst+self.cgst+self.insurance
        print(self.totalprice)
obj=showroom()
obj.company()
