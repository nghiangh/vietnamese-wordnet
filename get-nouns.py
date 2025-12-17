import json

dictionary = json.load(open('Vietnamese-dictionary.json'))

nouns = {}
list_of_nouns = []
for item in dictionary:
    if item["grammatical-category"] == "danh ngữ":
        morph = item["morphology"]
        if len(morph.split()) > 1:
            continue
        if morph not in nouns:
            nouns[morph] = []
        nouns[morph].append({
            "meaning": item["meaning"],
            "synonym.paradigmatic": [],
            "synonym.syntagmatic": []
        })
        list_of_nouns.append(morph)

json.dump(nouns, open('nouns.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(list_of_nouns, open('list-of-nouns.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

