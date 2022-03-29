import os

def read_file(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read().split()

possible_words = read_file("data/possible_words.txt")
removed_words = []
available_colors = ["green", "gray", "grey", "yellow"]

os.system('cls||clear')

for i in range(6):
    user_word_data = []
    while True:
        user_word = input("What word did you put in?: ")
        os.system('cls||clear')
        if user_word not in removed_words and user_word in possible_words:
            break
        elif user_word in removed_words or user_word not in possible_words:
            print("'%s' is not a valid word to use. Please choose another word\n" % user_word)
    for user_letter, user_letter_pos in zip(user_word, range(len(user_word))):
        while True:
            user_letter_color = input("What color was the letter '%s': " % user_letter)
            if user_letter_color in available_colors:
                break
            elif user_letter_color not in available_colors:
                print("'%s' is not one of the color options. Please choose either: 'green', 'gray', 'grey' or 'yellow'.\n" % user_letter_color)
        if user_letter_color == "gray" or user_letter_color == "grey":
            letter_is_duplicate = False
            for letter in user_word_data:
                if letter[0] == user_letter:
                    letter_is_duplicate = True
            if not letter_is_duplicate:
                for word in possible_words:
                    if user_letter in word and word not in removed_words:
                        removed_words.append(word)
            user_word_data.append([user_letter, user_letter_color])
        elif user_letter_color == "yellow":
            for word in possible_words:
                if word not in removed_words:
                    if user_letter not in word:
                        removed_words.append(word)
                    else:
                        word_split = list(word)
                        if word_split[user_letter_pos] == user_letter:
                            removed_words.append(word)
            user_word_data.append([user_letter, user_letter_color])
        elif user_letter_color == "green":
            for word in possible_words:
                if word not in removed_words:
                    if user_letter not in word:
                        removed_words.append(word)
                    else:
                        word_split = list(word)
                        if word_split[user_letter_pos] != user_letter:
                            removed_words.append(word)
            user_word_data.append([user_letter, user_letter_color])
    
    green_count = 0
    for data in user_word_data:
        if data[1] == "green":
            green_count += 1
    if green_count == len(user_word):
        print("Congratulations, you have found the answer to today's Wordle! :)")
        exit(1)
    words_that_need_printing = []
    for word in possible_words:
        if word not in removed_words:
            words_that_need_printing.append(word)
    
    os.system('cls||clear')
    print("WORDS AVAILABLE TO USE:")
    print(words_that_need_printing)