#!python3

lst = []
 
for i in range(0, 5):
    ele = input("Enter a word")
    lst.append(ele)
     
f = open("task3.txt", "a")
f.write(str(lst))
f.close()

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]
'''
