import random
random.seed(1)

print("Game of Scrambles!")
print("------------------")
print()

word_list = ['harvest', 'dinosaur', 'journey', 'ocean', 'pumpkin'] 

score = 0

for i in word_list:
  wrd = list(i)
  random.shuffle(wrd)
  wrd = ''.join(wrd)
  print(f"Scrambled word {word_list.index(i) + 1}: {wrd}")
  answer = input("Your guess: ")
  if answer == i:
    score += 1
print()
print(f"Your final score is: {score} out of 5!")
