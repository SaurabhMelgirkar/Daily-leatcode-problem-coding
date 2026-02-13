# import random

# def jumble_word(word):
#     word_letters = list(word)
#     random.shuffle(word_letters)
#     return ''.join(word_letters)

# def guess_the_character():
#     characters = ["Ironman", "Elsa", "Yoda", "Moana", "Harry", "Simba"]
#     original = random.choice(characters)
#     jumbled = jumble_word(original)

#     print("Guess the character from this jumble:", jumbled)
#     guess = input("Your guess: ")

#     if guess.lower() == original.lower():
#         print("Correct!")
#     else:
#         print("Oops! The correct answer was:", original)

# guess_the_character()
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix[2][1])