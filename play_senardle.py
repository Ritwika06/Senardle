from main import Senardle
from letter import LetterState
from typing import List
from colorama import Fore
import time
import random

ALPHABET = "Q W E R T Y U I O P\n A S D F G H J K L\n  Z X C V B N M"
def main():
    
    word_set = load_word_set('wordset.txt')
    secret = random.choice(list(word_set))
    print('Welcome to Senordle!\nRules:\nYou have 9 chances to guess a 6 letter word in 10 mins ')
    
    senardle = Senardle(secret)
        
    limit = 600
    start_time = time.time()
    while senardle.can_attempt:
        x = input("Type a word: ")
            
        if len(x) != senardle.WORD_LENGTH:
            print("Word must be 6 characters long")
            continue
        
        senardle.attempt(x)
        display(senardle)
        
        elapsed_time = time.time() - start_time
        remain = round((limit - float(elapsed_time))/60, 2)
        print(remain , "minutes remaining")
        if elapsed_time > limit:
            print("Time up! Game Over")
            
            break
        else:
            continue
            
    if senardle.is_solved:
        print("Congratulations! You got the word!")
        
    else:
        print("Try again")
    print("The word was: ",secret) 
    
 
def border(lines: List[str], size: int = 11, pad: int = 1):
    
    content = size + pad * 2
    top = "╔" + "═" * content + "╗"
    bottom = "╚" + "═" * content + "╝"
    space = " " * pad
    print(top)
    
    for l in lines:
        print("║" + space + l + space + "║")
    print(bottom)
        
def display(senardle: Senardle):
    lines = []
    
    for word in senardle.attempts:
        result = senardle.guess(word)
        colored_result_str = color(result)
        lines.append(colored_result_str)
        
    for _ in range(senardle.remain_attempts):
        lines.append(" ".join(["_"] * senardle.WORD_LENGTH))
    border(lines)
    print(ALPHABET)
    
def color(result: List[LetterState]):
    color_result = []
    for letter in result:
        if letter.is_in_position:
           color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        color_letter = color + letter.char + Fore.RESET
        color_result.append(color_letter)
    return " ".join(color_result)
    
def load_word_set(path:str):
    word_set = set()
    with open(path,"r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set
            
if __name__ == "__main__":
    main()