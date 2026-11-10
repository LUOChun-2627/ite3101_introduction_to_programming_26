def censor(text, word):
    n = "*" * len(word)
    return text.replace(word, n)