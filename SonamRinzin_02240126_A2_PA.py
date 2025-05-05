class Menu:
    def __init__(self):
        self.scores1 = 0
        self.scores2 = 0
        self.scores3 = 0
        self.scores4 = 0
    def menu(self):
        while True:
            print("Select a function (0-5)")
            print("1. Guess the Number")
            print("2. Rock Paper Scissors game")
            print("3. Trivia Pursuit Game ")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall Score")
            print("0. Exit Program")
    def program_run(self):
        while True:
            self.menu()
            function_choice = int(input("Your choice: "))
            if function_choice == 1 :
                game = guess_the_number()
                self.scores1 = game.play()
            elif function_choice == 2 :
                game = rock_paper_scissors()
                self.scores2 = game.play()
            elif function_choice == 3:
                game = Trivia_pursuit_game()
                self.scores3 = game.play()
            elif function_choice == 4:
                game = pokemon_card_binder_manager()
                self.scores4 = game.play()
            elif function_choice == 5:
                slef.score_display()
            elif function_choice == 0:
                print("End")
                break
            else:
                print("Invalid")  
    def score_display():
        print("Scores:")
        print("Guess the number: "+ self.scores1 )  
        print("Rock paper scissors: " + self.scores2)  
        print("trivia quiz: "+ self.scores3)  
        print("Pokemon binder:" + self.scores4)  
        print("Total score:")  
                
#main execution of the game
if __name__ = "__main__"
    menu = Menu()
    menu.run()