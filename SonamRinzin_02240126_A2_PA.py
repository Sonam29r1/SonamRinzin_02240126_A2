class Main_menu:
    def menu(self):
        print("Select a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("0. Exit program")
        
    def menu_run(self):
        while True:
            self.menu()
            player_choice = int(input("Enter the game you want to play: "))

            if player_choice == 1:
                #run guess the number game
                print("okay")
                print("--------------------------------------------------------------")
            elif player_choice == 2:
                #run rpc
                print("")
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



if __name__ == "__main__":
    menu = Main_menu()
    menu.menu_run()
