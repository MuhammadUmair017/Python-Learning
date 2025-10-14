# Display a user-entered name followed by “Good Afternoon”
name = input("Please enter your name: ")
msg = f'Good Afternoon {name}'
print(msg)


# Fill in a letter template with a name and date
# Dear <|Name|>,
# You are selected!
# <|Date|>
fullname = input("Please enter your name: ")
date = input("Please Enter date: ")
letter = f'Dear {fullname} \n You are selected! \n {date}'
print(letter)
# Another way to solve this
letter = "Dear <|Name|>,\n You are selected!\n <|Date|>"
print(letter.replace("<|Name|>","Muhammad Umair").replace("<|Date|>","13 Oct 2025"))


# Detect double spaces in a string 
detector = "Hello my name  is Umair"
print(detector.find("  "))
# if there's double space it will return its index otherwise it will return -1 which means double space don't exist 


# Replace double spaces with single spaces
spaces = "Hello  my  name  is Umair"
print(spaces.replace("  "," "))


# Format a letter using escape sequences
course = "Dear Harry,\n\t This python course is nice.\n Thanks!"
print(course)

