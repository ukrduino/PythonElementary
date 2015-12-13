# Write a program that computes the statistics of a file's content: most frequent word,
# number of words, and number of characters.
import os

lesson_dir = os.path.dirname(__file__)
filename = os.path.join(lesson_dir, 'example.txt')


def word_sorter(word_list_to_sort):
    word_dict = dict()
    for word in word_list_to_sort:
        if word.lower() in word_dict.keys():
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1
    for word, number in word_dict.items():
        print "word [" + word + "] used - " + str(number) + " times"
    # create a list of the dict's keys and values;
    word_list = word_dict.keys()
    number_of_uses_list = word_dict.values()
    max_number_of_uses = max(number_of_uses_list)
    # return the key with the max value
    most_used_word = word_list[number_of_uses_list.index(max_number_of_uses)]
    print "Most frequently used word is - [" + most_used_word + "]. It used - " + str(max_number_of_uses) + " times."


def words_counter(text_to_process):
    all_words_list = text_to_process.replace("\n", " ")\
        .replace(",", "")\
        .replace(".", "")\
        .replace("?", "")\
        .replace("!", "")\
        .split(" ")
    while all_words_list.count("") > 0:
        all_words_list.remove("")
    print "Given file has: " + str(len(all_words_list)) + " words and " + str(len(text_to_process)) + " characters."
    word_sorter(all_words_list)

with open(filename) as f:
    text_from_file = f.read()
    words_counter(text_from_file)








