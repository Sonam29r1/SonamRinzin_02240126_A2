
class Pokemon_Binder_Manager:
    def __init__(self):
        self.binder = {}  # Dictionary to store card info
        self.total_cards = 0
        self.max_pokedex = 1025
        self.cards_per_page = 64  # 8x8 grid
        self.rows_per_page = 8
        self.cols_per_page = 8

    def calculate_position(self, pokedex_num):  # Fixed method name
        pos_in_collection = pokedex_num - 1  # Convert to 0-based index
        page = (pos_in_collection // self.cards_per_page) + 1
        pos_in_page = pos_in_collection % self.cards_per_page
        row = (pos_in_page // self.cols_per_page) + 1
        col = (pos_in_page % self.cols_per_page) + 1
        return {'page': page, 'row': row, 'col': col}    
    
    def add_card(self, pokedex_num):
        # Validation checks
        if not 1 <= pokedex_num <= 1025:
            print("❌ Error: Invalid Pokedex number 0. Must be between 1-1025")
            return
        if pokedex_num in self.binder:
            print(f"⚠️ Card #{pokedex_num} already exists in the binder!")
            return
        
        position = self.calculate_position(pokedex_num)
        self.binder[pokedex_num] = position
        self.total_cards += 1
        
        # Print placement info
        print(f"Page: {position['page']}")
        print(f"Position: Row {position['row']}, Column {position['col']}")
        print(f"Status: Added Pokedex #{pokedex_num}")
        
        # Check for complete collection
        if self.total_cards == self.max_pokedex:
            print("🎉 CONGRATULATIONS! You've completed the entire collection! 🎉")
            
    def reset_binder(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder")
        confirmation = input("Type 'CONFIRM' to reset: ").upper()
        
        if confirmation == "CONFIRM":
            self.binder.clear()
            self.total_cards = 0
            print("Binder reset successfully")
        else:
            print("Reset cancelled")

    def display_binder(self):
        print("\nCurrent Binder Contents:")
        for pokedex_num in sorted(self.binder.keys()):
            pos = self.binder[pokedex_num]
            print(f"Pokedex #{pokedex_num}: Page {pos['page']}, Row {pos['row']}, Column {pos['col']}")
        
        print(f"\nTotal cards: {self.total_cards}")
        print(f"Completion: {(self.total_cards/self.max_pokedex)*100:.2f}%")
    


