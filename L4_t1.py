# LAb4 Task1:Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase 



fin=open("mybook.txt")
for line in fin:
    word=line.strip()
    print(word)

