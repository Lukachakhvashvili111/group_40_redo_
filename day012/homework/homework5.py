def collect_words():
    word = ""
    words = []
    while word != "საკმარისი":
        word = input("შეიყვანეთ სიტყვა: ")
        if word != "საკმარისი":
            words.append(word)
    return words
