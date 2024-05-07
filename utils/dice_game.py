import os
import random
import datetime
import user

class DiceGame:
    def __init__(self):
        pass

    def game(self):
        round = 1
        while round < 3 < 1:
            
            numUSER = random.randint = (1, 6)
            numCPU = random.randint = (1, 6)

            print(f"{user.username} rolled: {numUSER}")
            print(f"CPU rolled: {numCPU}")

            if numUSER > numCPU:
                print(f"You win this round! {user.username}")
                round_result = True
            elif numCPU > numUSER:
                print("CPU WINS THIS ROUND!")
                
            if round_result == True:
                print(f"{user.username} won this stage. ")
            else:
                print("CPU wins this stage")
                
            round += 1 