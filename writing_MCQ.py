import os

if os.path.exists("MCQ.txt"):
    mode = "a"
else:
    mode = "w"

with open("MCQ.txt", mode) as file:

    file.write("\n"*2)
    file.write("Question : In 1674, he was formally crowned as the chhatrapati (emperor) of his realm at _ _ _ _ _ _ ." + "\n")
    file.write(" "*4+"• aman"+ "\n")
    file.write(" "*4+"• aman"+ "\n")
    file.write(" "*4+"• aman"+ "\n")

