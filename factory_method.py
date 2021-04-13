class FrenchLocalizer:
    def localize(self, message):
        print("message localized in french")

class SpanishLocalizer:
    def localize(self, message):
        print("message localized in spanish")

class EnglishLocalizer:
    def localize(self, message):
        print("message localized in english")

def LocalizerFactory(language):
    locaizers = {
        "French": FrenchLocalizer,
        "Spanish":SpanishLocalizer,
        "English":EnglishLocalizer
    }
    return locaizers[language]()

f = LocalizerFactory("French")
s = LocalizerFactory("Spanish")
e = LocalizerFactory("English")
f.localize("me")
s.localize("me")
e.localize("me")