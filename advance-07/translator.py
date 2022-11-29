from datetime import datetime
import requests


def translate(text, url="translate.wiki.org/q=%s"):
    text = text.lower().strip()
    sentences = text.split("\n")
    responses = []

    for sentence in sentences:
        strip_sentence = sentence.strip()
        if not strip_sentence:
            continue

        resp = requests.get(url % sentence)
        responses.append(resp.text)

    return "\n".join(responses)


def is_ny():
    now = datetime.now()

    if now.month == 0 and now.day == 0:
        return "NY"

    return "Not NY"


def load_heavy_data(path):
    return {"1": 1, "2": 2}
