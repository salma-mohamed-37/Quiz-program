import os

file = os.path.join(os.path.dirname(__file__), 'questions.txt')
ins = os.path.join(os.path.dirname(__file__), 'instructions.txt')
students = os.path.join(os.path.dirname(__file__), 'points.txt')

Model_answer = open(file,  "r")
instructions = open(ins , "r")
sheetOfStudents = open(students,"a")

if(not(Model_answer.readable()) or not(instructions.readable()) ):
    os._exit()


print("The instructions:-")
print(''.join(instructions.readlines()))
name = input("Enter your name: ")
numberOfQuestions=int(Model_answer.readline())
points =0
for i in range(numberOfQuestions):
    question = Model_answer.readline()
    rightAnswer =Model_answer.readline().replace("\n",'')
    print(question, end='')
    answer= str(input())
    if(answer == rightAnswer):
        points +=1
print("Your points are " , points , " out of ",numberOfQuestions)      

sheetOfStudents.write(name+" "+str(points)+ "\n")
Model_answer.close()
