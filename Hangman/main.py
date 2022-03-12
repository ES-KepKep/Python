from random_word import RandomWords

rw = RandomWords()
word_gen = list(rw.get_random_word())
answer = [char.upper() for char in word_gen]
hidden_A = ["_" for letter in range(len(answer))]
used_letters = []
lives = 10

while(lives > 0):
    if not ("_") in hidden_A:
        print("You win!")
        break

    print(f"You have {lives} lives")
    print(f"{hidden_A}\n")
    user_input = input().upper()

    if user_input in used_letters:
        print(f"You have already used the letter {user_input}\n")
    else:
        used_letters.append(user_input)
        if user_input in answer:
            indexes = [i for i, x in enumerate(answer) if x == user_input]
            for i in indexes:
                hidden_A.pop(i)
                hidden_A.insert(i, user_input)
        else:
            lives -= 1

if lives == 0:
    print("You lost")
    print(f"The word was {answer}")