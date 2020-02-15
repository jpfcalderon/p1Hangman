'''
Created on Nov 23, 2019

@author: ITAUser
'''
#import the random library 

#define a function called pick_random_word():
    #open and read word dictionary/list(words.txt)   
    #variable called index = select random word from words.txt
    #variable called word = strip the randomly selected word
    #return the variable 'word'
def pick_random_word():
    f = open("words.txt", "r")
    words = f.readlines()
    index = random.randint(0, len(words)-1)
    word = words[index.strip]()
    return word
    
#define a function called ask_for_next_letter():
    #variable called letter = input function that asks user to select a letter
    #return the letter selected
def ask_user_for_next_letter():
    letter = input("Guess next letter:")
    return letter.strip(.upper())
    
#define a function called generate_word_string(word, letters_guessed)
    #variable called output = empty list
    #make a for loop that goes through each letter in the variable 'word':
        #if statement that checks if letter is in letters_guessed:
            #append letter to output
        #else:
            #append ("_")
        #return output as a string 
def generate_word_string(word, letter_guessed):
    output= []
    for letter in word:
        if letter in letters_guessed:
            output.append("_")
    return " ". join(output)
        
#create a main module:
   #variable called WORD = pick_random_word()
   #variable called letters_to_guess = set of WORD
   #variable called correct_letters_guessed = empty set
   #variable called incorrect_letters_guessed = empty set
   #variable called number_of_guesses = number of guesses you want the user to have
if __name__ == '__main__':
    WORD = pick_random_word()
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0

   #print statement that welcomes the user to hangman
   print ("Welcome to Hangman!")
   #while loop that runs until number_of_guesses less than one or letters_to_guess is greater than zero
        #variable called guess = ask_for_next_letter() and turn it into lower case
        while(len(letters_to_guess) >0) and num)guesses <6:
        guess = ask_user_for_next_letter()
        guess = guess.lower()   
#if statement that checks if guess is in correct_letters_guessed or  guess is in incorrect_letters_guessed:
    #print statement that says you already guessed that letter
if guess is correct_letters_guessed or guess is incorrect_letters_guessed:
         print("You already guessed that letter.")
    
#if statement checks if guess is in letters_to_guess:
    #remove guess from letters_to_guess
    #add guess to correct_letters_guessed
if guess is letters_to_guess:
        letters_to_guess.remove(guess)
        correct_letters_guessed.add(guess)
#else: 
    #add guess to incorrect_letters_guessed
    #number_of_guesses goes down by one 
else:
    incorrect_letters_guessed.add(guess)
     num_guesses +=1
#variable called word_string = generate_word_string(word, correct_letters_guessed)
#print statement that prints word_string 
#print statement that prints how many guesses you have left
word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left". format(6-num_guesses))
        
#if statement to check if number of guesses is greater than one:
        #print congratulations you guessed a word correctly
if num_guesses < 6:
    print ("Congratulations! You correctly guessed the word{}".format(WORD))
#else:
    #print sorry you lost the word was WORD
else:
    print ("Sorry, You lose. The word was {}".format(WORD))
   