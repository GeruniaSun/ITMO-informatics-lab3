# emoji :-{\
# answers for tests:
#   1   2   3   4   5
#   40  14  8   22  22
import re

text = open(r"Tests_for_first_task/input_1_1.txt", encoding='utf-8').read()  # читаем с файла
re_emoji = r':-{\\'  # шаблон для поиска эмодзи
print(len(re.findall(re_emoji, text)))  # находим длину объекта содержащего все найденные совпадения
