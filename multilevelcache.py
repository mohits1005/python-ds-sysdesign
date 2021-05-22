from abc import ABCMeta, abstractmethod

class CacheLevelFactory(object): pass

class Cache(object): pass

class Storage(object): pass

class StorageStrategy(object): pass

class EvictionStrategy(object): pass

class CachePerformanceData(object): pass


'''
class Polygon:
    __metaclass__ = ABCMeta
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon): pass
R = Triangle()
R.noofsides()
'''