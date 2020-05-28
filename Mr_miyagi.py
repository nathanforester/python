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
# import sys
#
# mr_miyagi_question = ''
# mr_miyagi_question = input()
#
# while True:
#      while mr_miyagi_question != "Sensei, I am at peace":
#          if mr_miyagi_question.lower().find("sensei") != 0:
#              print("You are smart, but not wise - address me as Sensei please")
#              mr_miyagi_question = input()
#          elif mr_miyagi_question.find("block") >= 0 or mr_miyagi_question.find("blocking") >=0:
#              print("Remember, best block not to be there...")
#              mr_miyagi_question = input()
#          elif mr_miyagi_question.lower().find("sensei") == 0 and mr_miyagi_question.endswith("?"):
#              print("questions are wise, but for now. Wax on, and Wax off!")
#              mr_miyagi_question = input()
#          else:
#              print('do not lose focus. Wax on. Wax off.')
#              mr_miyagi_question = input()
#
#      print('Sometimes, what heart know, head forget')
#      sys.exit(-1)

while True:

    def exit_miyagi(mr_miyagi_question):
        while mr_miyagi_question == "Sensei, I am at peace":
            response = "Sometimes, what heart know, head forget"
            return response

    def functional_miyagi(mr_miyagi_question):
        while mr_miyagi_question != "Sensei, I am at peace":
            if mr_miyagi_question.lower().find("sensei") != 0:
                response_1 = input("You are smart, but not wise - address me as Sensei please")
                return response_1
            elif mr_miyagi_question.find("block") >= 0 or mr_miyagi_question.find("blocking") >= 0:
                response_2 = input("Remember, best block not to be there...")
                return response_2
            elif mr_miyagi_question.lower().find("sensei") == 0 and mr_miyagi_question.endswith("?"):
                response_3 = input("questions are wise, but for now. Wax on, and Wax off!")
                return response_3
            else:
                response_4 = input('do not lose focus. Wax on. Wax off')
                return response_4
        exit(exit_miyagi(mr_miyagi_question))


    mr_miyagi_question = input()
    functional_miyagi(mr_miyagi_question)


 #     response_5 = input("Sometimes, what heart know, head forget")
        #     return response_5
        #                                      exit("Sometimes, what heart know, head forget") # # previous end of main def











