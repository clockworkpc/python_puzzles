#!/usr/bin/env python

"""Tests for `python_puzzles` package."""

import pprint
import json
import logging
import time
from python_puzzles import split_deck as sd


def pp(objekt):
    prettyprint = pprint.PrettyPrinter(indent=4)
    prettyprint.pprint(objekt)


def fresh_deck():
    with open("tests/fixtures/sorted_deck.json") as file:
        return json.load(file)


def test_shuffle_and_split_repeatedly():
    my_deck = sd.Deck()
    for _ in range(10):
        logging.info("Shuffle and split cards...")
        my_deck.shuffle_deck()
        res = my_deck.cut_deck()
        half1 = res["half1"]
        half2 = res["half2"]

        half1_blacks = my_deck.count_cards_by_colour(half1, "black")
        half2_reds = my_deck.count_cards_by_colour(half2, "red")
        half2_blacks = my_deck.count_cards_by_colour(half2, "black")
        half1_reds = my_deck.count_cards_by_colour(half1, "red")

        text1 = f"Blacks in 1st: {half1_blacks}, Reds in 2nd: {half2_reds}"
        text2 = f"Blacks in 2nd: {half2_blacks}, Reds in 1st: {half1_reds}"

        time.sleep(0.5)

        logging.info(text1)
        logging.info(text2)
        logging.info("------------------------------------------")

        assert half1_blacks == half2_reds
        assert half1_reds == half2_blacks
