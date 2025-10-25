# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    
    new_sentence = ""
    first_letter_done = False
    for character in sentence:
        if character.isupper():
            if first_letter_done == False:
                new_sentence += character
                first_letter_done = True
            else:
                new_sentence += " "
                new_sentence += character.lower()
        else:
            new_sentence += character
    return new_sentence

input_string = input('Enter a sentance with no spaces and the first letter of every word is capitalized ')
output_string = word_separator(input_string)
print(output_string)


   

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
