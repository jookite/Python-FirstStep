s = input()

vowels = "aeiouwyAEIUOWY"

for vowel in vowels:
  for i in s:
    if i == vowel:
      s = s.replace(vowel,"")
print(s)