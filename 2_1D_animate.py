from gameinterface import GameInterface


class Game:

    def __init__(self, height, width):        
        self.height = height
        self.width = width
        self.grid = []
        self.game_over = False
        
        self.player_position = 0

    def run(self):
        
        # Move the player to the right
        self.player_position += 1
        
        # A list of all the rows in th grid
        self.grid = []
        
        # Programmatically generate the row
        for r in range(self.height):
            row = []
            for c in range(self.width):
                if c == self.player_position:
                    row.append("x")
                else:
                    row.append(" ")
            # Add the row to the grid
            self.grid.append(row)                
        

            
game = Game(1, 10)  # This is an object that represents the logic of the game

# This is an object that handles the display of the game
# Don't worry about how this works. It's okay for it to be a black box for now
app = GameInterface(game, tick_time=500)  
app.run()  # This runs the game and updates the display once per tick