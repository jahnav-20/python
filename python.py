# Input string
s = "hi hello raju"

vowels = ""
consonants = ""

for ch in s:
    if ch.isalpha():  # Ignore spaces
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            consonants += ch

print("Vowels:", vowels)
print("Consonants:", consonants)