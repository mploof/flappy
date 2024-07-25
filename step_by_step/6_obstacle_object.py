from gameinterface import GameInterface

class Player:
    
    def __init__(self, x, y, icon):
        self.x = x
        self.x_dir = 1        
        self.y = y
        self.y_dir = 1
        self.icon = icon
        
class Obstacle:
    
    def __init__(self, x, y, icon="🌵"):
        self.x = x
        self.y = y
        self.icon = icon

class Game:

    def __init__(self, height, width, players, obstacles):        
        self.height = height
        self.width = width
        self.grid = []
        self.game_over = False
        
        self.players = players
        self.obstacles = obstacles

    def run(self):
        
        for player in self.players:
            # Move the player
            player.x += 1 * player.x_dir
            player.y += 1 * player.y_dir
            
            # Change direction if the player reaches the edge
            if player.x == 0 or player.x == self.width-1:
                player.x_dir *= -1
                
            if player.y == 0 or player.y == self.height-1:
                player.y_dir *= -1
        
        # A list of all the rows in th grid
        self.grid = []
        
        # Programmatically generate the rows
        for r in range(self.height):
            row = []
            for c in range(self.width):
                this_cell = " "
                for player in self.players:
                    if c == player.x and r == player.y:
                        this_cell = player.icon
                for obstacle in self.obstacles:
                    if c == obstacle.x and r == obstacle.y:
                        this_cell = obstacle.icon
                row.append(this_cell)
            # Add the row to the grid
            self.grid.append(row)                
            
players = [Player(0, 0, "x"), Player(2, 3, "o")]
obstacles = [Obstacle(4, 4), Obstacle(8, 2)]
game = Game(5, 10, players, obstacles)  # This is an object that represents the logic of the game

# This is an object that handles the display of the game
# Don't worry about how this works. It's okay for it to be a black box for now
app = GameInterface(game, tick_time=500)  
app.run()  # This runs the game and updates the display once per tick