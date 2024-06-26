import xmltodict
import json


def translation(s):  # функция перевода для корректного отображения кириллицы
    dict_utf = {
        'u0410': 'А', 'u0430': 'а',
        'u0411': 'Б', 'u0431': 'б',
        'u0412': 'В', 'u0432': 'в',
        'u0413': 'Г', 'u0433': 'г',
        'u0414': 'Д', 'u0434': 'д',
        'u0415': 'Е', 'u0435': 'е',
        'u0401': 'Ё', 'u0451': 'ё',
        'u0416': 'Ж', 'u0436': 'ж',
        'u0417': 'З', 'u0437': 'з',
        'u0418': 'И', 'u0438': 'и',
        'u0419': 'Й', 'u0439': 'й',
        'u041a': 'К', 'u043a': 'к',
        'u041b': 'Л', 'u043b': 'л',
        'u041c': 'М', 'u043c': 'м',
        'u041d': 'Н', 'u043d': 'н',
        'u041e': 'О', 'u043e': 'о',
        'u041f': 'П', 'u043f': 'п',
        'u0420': 'Р', 'u0440': 'р',
        'u0421': 'С', 'u0441': 'с',
        'u0422': 'Т', 'u0442': 'т',
        'u0423': 'У', 'u0443': 'у',
        'u0424': 'Ф', 'u0444': 'ф',
        'u0425': 'Х', 'u0445': 'х',
        'u0426': 'Ц', 'u0446': 'ц',
        'u0427': 'Ч', 'u0447': 'ч',
        'u0428': 'Ш', 'u0448': 'ш',
        'u0429': 'Щ', 'u0449': 'щ',
        'u042a': 'Ъ', 'u044a': 'ъ',
        'u042b': 'Ы', 'u044b': 'ы',
        'u042c': 'Ь', 'u044c': 'ь',
        'u042d': 'Э', 'u044d': 'э',
        'u042e': 'Ю', 'u044e': 'ю',
        'u042f': 'Я', 'u044f': 'я',
    }
    for k, v in dict_utf.items():
        s = s.replace('\\' + k, v)
    return s


dict_from_xml = xmltodict.parse(open(r"schedule.xml", encoding='utf-8').read())  # переводим xml-файл в словарь
json_from_dict = json.dumps(dict_from_xml, indent=4)  # делаем строку формата json из словаря

open("schedule.json", 'w', encoding='utf-8').write(translation(json_from_dict))
