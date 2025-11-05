import random
print("Welcome to Hangman Game!")
word_list=["apple","banana","peach","orange"]
chosen_word=random.choice(word_list)
print(chosen_word)
lives=6
placeholder=""
for letter in chosen_word:
    placeholder+="_"
print(placeholder)
correct_letter=[]
game_over=False
while not game_over:
    print(f"Your lives 6/{lives} left!")
    guess=input("Guess a letter:").lower()
    display=""
    if guess in correct_letter:
        print(f"You have already guess this letter:{correct_letter}")
        continue
    for letter in chosen_word:
        if letter ==guess:
            display+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in correct_letter:
        lives-=1
        if lives==0:
            game_over=True
            print(f"The word was:{chosen_word},You lose!")
    if "_" not in display:
        game_over=True
        print("You Win!")
