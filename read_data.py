import json

import data


with open('data_goals.json', 'w',  encoding='utf-8') as w:
    json.dump(data.goals, w, ensure_ascii=False)

with open('data_teachers.json', 'w',  encoding='utf-8') as w2:
    json.dump(data.teachers, w2, ensure_ascii=False)
