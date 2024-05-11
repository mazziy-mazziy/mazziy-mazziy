import json
import os
import random
import io
import logging
import argparse

args_parser = argparse.ArgumentParser()
args_parser.add_argument("-i", "--import_from")
args_parser.add_argument("-e", "--export_to")
args = args_parser.parse_args()

log_stream = io.StringIO()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

log_handler = logging.StreamHandler(log_stream)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

def out_(string_):
    print(string_)
    logger.info(string_)

def in_(string_):
    print(string_)
    user_input = input()
    logger.info(string_)
    logger.info(user_input)
    return user_input



class Card:
    def __init__(self):
        self.card = dict()  # {term: [definition, error]}
        self.error_dict = dict()
    def add_card(self):
        term = in_("The card:")

        while self.check_card(term):
            term = in_("The card:")

        definition = in_("The definition of the card:")
        while self.check_card(definition):
            definition = in_('')
        self.card[term] = [definition, 0]
        out_(f"The pair (\"{term}\":\"{definition}\") has been added.")


    def check_card(self, user_input):
        for value in self.card.values():
            if user_input in value:
                out_(f"The definition \"{user_input}\" already exists. Try again:")
                return True
        if user_input in self.card.keys():
            out_(f"The term \"{user_input}\" already exists. Try again:")
            return True
        else:
            return False

    def remove_card(self):
        remove_card = in_("Which card?")
        if remove_card in self.card.keys():
            self.card.pop(remove_card)
            out_("The card has been removed.")
        else:
            out_(f"Can't remove \"{remove_card}\": there is no such card.")

    def import_card(self, cl_arg=''):
        if cl_arg == '':
            file_name = in_("File name:")
        else:
            file_name = cl_arg
        if file_name in os.listdir():
            with open(file_name, "r") as file:
                self.card = json.load(file)
            out_(f"{len(self.card)} cards have been loaded.")
        else:
            out_("File not found")

    def export_card(self, cl_arg=''):
        if cl_arg == '':
            file_name = in_("File name:")
        else:
            file_name = cl_arg
        with open(file_name, "w") as file:
            json.dump(self.card, file)
        logger.info(f"{len(self.card)} cards have been saved.")
        out_(f"{len(self.card)} cards have been saved.")

    def ask_card(self):
        ask = in_("How many times to ask?")

        for _ in range(int(ask)):
            term = random.choice(list(self.card.keys()))
            answer = in_(f"Print the definition of \"{term}\":")
            if self.card[term][0] == answer:
                out_("Correct!")
            else:
                for i in self.card.items():
                    if answer == i[1][0]:
                        output_answer = (f"Wrong. The right answer is \"{self.card[term][0]}\""
                                  f", but your definition is correct for \"{i[0]}\".")
                        break
                    else:
                        output_answer = "wrong"
                out_(output_answer)
                self.card[term][1] += 1

    def log_handler(self):
        file_name = in_("File name:")

        with open(file_name, 'w') as log_file:
            log_file.write(log_stream.getvalue())
        out_("The log has been saved.")

    def hardest_card(self):
        if [value[1] for value in self.card.values()] and max([value[1] for value in self.card.values()])>0 :
            highest_error = max([value[1] for value in self.card.values()])
            hardest_cards = [f'"{key}"' for key, value in self.card.items() if value[1] == highest_error]
            if len(hardest_cards) > 1:
                output_str = (f"The hardest cards are \"{', '.join(hardest_cards)}\". "
                              f"You have {highest_error} errors answering them.")
            else:
                output_str = (f"The hardest card is \"{', '.join(hardest_cards)}\". "
                              f"You have {highest_error} errors answering it.")
        else:
            output_str = "There are no cards with errors."
        out_(output_str)

    def reset_stat(self):
        for value in self.card.values():
            value[1] = 0
        out_("Card statistics have been reset.")


def main():

    my_card = Card()

    export_file = ''
    if args.import_from is not None:
        my_card.import_card(args.import_from)
    if args.export_to is not None:
        export_file = args.export_to

    while True:
        user_input = in_("Input the action (add, remove, import, export, "
                           "ask, exit, log, hardest card, reset stats):")
        if user_input == 'add':
            my_card.add_card()
        elif user_input == 'remove':
            my_card.remove_card()
        elif user_input == 'import':
            my_card.import_card()
        elif user_input == 'export':
            if args.export_to is None:
                cl_arg = ''
            else:
                cl_arg = args.export_to
            my_card.export_card(cl_arg)
        elif user_input == 'ask':
            my_card.ask_card()
        elif user_input == 'log':
            my_card.log_handler()
        elif user_input == 'hardest card':
            my_card.hardest_card()
        elif user_input == 'reset stats':
            my_card.reset_stat()
        elif user_input == 'exit':
            if export_file == '':
                out_("Bye bye!")
            else:
                my_card.export_card(export_file)
            break
        else:
            out_("Incorrect input")

main()