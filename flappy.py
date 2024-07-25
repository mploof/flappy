import random
import keyboard

class Player:
    
    def __init__(self, x_loc, y_loc, key, icon):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.key = key
        self.icon = icon
        self.score = 0

    def move(self, dir):
        if dir == "up":
            self.y_loc -= 1
        elif dir == "down":
            self.y_loc += 1
        elif dir == "left":
            self.x_loc -= 1
        elif dir == "right":
            self.x_loc += 1

class Obstacle:

    def __init__(self, x, y, icon="🌵"):
        self.x_loc = x
        self.y_loc = y
        self.icon = icon

class Game:

    def __init__(self, title, height, width, players, obstacle_count):
        self.title = title
        self.height = height
        self.width = width
        self.players = players
        self.obstacles = self.generate_obstacles(obstacle_count)
        self.grid = []
        self.game_over = False

    def generate_obstacles(self, num_obstacles):
        obs = []
        for _ in range(num_obstacles):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            obs.append(Obstacle(x, y))
        return obs

    def run(self):

        # At each game tick
        #    - Check for keypress
        #    - Move the players
        #    - Check if the player is dead
        #    - Check if the player scored
        #    - Update the grid
        for player in self.players:

            # Check for keypress
            if keyboard.is_pressed(player.key):
                player.move("up")
            else:
                player.move("down")
            
            # No matter what, the player always moves right at each tick
            player.move("right")
            
            # Check if the player is dead
            if self.player_is_dead(player):
                print(f"{player.icon} died!")
                total_score = 0
                for b in self.players:
                    total_score += b.score
                print(f"Final Score: {total_score}")
                self.game_over = True
            
            # If the player is not dead, check if it scored
            elif self.player_scored(player):
                player.score += 1
                print(f"{player.icon} scored: {player.score}!")

        # Check if the game is over so we don't update the grid if it is
        if not self.game_over:
            self.update_grid()

    def update_grid(self):
        """Return the current grid of the game with the players and obstacles

        Returns:
            list: a list of lists of strings representing the game grid
        """
        
        # Start with a blank grid        
        grid = []

        # Fill the grid with empty spaces row by row
        for _ in range(0, self.height):
            # Add a row of empty spaces
            grid.append([" "] * self.width)

        # Get the location of each player and obstacle and add them to the grid
        for player in self.players:
            grid[player.y_loc][player.x_loc] = player.icon

        for obstacle in self.obstacles:
            try:
                grid[obstacle.y_loc][obstacle.x_loc] = obstacle.icon
            except IndexError:
                print("Obstacle out of bounds")
                print(obstacle.x_loc, obstacle.y_loc)

        # Update the game grid with the new grid
        self.grid = grid

    def player_is_dead(self, player):
        off_screen = (
            # Off screen to the right or left
            player.y_loc >= self.height or 
            player.y_loc < 0 or 
            # Off screen to the top or bottom
            player.x_loc >= self.width or 
            player.x_loc < 0
        )
        
        # Start by assuming there is no collision
        collision = False
        
        # If the player is at the same location as an obstacle, there is a collision
        for obstacle in self.obstacles:
            if player.x_loc == obstacle.x_loc and player.y_loc == obstacle.y_loc:
                collision = True
        
        # The player is dead if it is off screen or there is a collision
        return off_screen or collision

    def player_scored(self, player):
        # If the player is at the same x location as an obstacle, but not at the same y location
        # then the player has passed the obstacle and scored a point
        for obstacle in self.obstacles:
            if player.x_loc == obstacle.x_loc and player.y_loc != obstacle.y_loc:
                return True
        return False
