import tkinter as tk
import keyboard

class GameInterface:
    def __init__(self, game, tick_time=500, title="My Game"):  # tick_time in milliseconds
        """Initializes the GameInterface object

        Args:
            game (Game): The game object to display
            tick_time (int, optional): The time between game updates in milliseconds. Defaults to 500.
        """
        self.game = game
        self.root = tk.Tk()
        self.root.title(title)
        self.text_area = tk.Text(
            self.root,
            height=game.height,
            width=int(game.width + 1),
            font=("Courier", 12),
        )
        self.text_area.pack(padx=10, pady=10)

        self.tick_time = tick_time

        # Wait for the window to open
        self.root.update()

        self.schedule_game_updates()

    def update_text_area(self):
        grid = self.game.grid
        formatted_grid = "\n".join("".join(row) for row in grid)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, formatted_grid)

    def schedule_game_updates(self):
        self.game.run()
        self.update_text_area()
        if self.game.game_over:
            # Wait for a return key press before restarting the game
            k = keyboard.read_key()
            if k == "q":
                self.root.quit()
            elif k == "r":
                self.game.game_over = False
                self.game.players[0].x_loc = 0
                self.game.players[0].y_loc = 5
                self.game.players[0].score = 0
                self.root.after(self.tick_time, self.schedule_game_updates)
        else:
            self.root.after(self.tick_time, self.schedule_game_updates)

    def run(self):
        self.root.mainloop()
