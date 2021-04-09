class Product():
    def __init__(self):
        self.a = None
        self.b = None

class Builder(object):
    def __init__(self):
        self.product = Product()
    
    def build_somea(self):
        self.product.a = 25
        return self
    
    def build_someb(self):
        self.product.b = 40
        return self
    
    def getResult(self):
        return self.product

class Client:
    @staticmethod
    def construct():
        return Builder()\
            .build_somea()\
            .build_someb()\
            .getResult()
client = Client.construct()
print(client.a, client.b)