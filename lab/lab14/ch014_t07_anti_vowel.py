def anti_vowel(text):
    result=""
    vowels = "aeiouAEIOU"
    for i in text:
        if i not in vowels:
            result += i
    result result