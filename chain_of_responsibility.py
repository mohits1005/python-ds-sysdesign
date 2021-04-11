class BaseHandler(object):
    def __init__(self):
        self.nextHandler = None
    
    def handle(self, request):
        if self.nextHandler:
            self.nextHandler.handle(request)

class FirstHandler(BaseHandler):
    def handle(self, request):
        print("Handling first request",request)
        super(FirstHandler,self).handle(request)

class SecondHanlder(BaseHandler):
    def handle(self, request):
        print("Handling second request",request)
        super(SecondHanlder,self).handle(request)

first = FirstHandler()
second = SecondHanlder()
first.nextHandler = second
first.handle({"a":2})