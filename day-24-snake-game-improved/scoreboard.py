from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_history.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):

        self.clear()
        self.write(f"Score={self.score} - Higher Score={self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("score_history.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()
