import os

print("Current Directory:", os.getcwd())      # Show current working directory

# Create a new folder
os.mkdir("TestFolder")
print("Folder Created!")

# List all files and folders
print("Files and Folders:", os.listdir())

# Rename folder
os.rename("TestFolder", "NewFolder")
print("Folder Renamed!")

# Delete folder
os.rmdir("NewFolder")
print("Folder Deleted!")
