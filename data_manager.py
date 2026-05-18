import json
import os

# Файл для сохранения рекорда
SCORE_FILE = "highscore.json"


def load_high_score():
    """
    Загружает рекорд из JSON-файла.
    Если файл отсутствует или поврежден — возвращает 0.
    """
    if not os.path.exists(SCORE_FILE):
        return 0

    try:
        with open(SCORE_FILE, "r") as file:
            data = json.load(file)
            return data.get("high_score", 0)

    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка чтения файла: {e}")
        return 0


def save_high_score(score):
    """
    Сохраняет новый рекорд в JSON-файл.
    """
    try:
        with open(SCORE_FILE, "w") as file:
            json.dump({"high_score": score}, file)

    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")
