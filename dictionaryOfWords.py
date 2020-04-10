"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Despair"] = "Feelings of hopelessness and great sadness brought on by coding"
word_definitions["High-Five"] = "A mutual slapping of hands between two parties to signify accomplishment or agreement"
word_definitions["Beer"] = "Alcoholic substance used to increase confidence in coding"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

# print(word_definitions["Despair"])
# print(word_definitions["Beer"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for word, definition in word_definitions.items():
    print(f'The definition of {word} is {definition}')