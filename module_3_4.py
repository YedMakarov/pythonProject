# Задача "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        if i.lower().count(root_word.lower()):
            same_words.append(i)

    if same_words == []:
        for j in other_words:
            if root_word.lower().count(j.lower()):
                same_words.append(j)

    return same_words


# Main
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
