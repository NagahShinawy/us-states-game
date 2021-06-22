"""
created by Nagaj at 20/06/2021
"""
from ui import setup, get_state_answer, logger
from state import State

EXIT = "Exit"


def main():
    """
    entry point of game
    :return:
    """
    tries = 1
    score = 0
    screen = setup()
    state = State()
    while tries <= State.NUMBER_OF_STATES:
        answer = get_state_answer(screen, score)
        if answer == EXIT:
            logger.info("Stopping app using '%s' after '%d' tries", EXIT, tries - 1)
            State.init_missed_states()
            break
        coors = state.check_coordinates(answer)
        if coors:
            state.add_to_screen()
            score += 1
        tries += 1
    State.generate_report()
    State.states_to_learn()
    # turtle.mainloop()  # keeping screen open
    # screen.exitonclick()


if __name__ == "__main__":
    main()
