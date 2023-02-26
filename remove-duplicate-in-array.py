# 
#https://in.indeed.com/career-advice/interviewing/coding-interview-questions
#Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Can you find duplicate numbers in an array?

# Define an array of numbers
numbers = [1, 2, 3,2, 4, 5]

# Define an empty array to store the square of each number
squares = []
y=0
pos=0

# Loop through the numbers array and compute the square of each number
for num in numbers:
    #pos+=1
    # if pos>0&&:
    #   y=num
    #   squares.append(y) 
    # else:
    #   print(y)
      if num in squares:
          continue
      else:
          square=num
          squares.append(square)  # Add the square to the squares array
   
         

# Print the squares array
print(squares)  


