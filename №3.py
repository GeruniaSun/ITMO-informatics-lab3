schedule_xml = open(r"schedule.xml", encoding='utf-8').read().split('\n')  # открываем xml файл для чтения
schedule_json = open("schedule.json", 'w', encoding='utf-8')  # открываем json файл для записи
schedule_json.write('[\n')  # расписание - массив уроков, поэтому начнем и закончим файл квадратной скобкой
schedule_xml.pop(0)  # первая строка xml файла - корневой тег, удалим за ненадобностью
for word in schedule_xml:
    # находим и удаляем закрывающие теги
    if '/' in word:
        word = word[:word.find('/') - 1]
    # меняем xml теги на json теги
    word = word.replace('<', '"').replace('>', '":')
    # ставим фигурную скобку в начале блока
    if len(word) > 0 and word[-1] == ':':  #
        word = '\t{'
    # помещаем текст в тегах в кавычки
    if ':' in word and len(word[word.find(':') + 1:]) > 0:
        word = word[:word.find(':') + 1] + ' "' + word[word.find(':') + 1:] + '",'
    # убираем запятую и ставим фигурную скобку в конце блока
    if len(word) > 0 and word[-1] == ' ':
        schedule_json.seek(schedule_json.tell() - 3)
        schedule_json.write('\n')
        word += '},'
    schedule_json.write(word + '\n')  # записываем отформатированную строку в файл
schedule_json.seek(schedule_json.tell() - 5)  # убираем последнюю запятую
schedule_json.write('\n]')  # конец массива
