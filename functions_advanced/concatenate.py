def concatenate(*words, **kw_words):
    text = ''.join(words)

    for key, value in kw_words.items():
        text = text.replace(key, value)

    return text


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
