def censor(text, word):
    stars = "*" * len(word)
    return " ".join(stars if w == word else w for w in text.split())