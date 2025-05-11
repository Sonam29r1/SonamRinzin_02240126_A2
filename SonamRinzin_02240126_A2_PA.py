from SonamRinzin_02240126_A2_PB import Pokemon_Binder_Manager #imports part b pokemon binder manager
import random #for guess the number game and rock paper scissors

class Main_menu:
    def __init__(self):
        self.scoring = overall_scoring_system() #instantiating overall_scoring_system class in Main_menu

    def menu(self): #list of fucntions to be displayed
        print("★ ", "━"*40 ,"★")
        print("Select a function (0-5):")
        print("★ ", "━"*40 ,"★")
        print("1. Guess Number game")
        print("2. Rock paper scissors game (✌️  ✊ ✋)")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("0. Exit program")
    
        
    def menu_run(self):
        while True:
            self.menu() #displays the list of function(in a infinite loop)
            print("★ ", "━"*40 ,"★")
            player_choice = str(input("Enter the game you want to play: ")) #allows user to select a function
            
            if player_choice == "1":
                #run guess the number game 
                game = Number_guessing() #Number_guessing class is called and it is assigned to variable game
                score = game.game_execution() #from Number_guessing class, function game-execution is called and it is assigned to variable score
                self.scoring.score_updater('guess_number', score) #from overall_scoring_system class, score_updator function is called and score from the game is updated
            elif player_choice == "2":
                #run rock paper scissor game
                game2 = Rock_paper_scissor() #Rock_paper_scissor class is called and it is assigned to variable game2
                score = game2.game_execution() #from Rock_paper_scissor class, function game-execution is called and it is assigned to variable score
                self.scoring.score_updater('rock_paper_scissors', score) ##from overall_scoring_system class, score_updator function is called and score from the game is updated
                print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★")
                
            elif player_choice == "3":
                #run Trivia quiz game
                game3 = Trivia_quiz_game() #Trivia_quiz_game class is called and it is assigned to variable game
                score = game3.quiz_execution() #from Trivia_quiz_game class, function quiz-execution is called and it is assigned to variable score
                self.scoring.score_updater('trivia_quiz', score) #from overall_scoring_system class, score_updator function is called and score from the game is updated
                print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★")

            elif player_choice == "4":
                #run  Pokemon card binder manager
                game4 = Pokemon_Binder() #Pokemon_Binder class is called and it is assigned to variable game
                game4.menu_run() #from Pokemon_Binder class, function menu_run is called and list of functions is displayed
                self.scoring.score_updater('pokemon_binder', game4.manager) #from overall_scoring_system class, score_updator function is called and score from the game is updated
                print("★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★")

            elif player_choice == "5":
                #Check scores
                self.scoring.score_displayer() #from overall_scoring_system , score_displayer function is called and score is displayed
                print("★ ", "━"*40 ,"★")

            elif player_choice == "0":
                print("Exiting program !!")
                print("★ ", "━"*40 ,"★")

                break #exits the loop
            else: 
                print("Invalid choice! please enter a valid choice")
                print("★ ", "━"*40 ,"★")

#creating class for each game
class Number_guessing:
    def __init__(self):
        self.lowest_number = 0
        self.highest_number = 9
    def game_execution(self):
        number_to_be_guessed = random.randint(self.lowest_number,self.highest_number) #A random number between 0 and 9 is selected
        attempt = 0
        valid_numbers = 15
        correct_attempt = 0
        min = 0
        while True:
            try: # used try to handle value error
                print("I am thinking of a number between 0 and 15.\nCan you guess it?")
                print("★ ", "━"*40 ,"★")
                player_guess = int(input("Your guess is : "))
                print("★ ", "━"*40 ,"★")

                '''
                Checks if the player's guess is correct or wrong. If correct congrats user and exit the loop.
                If wrong notify if the guess the higher or lower than target number
                keeps track of valid attempst,correct attempts and avoids counting invalid attempts
                '''
                if player_guess == number_to_be_guessed:
                    attempt += 1
                    correct_attempt += 1
                    print("Wow! Your a prophet!")
                    print("★ ", "━"*40 ,"★")
                    break
                elif player_guess < number_to_be_guessed:
                    attempt +=1
                    print(f"Too bad {player_guess} is lower. Can you try higher")
                    print("★ ", "━"*40 ,"★")
                    continue
                elif player_guess > number_to_be_guessed:
                    attempt += 1
                    print(f"Too bad {player_guess} is way higher. Can your try lower")
                    print("★ ", "━"*20 ,"★")
                    continue

            except ValueError:
                print("Invalid Guess! \nEnter a valid input!!")
                continue
        score = max(0,valid_numbers-attempt)
        print("Your score is ",score)
        return score

class Rock_paper_scissor:
    def __init__(self):
        self.choices = ["Rock","Paper","Scissor"] #creates a list of choice
        self.win = 0
        self.attempt = 0
    def game_execution(self):
        while True:
            computer_choice = random.choice(self.choices) #A random number from choices[1,2,3] is selected
            try:
                '''
                Used try and except for handling Value Error
                used logical operator to determining the winner and loser.
                Tracks attempt and wins
                '''
                print("★ ", "━"*40 ,"★")
                player_choice = int(input("Enter Your Choice: \n Type 1 for Rock \n Type 2 for Paper \n Type 3 for Scissors \n Type 4 to Quit \nYour choice is: "))
                if (player_choice ==1 and  computer_choice == "Rock") or \
                   (player_choice == 2 and computer_choice == "Paper") or\
                   (player_choice == 3 and computer_choice == "Scissor"): # same choice leads to tie
                   print(f"Computer has chosen {computer_choice}! \nIts a tie")
                   self.attempt += 1

                elif(player_choice == 1 and computer_choice == "Scissor") or \
                    (player_choice == 2 and computer_choice == "Rock") or \
                    (player_choice == 3 and computer_choice == "Paper"): #This are all winning condotions for player
                    print(f"You win! Computer has chosen {computer_choice}")
                    self.attempt += 1
                    self.win += 1

                elif player_choice == 4: #allows user to quit
                    print("Thanks for playing")
                    break
                else:
                    print(f"You lost! Computer has chosen {computer_choice}")
                    self.attempt +=1
            except ValueError: #handles Value Error
                print("Invalid choice!")
                continue
        print(f"You won {self.win} time against computer in {self.attempt} match") #Displays the score(number of wins against computer)
        print("★ ", "━"*20 ,"★")
        return self.win
                    
class Trivia_quiz_game:
    def __init__(self):
        self.score = 0
        '''
        Creates a nested dict which includes category{question,option and answer}
        '''
        self.questions = {
            'Kings of Bhutan' : [
                {
                    'question': "Who is the current reigning king of Bhutan (as of 2025)?",
                    'options': ['A. Jigme Singye Wangchuck', 'B. Jigme Khesar Namgyel Wangchuck', 'C. Jigme Dorji Wangchuck', 'D. Ugyen Wangchuck'],
                    'answer': 'B'
                },
                {
                    'question': "Which Bhutanese king introduced democracy to Bhutan before abdicating?",
                    'options': ['A. Jigme Dorji Wangchuck', 'B. Jigme Singye Wangchuck', 'C. Ugyen Wangchuck', 'D.  Jigme Khesar Namgyel Wangchuck'],
                    'answer': 'B'
                },
                {
                    'question': "Which king is known as the 'Father of Modern Bhutan'?",
                    'options': ['A. Jigme Dorji Wangchuck', 'B.  Jigme Singye Wangchuck', 'C. Ugyen Wangchuck', 'D. Jigme Khesar Namgyel Wangchuck'],
                    'answer': 'A'
                },
                {
                    'question': "What major policy did King Jigme Singye Wangchuck introduce in the 1970s?",
                    'options': ['A. Free education for all', 'B. Gross National Happiness (GNH)', 'C. Bhutan’s first constitution', 'D. Abolishment of monarchy'],
                    'answer': 'B'
                }],
            'Bhutanese Culture & Traditions' : [
                {
                    'question' : "What is the national sport of Bhutan?",
                    'options' : ['A.Archery ', 'B.Football ', 'C.Cricket ','D.Khuru(Dart)'],
                    'answer' : 'A'
                },
                {
                    'question' : "Which famous Bhutanese festival features masked dances and religious performances?",
                    'options' : ['A.Diwali ', 'B.Losar ', 'C.Rimdro ','D.Tsechu'],
                    'answer' : 'D'
                },
                {
                    'question' : "Which UNESCO World Heritage Site in Bhutan is known as the 'Tiger’s Nest'?",
                    'options' : ['A.Punakha Dzong ', 'B.Trongsa Dzong ', 'C.Paro Taktsang ','D.Tak Chim'],
                    'answer' : 'A'
                }
            ]
        }
    def quiz_execution(self):
        print("Welcome to Trivia Pursuit Game!")
        print("Select a category:")
        print("-"*44)

        categories = list(self.questions.keys()) #A list is created from above dict using its keys(category) 
        for i in range(0,len(categories)): #Prints all the keys(categories) in the dict which is stored as list
            print(f"{i+1}. {categories[i]}")
            print("-"*44)
            
        try:
            category_choice = int(input("Enter category number: ")) - 1 #lets the user select a category(-1 because index starts from 0 and category choice starts from 1)
            selected_category = categories[category_choice]
        except (ValueError, IndexError): #handle error
            print("Invalid category selection.")
            print("★ ", "━"*20 ,"★")
            return 
            
        for question in self.questions[selected_category]: # this let us access every question for our selected category
            print(question['question'])
            print("★ ", "━"*20 ,"★")
            for option in question['options']: #prints the option of corresponding question listed in the dict
                print(option)
            print("★ ", "━"*20 ,"★")
                
            user_answer = input("Your answer (A/B/C/D): ").upper() #lets user enter a choice and make it case insensitive
            if user_answer == question['answer']: # uses conditional operation to check if user's answer matches the answer in the dict
                print("Correct!")
                print("★ ", "━"*20 ,"★")
                self.score += 1 #if correct answer adds +1 to score
            else:
                print(f"Wrong! The correct answer is {question['answer']}")
                print("★ ", "━"*20 ,"★")
                
        print(f"\nYour score: {self.score}/{len(self.questions[selected_category])}")
        return self.score #returns score value to be used in overall score
    

class Pokemon_Binder:
    def __init__(self):
        self.manager = Pokemon_Binder_Manager() #initializes the manager attribute as an instance of Pokemon_Binder_Manager() class
    def menu(self): #game menu to be displayed
        print("Welcome to Pokemon Card Binder Manager")
        print("★ ", "━"*20 ,"★")
        print("Game Menu:")
        print("1. Add Pokemon Card")
        print("2. Reset Binder")
        print("3. View Current placements")
        print("4. Exit")
    
    def menu_run(self):
        while True:
            self.menu() #displays the game menu
            try:
                player_choice = int(input("Enter your choice:")) #lets user select a function
                if player_choice == 1 :
                    try:
                        user_choice = int(input("Enter Pokedex Number (1-1025): ")) #Lets user enter pokedex number
                        self.manager.add_card(user_choice) #from part b, uses add_card function of pokemon_binder_manager class and a card is added as the user_choice input is passed down as a parameter for add_card function
                        ("★ ", "━"*20 ,"★")
                    except ValueError: #handles ValueError 
                        print("Invalid Input! Please enter a number.")
                        ("★ ", "━"*20 ,"★")
                elif player_choice == 2:
                    self.manager.reset_binder() #uses reset_binder function from pokemon_binder_manager class in part b.
                    ("★ ", "━"*20 ,"★")
                elif player_choice == 3:
                    self.manager.display_binder() #uses display_binder function from pokemon_binder_manager class in part b
                    ("★ ", "━"*20 ,"★")
                    
                elif player_choice == 4:
                    print("Exiting")
                    break #lets player exit by breaking the loop
                else:
                    print("Invalid")
            except ValueError:
                print("Invalid Choice!")
class overall_scoring_system:
    def __init__(self):
        self.overall_score = {
            'guess_number': 0,
            'rock_paper_scissors': 0,
            'trivia_quiz': 0,
            'pokemon_binder': 0
        }
    def score_updater(self, game_name,score): #This checks if the game exists as key in the dictionary 
        if game_name in self.overall_score:   #and updates the corresponding score value of the game
            self.overall_score[game_name] = score
    def score_displayer(self):
        print("Your Current Overall Score is: ")
        '''
        Displays the corresponding values of each given key which is stored as the score of each game
        '''
        print("★ ", "━"*20 ,"★")
        print(f"1. Guess the Number Game: {self.overall_score['guess_number']}")
        print(f"2. Rock Paper Scissors: {self.overall_score['rock_paper_scissors']} ")
        print(f"3. Trivia Quiz Game: {self.overall_score['trivia_quiz']}")
        print(f"4. Pokemon Binder: {self.overall_score['pokemon_binder']}")



            

    

if __name__ == "__main__": #this make our code run only when we execute the file directly
    menu = Main_menu() #creates the main_menu obj
    menu.menu_run() #starts the program
