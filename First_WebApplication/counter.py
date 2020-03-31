#for article analyser
def count(article):
    words = article.split()
    word_count = len(words)
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    return word_count, dict_words