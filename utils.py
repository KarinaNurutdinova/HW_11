import json


def load_candidates_from_json(file):
    """возвращает список всех кандидатов"""
    with open(file, "r") as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    with open("candidates.json", "r") as file:
        data = json.load(file)
        for candidate in data:
            if candidate["id"] == int(candidate_id):
                return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    with open("candidates.json", "r") as file:
        data = json.load(file)
        candidates = []
        for candidate in data:
            if candidate_name in candidate["name"]:
                candidates.append(candidate)
        return candidates


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    with open("candidates.json", "r") as file:
        data = json.load(file)
        candidates = []
        for candidate in data:
            candidate_skill = candidate["skills"].lower()
            skills = candidate_skill.split(", ")
            if skill_name.lower() in skills:
                candidates.append(candidate)
    return candidates
