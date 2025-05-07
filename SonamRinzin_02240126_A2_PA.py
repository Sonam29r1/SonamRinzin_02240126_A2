class Main_menu:
    def menu(self):
        print("Select a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("0. Exit program")
    def __init__(self):
        self.overall_score = {
            'guess_number': 0,
            'rock_paper_scissors': 0,
            'trivia_quiz': 0,
            'pokemon_binder': 0
        }
        
    def menu_run(self):
        while True:
            self.menu()
            player_choice = int(input("Enter the game you want to play: "))

            if player_choice == 1:
                #run guess the number game
                game = Number_guessing()
                self.overall_score['guess_number'] = game.game_execution()
                print("--------------------------------------------------------------")
            elif player_choice == 2:
                #run rpc
                game2 = Rock_paper_scissor()
                self.overall_score['rock_paper_scissors'] = game2.game_execution()
                print("--------------------------------------------------------------")
                
            elif player_choice == 3:
                #run TPG
                print("")
                print("--------------------------------------------------------------")

            elif player_choice == 4:
                #run  PCBM
                print("")
                print("--------------------------------------------------------------")

            elif player_choice == 5:
                #Check scores
                print("")
                print("--------------------------------------------------------------")

            elif player_choice == 0:
                print("Exiting program !!")
                print("--------------------------------------------------------------")

                break
            else:
                print("Invalid choice! please enter a valid choice")
                print("--------------------------------------------------------------")

#creating class for each game
import random
class Number_guessing:
    def __init__(self):
        self.lowest_number = 0
        self.highest_number = 40
    def game_execution(self):
        number_to_be_guessed = random.randint(self.lowest_number,self.highest_number)
        attempt = 0
        valid_numbers = 0
        correct_attempt = 0
        min = 0
        while True:
            try:
                print("I am thinking of a number between 0 and 40. \nCan you guess it?")
                player_guess = int(input("Your guess is : "))
                if player_guess == number_to_be_guessed:
                    attempt += 1
                    valid_numbers += 1
                    correct_attempt += 1
                    print("Correct")
                    break
                elif player_guess < number_to_be_guessed:
                    attempt +=1
                    print("Too low")
                    continue
                elif player_guess > number_to_be_guessed:
                    attempt += 1
                    print("Too high")
                    continue

            except ValueError:
                attempt +=1
                print("Invalid input! \nEnter a valid input!!")
                continue
        score = max(0,attempt-valid_numbers)
        print("Your score is ",score)
        return score

class Rock_paper_scissor:
    def __init__(self):
        self.choices = [1,2,3] #1 for rock, 2 for paper, 3 for scissors
        self.win = 0
        self.attempt = 0
    def game_execution(self):
        while True:
            computer_choice = random.choice(self.choices)
            try:
                player_choice = int(input("Enter: \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n 4 to Quit \nYour choice is: "))
                if player_choice == computer_choice:
                    print("Its a tie")
                    self.attempt += 1

                elif(player_choice == 1 and computer_choice == 3) or \
                    (player_choice == 2 and computer_choice == 1) or \
                    (player_choice == 3 and computer_choice == 2):
                    print("You win!")
                    self.attempt += 1
                    self.win += 1

                elif player_choice == 4:
                    break
                else:
                    print("You lost!")
                    self.attempt +=1
            except ValueError:
                print("Invalid choice!")
                continue
        print(f"You won {self.win} time against computer in {self.attempt} match")
                    
                
           
            

    

if __name__ == "__main__":
    menu = Main_menu()
    menu.menu_run()
