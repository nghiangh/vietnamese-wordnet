import json

dictionary = json.load(open('Vietnamese-dictionary.json'))

verbs = {}
for item in dictionary:
    if item["grammatical-category"] == "động ngữ" or item["grammatical-category"] == "phụ ngữ":
        morph = item["morphology"]
        if morph not in verbs:
            verbs[morph] = []
        verbs[morph].append({
            "meaning": item["meaning"],
            "synonym.paradigmatic": [],
            "synonyms.syntagmatic": []
        })

json.dump(verbs, open('verbs.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

