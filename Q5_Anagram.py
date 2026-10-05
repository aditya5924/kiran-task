word1 = input("Enter first word: ")
word2 = input("Enter second word: ")


word1_clean = word1.lower().replace(" ", "")
word2_clean = word2.lower().replace(" ", "")

if sorted(word1_clean) == sorted(word2_clean):
    print(f"'{word1}' and '{word2}' are Anagrams.")
else:
    print(f"'{word1}' and '{word2}' are Not Anagrams.")