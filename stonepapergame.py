import random
while True:
    my_action= input('enter your choice(Rock or Paper or Scissor):')
    possible_actions=['Rock','Paper','Scissor']
    computer_action= random.choice(possible_actions)
    print('your choose',my_action,'\ncomputer choose=',computer_action)
    if my_action==computer_action:
        print('Both players choose same chooise',my_action,'so match tie')
    elif my_action == 'Rock':
        if computer_action=='Scissor':
            print('Rock smashes sciccor so you win!')
        else:
            print('paper cover the rock so you loss!')
    elif my_action=='Paper':
        if computer_action=='Rock':
            print(' paper cover the Rock so you win!')
        else:
            print('scissor cut the paper so you loss!')
    elif my_action=='Scissor':
        if computer_action=='Paper':
            print('sciccor cut the paper so you win!')
        else:
            print('rock smashes the scissor so you loss!')        
