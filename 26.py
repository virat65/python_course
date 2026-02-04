# # Parent class
# class Coder:
#     def __init__(self):
#         self.language = "Python"  # default language in parent

# # Child class
# class ChildCoder(Coder):
#     def introduce(self, name, language=None):
#         # If language is provided, use it; otherwise use parent's language
#         lang_to_use = language if language else self.language
#         print(f"Hello, my name is {name} and I code in {lang_to_use}.")

# # Example usage
# child = ChildCoder()

# # Using parent's language
# child.introduce("Ramanand")
# # Output: Hello, my name is Ramanand and I code in Python.

# # Overriding parent's language
# child.introduce("Ramanand", "JavaScript")
# # Output: Hello, my name is Ramanand and I code in JavaScript.






# --->
# 2nd another
# Parent class
# class Coder:
#     language = "Python"  # parent variable

# # Child class
# class ChildCoder(Coder):
#     def introduce(self, name, language=None):
#         print(f"Hello, my name is {name} and I code in {language or self.language}.")

# # Example usage
# child = ChildCoder()

# child.introduce("Ramanand")           # Uses parent's language
# child.introduce("Ramanand", "Java")  # Overrides with new language



# ---->
# # 3rd
# class Coder:
#     def __init__(self, language="Python"):
#         self.language = language   # parent variable


# class ChildCoder(Coder):
#     def introduce(self, name):
#         print(f"My name is {name} and I code in {self.language}.")


# # Usage
# c1 = ChildCoder()              # Uses Python
# c1.introduce("Ramanand")

# c2 = ChildCoder("JavaScript")  # Override parent without passing in introduce()
# c2.introduce("Ramanand")



# # 4th


class Coder:
    # Parent constructor with default values
    def __init__(self, language="Python", experience=1):
        self.language = language
        self.experience = experience


class ChildCoder(Coder):
    # Child inherits everything from parent
    def introduce(self, name):
        print(f"My name is {name}.")
        print(f"I code in {self.language}.")
        print(f"I have {self.experience} years of experience.")


# ---------- USING THE CLASSES ----------

# 1. Using parent default values
coder1 = ChildCoder()
# coder1.introduce("Ramanand")

print()  # just a space

# 2. Passing values while creating object to override parent defaults
coder2 = ChildCoder(language="JavaScript", experience=3)
coder2.introduce("Ramanand")
