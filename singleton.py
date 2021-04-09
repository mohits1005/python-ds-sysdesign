class Singleton_Genius(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton_Genius.__instance:
            Singleton_Genius.__instance = object.__new__(cls)
        return Singleton_Genius.__instance

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

s1 = Singleton_Genius("Yang", "Zhou")
s2 = Singleton_Genius("Elon", "Musk")
print(s1)
print(s2)
print(s1 == s2)
# True
print(s1.last_name)
# Musk
print(s2.last_name)
# Musk