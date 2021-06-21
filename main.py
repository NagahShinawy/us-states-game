"""
created by Nagaj at 20/06/2021
"""
import turtle
from ui import setup, get_state_answer
from state import State

MAX_STATES = 5


def main():
    lines = []
    tries = 1
    score = 0
    screen = setup()
    state = State()
    while tries <= MAX_STATES:
        success_fail = "Fail"
        answer = get_state_answer(screen, score)
        coors = state.check_coordinates(answer)
        if coors:
            state.add_to_screen()
            score += 1
            success_fail = "Success"
        line = f"{answer}[{success_fail}]\n"
        lines.append(line)
        tries += 1
    State.export_to_txt()
    turtle.mainloop()  # keeping screen open


if __name__ == "__main__":
    main()
