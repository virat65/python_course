class Coder:
    lang = "Python"     # parent class default

    def _init_(self, name):
        self.name = name


class AdvancedCoder(Coder):
    def _init_(self, name, lang=None):
        super()._init_(name)

        if lang:                # user-provided value
            self.lang = lang
        else:                   # use parent class value
            self.lang = super().lang


# --- Test ---
c1 = AdvancedCoder("Raman")              # uses parent value
c2 = AdvancedCoder("Aman", "JavaScript") # user value
c3 = AdvancedCoder("Kiran", "C++")

print(c1.name, c1.lang)   # Raman Python
print(c2.name, c2.lang)   # Aman JavaScript
print(c3.name, c3.lang)   # Kiran C++
