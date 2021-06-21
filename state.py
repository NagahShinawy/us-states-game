"""
created by Nagaj at 21/06/2021
"""
from turtle import Turtle
from logs import logger
import pandas as pd

STATES = "./data/states.csv"
FONT = ("Courier", 9, "bold")


class State(Turtle):
    states_df = pd.read_csv(STATES)
    successful_guess_states = []
    STATESPATH = "./data/report.txt"

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
            self.coordinates = st["x"].iloc[0], st["y"].iloc[0]
            self.name = answer
            self.successful_guess_states.append(self.name)
        logger.info("bad answer for state '%s'", answer)
        return self.coordinates

    @classmethod
    def get_states(cls):
        states = cls.states_df["state"].tolist()
        logger.info("get states %s", states)
        return states

    @classmethod
    def export_to_txt(cls):
        with open(cls.STATESPATH, 'w') as f:
            for state in cls.successful_guess_states:
                f.write(state + "\n")
