from turtle import Turtle



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt") as data:
            self.high_score  = int(data.read())

        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 270)

        self.write(f"Score = {self.score}" ,  align="left", font = ("Arial", 16, "normal"))
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = 'w') as data:

                data.write(f"{self.high_score}")



        self.goto(150, 270)
        self.write(f"HighScore = {self.high_score}", align="right", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font = ("Arial", 16, "normal"))

    def refresh_score(self):

        self.score += 1
        self.clear()
        self.update_score()

    def start_over(self):
        self.score= 0
        self.update_score()



