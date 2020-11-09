word1 = input()
word2 = input()

# How many letters does the longest word contain?
print(len(word2) if len(word2) >= len(word1) else len(word1))
