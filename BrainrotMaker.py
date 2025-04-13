import random

BrainRotWords = [
    "sigma", "skibidi", "goon", "rizz",
    "gyatt", "slay", "bussin", "sus",
    "skibidi", "nahida", "goofy", "broki",
    "npc", "based", "mid", "ligma",
    "drip", "zaza", "glo", "fanum",
    "shid", "gyat", "delulu", "slopper",
    "skibidi rizzy", "meemaw", "brainrot", "smeagol"
]

while True:
    print(" ")
    word = str(input(" Enter atleast 5 words: "))

    NewWord = []

    for letter in word:
        if letter == " ":
            if random.randint(1,3) == 1:
                NewWord.append(f" {random.choice(BrainRotWords)} ")
            else:
                    if letter == "":
                        NewWord.append(letter + " ")
                    else:
                        NewWord.append(letter)
        else:
            NewWord.append(letter)
    for lt in NewWord:
        print(lt, end="")


