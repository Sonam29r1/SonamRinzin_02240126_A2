
class Pokemon_Binder_Manager:
    def __init__(self):
        self.binder = {}  # used dictionary to store card info since it overwrites exisiting keys or vlaues(suitable as it avoids duplicates)
        self.total_cards = 0 # 
        self.max_pokedex = 1025 # Limit is 1025
        self.cards_per_page = 64  # 8x8 grid
        self.rows_per_page = 8 # 8 rows per page
        self.cols_per_page = 8 # 8 rows per colum
        

    def calculate_position(self, pokedex_num):
        """
        Algorithm and logic:
        1. First, we convert the Pokedex number to a 0-based index to avoid the need to handle page 0
        2. Then, to determin the page number, used floor division to find which page the card belongs to by using the formula pokedex Number//64 and add 1 to turn into 1_based index since our card starts from 1 to 1025
        - since a page hold 64 cards and we need an whole number as a page number.
        - if we take 2 as our pokdex number we get 2//64 = 0 then add 1 and we get our page number as 1
        - if pokedex no = 132 we get 132//64 = 2 and then add one and we get our page as 3
        3. To determine the position within the page, used modulo operation since the remainder is the postion in page and we add one since our pokedex number is 0 based index(turns to 1_based index)
        - if we take 2 as position_in_collection, 2 % 64 = 0(adds 1 when calculationg row and column)
        - if position_in_collection = 132, 132 % 64 = 4(add 1 in row and column)
        4. Calculate the row and column within the page by further division and modulo operations.(Same logic applies here)
        - we take pos_in_page for calculationg row and column since this shows where the card's slot is located in the page from 0 to 63
        - then we use (pos_in_page // 8 (since is 8x8) and adds 1 since our binder is 1-based index
        - for column we use (pos_in _page // 8(8x8) ) and adds 1
        """
        position_in_collection = pokedex_num - 1  # Convert to 0-based index
        page = (position_in_collection // self.cards_per_page) + 1 
        pos_in_page = position_in_collection % self.cards_per_page
        row = (pos_in_page // self.cols_per_page) + 1
        column = (pos_in_page % self.cols_per_page) + 1
        return {'page': page, 'row': row, 'col': column}    
    
    def add_card(self, pokedex_num):
        '''
        Validation
        - entered card number should be between 1 and 1025
        '''
        if not 1 <= pokedex_num <= 1025: # Handles all other invalid inputs
            print("❌ Error: Invalid Pokedex number 0. Must be between 1-1025")
            return
        
        '''
        Avoids(overwrites) duplicated cards in the binder
        '''
        if pokedex_num in self.binder: #checks if card exist in the binder
            print(f"⚠️ Card #{pokedex_num} already exists in the binder!")
            return
        
        '''
        Entered pokedex number(pokedex_num) is taken and uses calculate_postion funtion to calculate its position
        in the binder
        '''
        position = self.calculate_position(pokedex_num)
        self.binder[pokedex_num] = position
        self.total_cards += 1
        
        '''Above calculated postion is printed or displayed'''
        print(f"Page: {position['page']}")
        print(f"Position: Row {position['row']}, Column {position['col']}")
        print(f"Status: Added Pokedex #{pokedex_num}")
        
        # Checks if card collection is completed 
        if self.total_cards == self.max_pokedex:
            print("🎉 CONGRATULATIONS! You've caught them all! 🎉")
            
    
    def reset_binder(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder")
        confirmation = input("Type 'CONFIRM' to reset or any other key to CANCEL: ").upper() #Confirmation from players and made case insenstive

        '''If user confrims to reset, uses dict method clear to erase everthing'''
        
        if confirmation == "CONFIRM": #User confrimation to avoid accidental data loss
            self.binder.clear() #upon confrimation clears the binder
            self.total_cards = 0 # set total cards value to 0
            print("Binder reset successfully")
        else:
            print("Reset cancelled")

    def display_binder(self):
        print("\nCurrent Binder Contents:")
        '''For every pokedex number in our sorted binder, we print its pokdex num along with its postion'''
        for pokedex_num in sorted(self.binder.keys()):
            pos = self.binder[pokedex_num]
            print(f"Pokedex #{pokedex_num} \n Page :{pos['page']}, Row :{pos['row']}, Column:{pos['col']}")
        
        print(f"\nTotal cards: {self.total_cards}") #Displays how many cards player have collected so far
        print(f"Completion: {(self.total_cards/self.max_pokedex)*100:.2f}%") # calculates and displays the percentage of card collection and round it to two decimals

    def total_score(self):
        score = self.total_cards
        return score
        
    


