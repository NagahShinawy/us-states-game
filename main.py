"""
created by Nagaj at 20/06/2021
"""
import turtle
from ui import setup, get_state_answer
from state import State


def main():
    tries = 1
    score = 0
    screen = setup()
    state = State()
    while tries <= State.MAX_STATES:
        answer = get_state_answer(screen, score)
        coors = state.check_coordinates(answer)
        if coors:
            state.add_to_screen()
            score += 1
        tries += 1
    State.export_to_txt()
    turtle.mainloop()  # keeping screen open


if __name__ == "__main__":
    main()
