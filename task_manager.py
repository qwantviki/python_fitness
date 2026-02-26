import datetime

id = 0

def create_note(title: str, content: str, author: str) -> dict | None:
    """
    Сумка создает словарь заметок с автоматическим счетчиком id,
    а также указанием даты создания заметки
    :param title: название заметки
    :param content: суть заметки, ее содержание
    :param author: имя автора заметки
    :return: Заметку в виде словаря или None, если ошибка
    """
    global id
    id += 1
    if title == "" or author == "" or len(content) > 300:
        return None
    else:
        return {
            "id": id,
            "title": title,
            "content": content,
            "author": author,
            "created_at": datetime.datetime.now().isoformat(),
        }

note1 = create_note("Купить продукты", "Молоко, хлеб", "Иван")
print(note1)

note2 = create_note("Купить цветы", "Тюльпаны: красные и белые", "Виктор")
print(note2)

note3 = create_note("Заметка", "а" * 301, "Иван")
print(note3)