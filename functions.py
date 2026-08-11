import random
import json

def findCaseById(id):
    with open('cases.json', 'r', encoding="utf-8") as f:
        cases = json.load(f)
    for case in cases["cases"]:
        if case["id"] == id:
            return case
    return None

def findItemById(id):
    with open('items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    for item in items['items']:
        if item["id"] == id:
            return item
    return None

def openCase(caseId):
    Case = findCaseById(caseId)
    ticket = random.randint(1, 1_000_000)
    for i in Case["items"]:
        if i["ticket_min"] <= ticket <= i["ticket_max"]:
            result = {"drop_item": findItemById(i["item_id"]), "ticket": ticket}
            return result



