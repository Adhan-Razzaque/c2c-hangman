hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)


word = "test"
num_wrong_guesses = 0
wrong_letters = []
correct_guesses = []
for x in list(word):
    correct_guesses.append("_")

while num_wrong_guesses <= num_wrong_guesses_allowed:
    guess = input("what's your letter? ").lower()
    if guess in word:
      print("Correct")
      for ind, char in enumerate(list(word)):
          if char in guess:
            del correct_guesses[ind]
            correct_guesses.insert(ind, guess)
      draw_hangman(num_wrong_guesses)
      print(correct_guesses)
    else:
      print("Try Again")
      num_wrong_guesses += 1
      draw_hangman(num_wrong_guesses)
      wrong_letters.append(guess)
      print(wrong_letters)
    if word == ''.join(correct_guesses):
        print("You Win!")
        break
    if num_wrong_guesses > num_wrong_guesses_allowed:
        print("You lose")