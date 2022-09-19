from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()

def game():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    difficulty = screen.textinput(title="snake game difficulty", prompt="(e) for easy, (m) for medium, (h) for hard")
#game difficulty
    if difficulty == "e":
        FPS = 0.2
    elif difficulty == "m":
        FPS = 0.1
    else:
        FPS = 0.05
#controls
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkeypress(snake.up, "w")
    screen.onkeypress(snake.left, "a")
    screen.onkeypress(snake.down, "s")
    screen.onkeypress(snake.right, "d")
#snake move
    screen.update()
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(FPS)
        snake.move()
#detect collision with food
        if snake.segments[0].distance(food) < 18:
            food.refresh()
            scoreboard.eaten()
            snake.extend()

        if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or \
                snake.segments[0].ycor() < -290:
            scoreboard.changehs()
            scoreboard.loser()
            game_is_on = False

    #detect collision with tail
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                game_is_on = False
                scoreboard.changehs()
                scoreboard.loser()

    recurs = screen.textinput(title="do you want to play again", prompt="(y) for yes and (n) for no")
    if recurs == "y":
        screen.reset()
        game()
    else:
        screen.bye()
#runs the game
game()
screen.exitonclick()
