"""
created by Nagaj at 20/06/2021
"""
import turtle
from logs import logger

IMG = "./data/states.gif"  # turtle only works in gif format
TITLEBAR_ICON = "./data/states.ico"
SCREEN_TITLE = "U.S. States Game"
ASK_FOR_STATE = "What's another states name?"
INPUT_TITLE = "Guess The State {score}/{max_answers}"
MAX_ANSWERS = 50


def setup():
    """
    setup screen with us states
    :return:
    """
    logger.info("starting setup screen")
    screen = turtle.Screen()
    screen.title(SCREEN_TITLE)
    screen.addshape(IMG)
    turtle.shape(IMG)
    root = screen._root
    root.iconbitmap(TITLEBAR_ICON)
    logger.info("setup screen finished successfully")
    return screen


def get_state_answer(screen: turtle.Screen, score):
    """
    get state answer from user
    :param screen: screen that contains map of us
    :param score: user score that will be updated after success state answer
    :return: answer with titlecase if not None
    """
    state = screen.textinput(
        title=INPUT_TITLE.format(score=score, max_answers=MAX_ANSWERS),
        prompt=ASK_FOR_STATE,
    )
    if state:
        return state.title()
    return ""
