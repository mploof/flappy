import random

from gameinterface import GameInterface

class Player:
    
    def __init__(self, x, y, icon):
        self.x = x
        self.x_dir = 1        
        self.y = y
        self.y_dir = 1
        self.icon = icon
        self.score = 0
        
class Obstacle:
    
    def __init__(self, x, y, icon="🌵"):
        self.x = x
        self.y = y
        self.icon = icon

class Game:

    def __init__(self, height, width, players, obstacle_count=10):        
        self.height = height
        self.width = width
        self.grid = []
        self.game_over = False
        
        self.players = players
        self.obstacles = self.generate_obstacles(obstacle_count)
    
    def generate_obstacles(self, num_obstacles):
        obstacles = []
        for _ in range(num_obstacles):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            obstacles.append(Obstacle(x, y))
        return obstacles
        
    def check_collision(self):
        for player in self.players:
            scored = False
            for obstacle in self.obstacles:
                if player.x == obstacle.x:
                    scored = True
                    if player.y == obstacle.y:
                        self.game_over = True
                        print("Game Over")
                        
            if scored and not self.game_over:
                player.score += 1
                print(f"Player {player.icon} scored! Total score: {player.score}")

    def move_players(self):
        for player in self.players:
            # Move the player
            player.x += 1 * player.x_dir
            player.y += 1 * player.y_dir
            
            # Change direction if the player reaches the edge
            if player.x == 0 or player.x == self.width-1:
                player.x_dir *= -1
                
            if player.y == 0 or player.y == self.height-1:
                player.y_dir *= -1
    
    def update_grid(self):
        # A list of all the rows in th grid
        self.grid = []
        
        # Programmatically generate the rows
        for r in range(self.height):
            row = []
            for c in range(self.width):
                this_cell = " "
                
                # Draw the players
                for player in self.players:
                    if c == player.x and r == player.y:
                        this_cell = player.icon

                # Draw the obstacles
                for obstacle in self.obstacles:
                    if c == obstacle.x and r == obstacle.y:
                        this_cell = obstacle.icon
                        
                row.append(this_cell)
                
            # Add the row to the grid
            self.grid.append(row)
            
    def run(self):
                
        self.move_players()
        self.update_grid()  
        self.check_collision()

players = [Player(0, 0, "x"), Player(2, 3, "o")]
game = Game(10, 15, players, 4)  # This is an object that represents the logic of the game

# This is an object that handles the display of the game
# Don't worry about how this works. It's okay for it to be a black box for now
app = GameInterface(game, tick_time=500)  
app.run()  # This runs the game and updates the display once per tick