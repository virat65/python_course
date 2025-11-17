# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# Then the trav’ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.
# In the dark blue sky you keep,
# And often thro’ my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.
# ’Tis your bright and tiny spark,
# Lights the trav’ller in the dark:
# Tho’ I know not what you are,
# Twinkle, twinkle, little star.""")



# external module use -->
# import pyttsx3
# engine = pyttsx3.init()


# engine.say("hello dosto")
# engine.runAndWait()

""" problem 4 --> Write a python program to print the contents of a directory using the os module.
Search online for the function which does that  """

# import os

# def list_directory_contents(dir_path="."):
#     """
#     Print all entries (files + directories) in dir_path.
#     Default is current directory.
#     """
#     try:
#         entries = os.listdir(dir_path)
#     except FileNotFoundError:
#         print(f"Error: Directory not found: {dir_path}")
#         return
#     except NotADirectoryError:
#         print(f"Error: Not a directory: {dir_path}")
#         return
#     except PermissionError:
#         print(f"Error: Permission denied: {dir_path}")
#         return

#     print(f"Contents of directory '{dir_path}':")
#     for name in entries:
#         print(name)

# if __name__ == "__main__":
#     # Example usage:
#     path = input("Enter directory path (or leave blank for current): ").strip()
#     if path == "":
#         path = "."
#     list_directory_contents(path)

# --> checking their type
# a =6
# print(type(a))
# b=8.8
# print(type(a))
# c = "hello"
# print(type(c))

# typecasting
# num = "20.4"
# print(type(num))
# print(type(b))
# b = float(num)

B = 40//9
print(B)