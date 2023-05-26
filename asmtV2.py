#this program will increase the user's mental skill on general topics with added feature of dictionary, try and excepte and if functions.
print ("welcome to quiz quesr")
#initialising variables

#mainroutine
name = input("enter your name : ")
playing = input("Do you want ot play ? (yes or no) : ").lower()
while playing not in['yes', 'no']:
    playing = input("invaild input. Do you want to play? (yes or no): ").lower()

if playing == "no":
    print("Thank you. Maybe you can play later.")
    exit()

while True:
    try:
        age = int(input("enter your age : "))
        if age in range(8,19):
            print("you are eligible to play this science quiz")
            break
        else:
            print("you are not eligible to play this science quiz. please try later.")
            exit()
            
    except ValueError:
            print('please enter only integers')



qa = {'is the height of mount everst':'29000 feet','is the tallest building on Earth':'Burj Khalifa','is the strongest metal':'Tungsten','animal is mans best friend':'Dogs'}

options = [['28000 feet','29000 feet','30000 feet'],

           ['twin towers','skytower','Burj Khalifa'],

           ['Tungsten','Titanium','Iron'],

           ['Cats','Dogs','Parrots']]


 
 

def quiz(options, qa):

    score = 0

    opt_num = 0

    for k, v in qa.items():

        print('What', k)

        print('Options:')

        for i, option in enumerate(options[opt_num]):

            print(f'{i + 1}. {option}')

        opt_num += 1

        ans = int(input('Enter the option number for your answer: '))

        if options[opt_num - 1][ans - 1] == v:

            score += 1

            print('Correct! you get one point')

        else:

            print('Incorrect! no points')

        print('Score:', score)

 

    print('Your final score is', score )

 

# Example usage

 


quiz(options, qa)

