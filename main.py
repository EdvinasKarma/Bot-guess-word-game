import random


with open('words.txt', 'r') as file:
    reader = file.read().replace(" ", "").lower()

reader = reader.split()
words = []
for i in reader:
    words.append(i[-6:])


def BotGuessWord(words: list, myword: str):
    
    if myword not in words:
        return "Your word not matches game words"

    times = 1
    while True:

        random_guess = random.choice(words)
        print(f"Bot guess: {random_guess}")

        if random_guess == myword and times == 1:
            print(f'Found word "{myword}" in first try!')
            break
        elif random_guess == myword:
            print(f'Found word "{myword}" in {times} tries!')
            break

        for index, letter in enumerate(random_guess):
                
            if letter == myword[index]:
                words = [word for word in words if letter == word[index]]
                
            if letter not in myword:
                words = [word for word in words if letter not in word]

        times += 1
 
    return None

        
"""
Bot can guess only words that are in words.txt file
"""
myword = input("Your word: ")
print(BotGuessWord(words,myword))
