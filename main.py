from flappy import Player, Game
from gameinterface import GameInterface

# Create two players and set their initial positions, keys, and icons
# For convenience, we can put them in a list
players = [] # List of Player objects

players.append( Player(5, 5, "a", "🐥") )
players.append( Player(0, 5, "f", "🐔") )



# Set the parameters for the game
obstacle_count = 10
game_width = 100    # The width of the game grid
game_height = 10    # The height of the game grid
tick_time = 200     # The time between game updates in milliseconds

game = Game(game_height, game_width, players, obstacle_count)
app = GameInterface(game, tick_time)
app.run()
