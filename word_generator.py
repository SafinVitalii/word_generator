from Dictogram import Dictogram
import random
import re
import codecs


def make_markov_model(data):
    markov_model = dict()

    for i in range(0, len(data) - 1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i + 1]])
        else:
            markov_model[data[i]] = Dictogram([data[i + 1]])

    return markov_model


def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data) - order):
        window = tuple(data[i: i + order])
        if window in markov_model:
            markov_model[window].update([data[i + order]])
        else:
            markov_model[window] = Dictogram([data[i + order]])

    return markov_model


def generate_random_start_advanced(model):
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word = model['END'].return_weighted_random_word()
        return seed_word
    return random.choice(list(model.keys()))


def generate_random_sentence(length, markov_model):
    current_word = generate_random_start_advanced(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'


if __name__ == '__main__':
    content = ""
    files_to_read = ["pride_and_prejudice.txt", "alice_adventures_in_wonderland.txt", "the_picture_of_dorian_gray.txt",
                     "war_and_peace.txt", "iliad.txt"]
    print("Reading data from files...")
    for file_name in files_to_read:
        with codecs.open(file_name, "r", "utf-8") as content_file:
            content += content_file.read()
    print("Parsing content...")
    content_splitted = re.findall(r"[\w']+", content)
    print("Building Markov model...")
    model = make_markov_model(content_splitted)
    print("Done!\n\n")
    user_choice = int(input("Enter the length of a sentence to generate: "))
    while user_choice != 0:
        print(generate_random_sentence(user_choice, model))
        user_choice = int(input("Enter the length of a sentence to generate: "))
