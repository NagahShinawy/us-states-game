"""
created by Nagaj at 20/06/2021
"""
import turtle
from logs import logger

IMG = "./data/states.gif"  # turtle only works in gif format
TITLEBAR_ICON = "./data/states.ico"
SCREEN_TITLE = "U.S. States Game"
ASK_FOR_STATE = "What's another states name?"
INPUT_TITLE = "Guess The State {answer}/{max_answers}"
MAX_ANSWERS = 50


def setup():
    logger.info("starting setup screen")
    screen = turtle.Screen()
    screen.title(SCREEN_TITLE)
    screen.addshape(IMG)
    turtle.shape(IMG)
    root = screen._root
    root.iconbitmap(TITLEBAR_ICON)
    logger.info("setup screen finished successfully")
    return screen


def get_state_answer(screen: turtle.Screen, answer):
    state = screen.textinput(
        title=INPUT_TITLE.format(answer=answer, max_answers=MAX_ANSWERS),
        prompt=ASK_FOR_STATE,
    )
    if state:
        return state.title()
    return ""
