'''
You will be creating an interactive chat-bot type program.
Eliza is a therapist program that interacts with the user.
Your program will need to evaluate what the user asks and turn the user's
input into a question that sounds like the therapist really cares.

Your first task is to develop a program with a running loop.
If the user types in "I am feeling great" or enter "Q", the program
will stop running. Your program should print out the last input
(as an output) every time before accepting new input.
Make sure you are accommodating for NO case-sensitivity.
(Q is the same as q)
'''
# string variable for the intro message. read the input, if 'q' or 'Q' than end

print ("Good day. Lets talk?")
message = input("Enter your question or enter 'Q' to quit:")
if message == "q" or message == "Q" :
    print("Good day & remember Eliza is here for you")
else:
       # message2 = input("So what is on your mind today?")
        print("I see that you typed:", message)
        
    

