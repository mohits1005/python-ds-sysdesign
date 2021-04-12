class GoogleTTS:
    def __init__(self, text):
        self.text = text
    def convert(self):
        print("converting text to speech:",self.text)

class GoogleTTSProxy:
    def __init__(self,text):
        self.googletts = GoogleTTS(text)
    def convert(self):
        print("do some logging")
        self.googletts.convert()

g = GoogleTTSProxy("hello my name is")
g.convert()