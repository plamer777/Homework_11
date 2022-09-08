"""This unit provides all logic to run Flask app"""
import json
# -------------------------------------------------------------------------


def load_json_data(filename: str) -> list:
    """The function loads all candidates from json file.

    :param filename: The name of json file

    Returns:
        candidates: The list of dicts with candidates data
    """

    try:
        with open(filename, encoding="utf-8") as fin:

            candidates = json.load(fin)

        return candidates

    except Exception:
        print(f'Не удалось загрузить данные из файла {filename}')
        return []


def get_candidate_by_id(user_id: int, candidate_list: list) -> dict:
    """The function returns candidate finding by his user_id or empty dict
    instead.

    :param user_id: The id to find candidate by.
    :param candidate_list: The list with candidates' data.

    Returns:
        candidate - The dict with candidate's data
    """
    try:
        candidate = [data for data in candidate_list if data['id'] ==
                     user_id][0]

    except Exception:
        candidate = {}

    return candidate


def get_candidates_by_name(name: str, candidate_list: list) -> list:
    """The function returns candidates finding by his name or empty list
        instead.

    :param name: A name to find candidate by.
    :param candidate_list: A list with candidates' data.

    Returns:
        candidate - The dict with candidate's data
        """
    try:
        candidates = [data for data in candidate_list if name.lower() in
                      data['name'].lower()]

    except Exception:
        candidates = []

    return candidates


def get_candidates_by_skill(skill: str, candidate_list: list) -> list:
    """The function returns candidates list finding by his skills or empty list
            instead.

    :param skill: A skill to find candidate by.
    :param candidate_list: A list with candidates' data.

    Returns:
        candidates - The dict with candidate's data
    """
    try:
        candidates = [data for data in candidate_list if skill.lower() in
                      data['skills'].lower().split(', ')]

    except Exception:
        candidates = []

    return candidates
