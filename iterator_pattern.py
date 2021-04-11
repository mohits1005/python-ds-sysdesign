class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def next(self):
    x = self.a
    if x >= 6:
        raise StopIteration
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))