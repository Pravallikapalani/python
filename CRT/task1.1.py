class Car:
  def company(self,name):
    I = ['Toyota','Mercedes' 'Suzuki']
    if name in I:
       print("Welcome to ", name)
  def model(self,name):
    d = {'Toyota': ['Fortuner', 'Innova'],'Mercedes': ['BMW'],'Suzuki':['Swift','Alto']}
    if name in d:
       print(d[name])
  def price(self,name,m):
    print("You have selected ",m)
    prices_list = {'Fortuner':7500000,'Innova': 5000000,'BMW':10000000,'Swift':300000,'Alto':100000}
    if m in prices_list:
       car_price = prices_list[m]
       gst = 0.1*car_price
       insurance = 100000
       final_price = car_price+gst+insurance
       print("Final price:",final_price)
n = input("Enter the car company:")
c =Car()
c.company(n)
c.model(n)
m = input("Enter model of car :")
c.price(n,m)
