"""
created by Nagaj at 21/06/2021
"""
from turtle import Turtle
import pandas as pd

from logs import logger

STATES = "./data/states.csv"
FONT = ("Courier", 9, "bold")


class State(Turtle):
    STATESPATH = "./data/states.csv"
    STATES_REPORT_PATH = "./data/report.txt"
    SUCCESS = "SUCCESS GUESS"
    MISSED = "MISSED STATES"
    REPLACE_ME = "REPLACE-ME"
    HEADLINE = f"{'#' * 25} {REPLACE_ME} {'#' * 25}\n"
    states_df = pd.read_csv(STATESPATH)
    states = []
    successful_guess_states = []
    missed_states = []
    NUMBER_OF_STATES = len(states_df["state"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hideturtle()
        self.penup()
        self.coordinates = None
        self.name = None
        self.get_states()

    def add_to_screen(self):
        self.goto(self.coordinates)
        self.write(self.name, font=FONT)

    def check_coordinates(self, answer: str):
        st = self.states_df[self.states_df["state"] == answer]
        if st.shape[0] > 0:
            logger.info("successfully guess '%s'", answer)
            self.coordinates = int(st["x"]), st["y"].iloc[
                0]  # all work ==> int(st["x"]), st["x"].item(), st["x"].iloc[0]
            self.name = answer  # st["state"].item()
            self.successful_guess_states.append(self.name)
            return self.coordinates
        logger.info("bad answer for state '%s'", answer)

    @classmethod
    def get_states(cls):
        cls.states = cls.states_df["state"].tolist()
        logger.info("get states %s", cls.states)
        return cls.states

    @classmethod
    def generate_report(cls):
        with open(cls.STATES_REPORT_PATH, 'w') as file:
            file.write(cls.HEADLINE.replace(cls.REPLACE_ME, cls.SUCCESS))
            cls.update_report_with_sates(file, cls.successful_guess_states)
            file.write(cls.HEADLINE.replace(cls.REPLACE_ME, cls.MISSED))
            cls.update_report_with_sates(file, cls.get_missed_states())

    @classmethod
    def update_report_with_sates(cls, file, states: list):
        for state in states:
            file.write(state + "\n")

    @classmethod
    def get_missed_states(cls):
        cls.missed_states = [state for state in cls.states if state not in cls.successful_guess_states]
        return cls.missed_states
