from __future__ import print_function
'''
                    general manager
        manager1                        manager2
    developer11  developer12     developer21    developer22
'''
class LeafElement:
    def __init__(self, *args):
        self.pos = args[0] 
    def showDetails(self):
        print("\t", end="")
        print(self.pos)

class CompositeElement:
    def __init__(self, *args):
        self.pos = args[0]
        self.children = []
    def add(self, child):
        self.children.append(child)
    def remove(self, child):
        self.children.remove(child)
    def showDetails(self):
        print(self.pos)
        for i, child in enumerate(self.children):
            print("\t", end="")
            child.showDetails()

topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem21)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()
