# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')

#  EXTRA:
#  make it run continuously
#  consider best practices of functions - make this functional
import sys

Mr_miyagi_question = ''
Mr_miyagi_question = input()

while True:
    while Mr_miyagi_question != "Sensei, I am at peace":
        if Mr_miyagi_question.lower().find("sensei") != 0:
            print("You are smart, but not wise - address me as Sensei please")
            Mr_miyagi_question = input()
        elif Mr_miyagi_question.find("block") >= 0 or Mr_miyagi_question.find("blocking") >=0:
            print("Remember, best block not to be there...")
            Mr_miyagi_question = input()
        elif Mr_miyagi_question.lower().find("sensei") == 0 and Mr_miyagi_question.endswith("?"):
            print("questions are wise, but for now. Wax on, and Wax off!")
            Mr_miyagi_question = input()
        else:
            print('do not lose focus. Wax on. Wax off.')
            Mr_miyagi_question = input()

    print('Sometimes, what heart know, head forget')
    sys.exit(-1)

