
# def count_letters(s):
#     uppercase_count = 0
#     lowercase_count = 0

#     for glsg in s:
#         if glsg.isupper():
#             uppercase_count += 1
#         elif glsg.islower():
#             lowercase_count += 1

#     print("Количество прописных букв:", uppercase_count)
#     print("Количество строчных букв:", lowercase_count)
# count_letters("The quick Brow Fox")

def glasniy_and_soglasniy(sentence):
    glasniy = 0
    soglasniy = 0
    for glsg in sentence:
        if glsg.lower() in ['a', 'e', 'i', 'o', 'u']:
            glasniy += 1
        else:
            soglasniy += 1
    return glasniy, soglasniy