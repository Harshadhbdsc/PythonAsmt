#this program will increase the user's mental skill on general topics.
print ("welcome to the science quiz game")
print ("NOTE: type a b or c for answer")
#initialising variables
score = 0
question_no = 0


print("------------------------------")
print(f' 1. what is the hieght of mount everest?')
print("A. 26000 feet")
print("B. 29000 feet")
print("C. 30000 feet")
ques = input("enter your answer (A/B/C : ").lower()
if ques == 'b':
    score +=1
    print('correct!')
    question_no += 1

else:
    print('incorrect!')
    print(f'correct answer is --> B')
print("--------------------------------")
print("--------------------------------")
print(f' 2. what is the tallest building on Earth?')
print("A. Twin towers")
print("B. Sky tower")
print("C. Burj Khalifa")
ques = input("enter your answer (A/B/C : ").lower()
if ques == 'c':
    score +=1
    print('correct!')
    question_no += 1

else:
    print('incorrect!')
    print(f'correct answer is --> C')
print("--------------------------------")
print("-------------------------")
print(f' 3. Which element got its name from the water it makes when burned?')
print("A. Hydrogen")
print("B. Sodium")
print("C. Tungsten")
ques = input("enter your answer (A/B/C : ").lower()
if ques == 'a':
    score +=1
    print('correct!')
    question_no+=1

else:
    print('incorrect!')
    print(f'correct answer is --> A')
print("--------------------------------")
print("--------------------------------")
print(f' 4.who was the first president in united states ?')
print("A. Joe Biden")
print("B. Donald Trump")
print("C. George Washington")
ques = input("enter your answer (A/B/C : ").lower()
if ques == 'c':
    score +=1
    print('correct!')
    question_no += 1

else:
    print('incorrect!')
    print(f'correct answer is --> C')

total_score = score
print("----------------------------")
print("your total score is : ", total_score)
if total_score<=3:
        print("that was not too bad try harder")
else:
    print ("well done")
print("----------------------------")
