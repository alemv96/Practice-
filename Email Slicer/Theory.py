# within this file, we will make sure to study
# string methods to get words using slicing theory.
# reference: word [start : end  : step] 
# understand step as how many words you want to show.   
# if we use word[start : ] it will start in index 5 and then it will show letters until the end. 
#if we use word[start : : steps] it will assume to go until the end, using the number of steps. 
#You can also use word[:end] and it will start at the beginning and show until the end number you provide. 
#Strings are immutable data types. 
word = 'supercalifragilisticexpialidocious'
print(word[5::2])
#Reversing a string: 
print(word[::-1])

# we can use methods inside of methods: 
print(word[word.index("cali") : word.index("fragi")])
print(word[word.index("docious"):])
