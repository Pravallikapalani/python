a=int(input("enter a value"))
if a%3==0 and a%5==0:
    print("great")
elif a%3==0 and a%9==0:
    print("good")
elif a%3==0 and a%7==0:
    print("ok")
else:
    print("not ok")
