def add(x,y): 
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def stockXTotalBuyerFees(x,y,z): 
    return x + x * (1-y) + x * 0.03 + 14.95
def stockXTotalSellerFees(x,z):
#z indicates your seller level, 1,2,3,4 or 5
#x is the price of product being sold, has to be greater tha $50
    if(x < 15):
        print("The Minimum Listing Price on StockX is $15")
    if(z == 1):
        return x - x * 0.1 - 4
    if(z == 2):
        return x - x * 0.095 - 4
    if(z == 3):
        return x - x * 0.09 - 4
    if(z == 4):
        return x - x * 0.085 - 4
    if(z == 5):
        return x - x * 0.08 - 4
def percentageCalculator(x,y):
    return x + x * y
def percentOff(x,y):
    return x - x * (1-y)
