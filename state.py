"""
created by Nagaj at 21/06/2021
"""
from turtle import Turtle
from typing import Optional
import pandas as pd
from prettytable import PrettyTable
from logs import logger
STATES = "./data/states.csv"
FONT = ("Courier", 9, "bold")


class State(Turtle):
    """
    class to handle state operations
    """

    STATESPATH = "./data/states.csv"
    STATES_REPORT_PATH = "./data/report.txt"
    MISSED_STATES_PATH = "./data/states_to_lean.csv"
    SUCCESS = "SUCCESS GUESS"
    MISSED = "MISSED STATES"
    REPLACE_ME = "REPLACE-ME"
    HEADLINE = f"{'#' * 25} {REPLACE_ME} {'#' * 25}\n"
    states_df = pd.read_csv(STATESPATH)
    states = []
    missed_states = []
    successful_guess_states = []
    successful_rows = []
    state_fields = ["State", "X", "Y"]
    NUMBER_OF_STATES = len(states_df["state"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hideturtle()
        self.penup()
        self.coordinates = None
        self.name = None
        State.states = self.get_states()

    @classmethod
    def unpack_row(cls, row):
        return row["state"].iloc[0], row["x"].iloc[0], row["y"].iloc[0]

    @classmethod
    def to_prettytable(cls):
        table = PrettyTable()
        table.field_names = cls.state_fields
        table.add_rows(cls.successful_rows)
        print(table)

    def add_to_screen(self) -> None:
        """
        update screen with us-state based on coor of that state
        :return:
        """
        self.goto(self.coordinates)
        self.write(self.name, font=FONT)

    def check_coordinates(self, answer: str) -> Optional[tuple]:
        """
        if valid state, update state name with answer and add it to successful states list
        then return its coor
        :param answer: user state answer to check
        :return: state coor if it is valid state
        """
        state = self.states_df[self.states_df["state"] == answer]
        if state.shape[0] > 0:
            logger.info("successfully guess '%s'", answer)
            self.coordinates = (
                int(state["x"]),
                state["y"].iloc[0],
            )  # all work ==> int(st["x"]), st["x"].item(), st["x"].iloc[0]
            self.name = answer  # st["state"].item()
            self.successful_guess_states.append(self.name)
            self.successful_rows.append(self.unpack_row(state))
            return self.coordinates
        logger.info("bad answer for state '%s'", answer)
        return None

    @classmethod
    def get_states(cls) -> list:
        """
        get all states list
        :return: states list
        """
        states = cls.states_df["state"].tolist()
        logger.info("get states %s", states)
        return states

    @classmethod
    def generate_report(cls) -> None:
        """
        generate txt report of successful states guess and missed states
        :return:
        """
        with open(cls.STATES_REPORT_PATH, "w") as file:
            cls.update_report_with_states(
                file,
                cls.HEADLINE.replace(cls.REPLACE_ME, cls.SUCCESS),
                cls.successful_guess_states,
            )
            cls.update_report_with_states(
                file,
                cls.HEADLINE.replace(cls.REPLACE_ME, cls.MISSED),
                cls.missed_states,
            )

    @classmethod
    def update_report_with_states(cls, file, title, states: list) -> None:
        """

        :param file: text file that contains states (success or missed)
        :param title: title of states list (success or missed)
        :param states: list of states that write to file, (success or missed)
        :return:
        """
        file.write(title)
        for state in states:
            file.write(state + "\n")

    @classmethod
    def init_missed_states(cls) -> None:
        """
        if user exist the game, update states he/she missed
        :return:
        """
        cls.missed_states = [
            state for state in cls.states if state not in cls.successful_guess_states
        ]

    @classmethod
    def states_to_learn(cls) -> None:
        """
        export missed states to csv to allow user to learn more about states
        :return:
        """
        missed_states_df = cls.states_df[cls.states_df["state"].isin(cls.missed_states)]
        missed_states_df.to_csv(cls.MISSED_STATES_PATH)
