#2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
inpt = input("Enter sentense to find the vowel in your sentence: ")
vowel = ["A","a","e","E","I","i","O","o","U","u"]
ans = []
for i in vowel:
    for j in range(len(inpt)):
        if i ==inpt[j]:
            ans.append(i)
print(len(ans))
