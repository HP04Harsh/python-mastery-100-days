# def Outer():
#     x = 10
#     def inner():
#        return print(x)
#     inner()


# f = Outer()
# f    

def bankbalance(balance):
    def check_balance():
        print("Account Balance: ",balance)
    return check_balance()

f = bankbalance(500)
f        
