import re

text = [x for x in open(r"Tests_for_second_task/input_2_5.txt", encoding='utf-8')]    # записываем файл в массив строк
res = []
my_group = r"\bP3120\b"  # задаем номер своей группы
for s in text:
    if re.findall(r'[A-ZА-ЯЁ]\.', s)[0] == re.findall(r'[A-ZА-ЯЁ]\.', s)[1]:  # условие на инициалы вида А.А.
        if re.search(my_group, s):  # проверяем из нашей ли группы человек
            continue  # этих людей НЕ записываем в ответ
    res.append(s)  # всех остальных записываем
print(*res, sep='')
