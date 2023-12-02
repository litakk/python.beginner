# user = str(input())
# text = print(len(user))
# print(user[::2]) # через 1  символ 
# print(user[::-2]) # через 1 символ наоборот

import re

text = "Mentioning of reD, GrEen and BLUE is prohibited"
words_to_replace = ["red", "green", "blue"]

new_text = re.sub(f'{"|".join(words_to_replace)}',
                "***",
                text,
                flags=re.IGNORECASE)
print(new_text)