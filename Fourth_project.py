import random as rm

def guess_project() :

    # To get the guess :

    def get_guess():
        return list(input("What's your guess ? :"))

    # To generate computer code :

    def generate_code():
        Digits = [str(number) for number in range(10)]
        rm.shuffle(Digits)

        return Digits[:3]

    # To generate the clues :

    def generate_clues(code,user_guess):    
        if user_guess == code :
            return "Code cracked"

        clues = []

        for index,number in enumerate(user_guess):
            if number == code[index]:
                clues.append("match")
            elif number in code :
                clues.append("close")

        if clues == []:
             return ["nope"]
        else:
             return clues

    # To run game logic :

    print("Welcome to this game =)")
    print("Close: You've guessed a correct number but in the wrong position")
    print("Match: You've guessed a correct number in the correct position")
    print("Nope: You haven't guess any of the numbers correctly")

    secret_code = generate_code()
    clue_report = []

    while clue_report != "Code cracked" :

        guess = get_guess()
        clue_report = generate_clues(guess,secret_code)
        print("Let's see your result")

        for clue in clue_report :
            print(clue)