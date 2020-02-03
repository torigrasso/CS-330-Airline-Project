

class Customer:
    #   A Class to Create each customer and store their Name, Type, Username, Password, and
    #   Satisfaction level

    def __init__(self, FirstName, CustomerType, Username, Password, Satisfaction):
        self.Satisfaction = Satisfaction
        self.FirstName = FirstName
        self.CustomerType = CustomerType
        self.Username = Username
        self.Password = Password


    def setCustomerType(self,CustomerType):
        self.CustomerType = CustomerType

    def Type(self):
        return self.CustomerType

    def GetName(self):
        return self.FirstName


    def Verify(self, username, password):
        if username == self.Username and password == self.Password:
            return 1
        return 2

    def getuser(self):
        return self.Username

    def setSatisfaction(self,Satisfaction):
        self.Satisfaction += Satisfaction

    def changeSatisfaction(self,Satisfaction):
        self.Satisfaction = Satisfaction

    def getSatisfaction(self):
        return self.Satisfaction