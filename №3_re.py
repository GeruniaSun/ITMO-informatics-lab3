import re

schedule_xml = open(r"schedule.xml", encoding='utf-8').read()  # открываем xml файл для чтения
schedule_json = open("schedule.json", 'w', encoding='utf-8')  # открываем json файл для записи

re_tag_with_text_xml = r'<(\w+)>([\w \d.:,!?]+)<\/\w+>'  # шаблон для однострочных тегов с текстом
schedule_xml = re.sub(re_tag_with_text_xml, r'"\1": "\2"', schedule_xml)  # меняем формат однострочных тегов на JSON

re_tag_with_text_json = r'\"\w+\": \"[\w \d.:,!?]+\"'  # шаблон для поиска новых однострочных тегов
# шаблон для поиска тегов внутри, которых массив тегов
re_tag_with_array_of_tags = r'(\s+)<\w+>(\s+(?:' + re_tag_with_text_json + r'\s+)+)<\/\w+>'
schedule_xml = re.sub(re_tag_with_array_of_tags, r'\1{\2}', schedule_xml)  # превращаем эти массивы в JSON объекты

schedule_xml = re.sub(r'\"(\s+\")', r'",\1', schedule_xml)  # расставляем запятые между однострочными тегами
schedule_xml = re.sub(r'}(\s+{)', r'},\1', schedule_xml)  # расставляем запятые между объектами

# шаблон для поиска новых массивов
re_tag_with_array_of_json_objects = r'<(\w+)>(\s+({[\w\":,.\s]+},\s+)+{[\w\":,.\s]+}\s+)<\/\w+>'
schedule_xml = re.sub(re_tag_with_array_of_json_objects, r'"\1": [\2]', schedule_xml)

schedule_json.write('{\n')  # JSON файл должен начинаться и заканчиваться фигурными скобками
for s in schedule_xml.split('\n'):  # добавим табуляцию к каждой строчке
    schedule_json.write('\t' + s + '\n')
schedule_json.write('}')
