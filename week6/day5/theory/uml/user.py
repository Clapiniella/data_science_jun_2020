class User:
    def __init__(self, userId, password, loginStatus, registerDate):
        self.userId = userId
        self.password = password
        self.loginStatus = loginStatus
        self.registerDate = registerDate
    
    def verifyLogin(self):
        if self.password == "XHG":
            return True
        else: 
            return False
        

class Administrator(User):
    
    def __init__(self, userId, password, loginStatus, registerDate):
        User.__init__(userId, password, loginStatus, registerDate)
        
class Customer(User):
    def __init__(self, eyes):
        User.__init__(userId, password, loginStatus, registerDate)
        self.eyes = eyes

class Order:
    
    def __init__(self, orderID, dateCreated, customer):
        self.orderID = orderID
        self.dateCreated = dateCreated
        self.customer = customer
        
customer = Customer(eyes=2)
order = Order(orderID=2662, 
              dateCreated="06/07/2020", 
              customer=customer)

order.customer.eyes
