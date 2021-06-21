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
    states_df = pd.read_csv(STATESPATH)
    successful_guess_states = []
    MAX_STATES = len(states_df["state"])

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
        states = cls.states_df["state"].tolist()
        logger.info("get states %s", states)
        return states

    @classmethod
    def export_to_txt(cls):
        with open(cls.STATES_REPORT_PATH, 'w') as f:
            for state in cls.successful_guess_states:
                f.write(state + "\n")
