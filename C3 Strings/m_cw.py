# strings practice

course = "Python course for Beginners"
        # 0123456789101112...
print(course[4])
print(course[-4])

# for getting more inputs

print(course[0:5])
  # Python is not fully printed because the last index is exluded i-e 0:5 means index 5 is not included 

print(course[0:]) # From 0 index to the end by default

print(course[1:]) # From 1 index to the end

print(course[:]) # In this case the interpreter will detect the starting as 0 and others value as end

another = course[:]
print(another)

