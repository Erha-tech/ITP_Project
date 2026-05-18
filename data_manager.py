import json
import os

# Название файла, где будет храниться рекорд игрока
SCORE_FILE = "highscore.json"


def load_high_score():
    # Если файл с рекордом еще не создан, возвращаем 0
    if not os.path.exists(SCORE_FILE):
        return 0

    try:
        # Открываем файл для чтения
        with open(SCORE_FILE, "r") as file:
            # Загружаем данные из JSON-файла
            data = json.load(file)

            # Возвращаем сохраненный рекорд.
            # Если ключа "high_score" нет, возвращаем 0
            return data.get("high_score", 0)

    except (json.JSONDecodeError, IOError) as e:
        # Если файл поврежден или его не удалось прочитать
        print(f"Ошибка чтения файла: {e}")
        return 0


def save_high_score(score):
    try:
        # Открываем файл для записи.
        # Если файла нет, он будет создан автоматически
        with open(SCORE_FILE, "w") as file:
            # Сохраняем рекорд в JSON-формате
            json.dump({"high_score": score}, file)

    except Exception as e:
        # Если произошла ошибка при сохранении файла
        print(f"Ошибка сохранения файла: {e}")
