class EventManager:
    def __init__(self):
        self.observers = []
    def notify(self):
        for observer in self.observers:
            observer.update(self)
    def attach(self, observer):
        self.observers.append(observer)
    def detach(self, observer):
        self.observers.remove(observer)

class FileDialog(EventManager):
    def __init__(self,name):
        self.name = name
        self.data = 0
        EventManager.__init__(self)
    
    def getFileDialog(self):
        return self.data
    
    def setFileDialog(self, data):
        self.data = data
        self.notify()

class FirstView:
    def update(self, publisher):
        print('First', publisher.name, publisher.data)


class SecondView:
    def update(self, publisher):
        print('Second', publisher.name, publisher.data)

dialog1 = FileDialog('FileDialog 1')
dialog2 = FileDialog('FileDialog 2')
view1 = FirstView()
view2 = SecondView()
dialog1.attach(view1)
dialog1.attach(view2)
dialog2.attach(view1)
dialog2.attach(view2)
dialog1.setFileDialog(10)
dialog2.setFileDialog(15)
