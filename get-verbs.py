import json

dictionary = json.load(open('Vietnamese-dictionary.json'))

verbs = {}
list_of_verbs = []
for item in dictionary:
    if item["grammatical-category"] == "động ngữ" or item["grammatical-category"] == "phụ ngữ":
        morph = item["morphology"]
        if len(morph.split()) > 1:
            continue
        if morph not in verbs:
            verbs[morph] = []
        verbs[morph].append({
            "meaning": item["meaning"],
            "synonym.paradigmatic": [],
            "synonym.syntagmatic": []
        })
        list_of_verbs.append(morph)

json.dump(verbs, open('verbs.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(list_of_verbs, open('list-of-verbs.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


