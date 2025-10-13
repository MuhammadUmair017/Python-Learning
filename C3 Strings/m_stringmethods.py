# All About String Methods

# len method (Length)
course = "Python for Beginners"
print(len(course))

# upper 
print(course.upper())

# lower
print(course.lower())

# find ( to find the index of first occurence )
print(course.find('n'))
print(course.find('Beginners'))

# replace ( to replace something )
print(course.replace('Beginners', 'Absolute beginners'))

# title
print(course.title())
# The title() method does not take any parameters. It simply converts the first character of each word to uppercase and the remaining characters to lowercase.

# endswith
print(course.endswith('ers'))

# startswith
print(course.startswith('pyth'))

# important ( boolean expression)

print("Python" in course) # It checks if a following word is in the text or not