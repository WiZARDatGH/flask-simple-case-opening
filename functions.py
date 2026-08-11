import random
import json

def findCaseById(id):
    with open('cases.json', 'r', encoding="utf-8") as f:
        cases = json.load(f)
    for case in cases["cases"]:
        if case["id"] == id:
            return case


def openCase(caseId):
    Case = findCaseById(caseId)
    ticket = random.randint(1, 1_000_000)
    for i in Case["items"]:
        if i["ticket_min"] <= ticket <= i["ticket_max"]:
            result = {"drop_item": i, "ticket": ticket}
            return result



