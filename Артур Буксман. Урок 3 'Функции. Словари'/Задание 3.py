# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }

def thesaurus(name):
    letter_dict = {
        "И": ["Иван", "Илья"],
        "К": ["Кирилл", "Константин"],
        "Л": ["Леонид", "Лев"],
        "М": ["Мария"],
        "П": ["Петр"]
    }
    for k, v in letter_dict.items():
        for i in v:
            if i == name:
                return {k: v}


print(thesaurus("Леонид"))
