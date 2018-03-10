#open the file
f = open('constitution.txt' , 'r')
#read the file
text = f.read()
#split the file
words = text.split ()
print (words)
#print the number of words in the list
words = len(words)
print(words)