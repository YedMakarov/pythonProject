# Задача по теме "Генераторы".

# def all_variants(text):
#     for i in range(len(text)):
#         for j in range(i,len(text)):
#             yield text[i:j+1]

def all_variants(text):
    for size in range(len(text)):
        for i in range(len(text) - size):
            yield text[i:i + size + 1]


a = all_variants("abc")
for i in a:
    print(i)
