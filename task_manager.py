import datetime

id = 0

class Note:
    def __init__(self, title, content, author):
        self.id = None
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.datetime.now().isoformat()

    def is_valid(self) -> bool:
        if self.title == "" or len(self.content) > 300 or self.author == "":
            return False
        else:
            return True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_at": self.created_at
        }

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

# note1 = create_note("Купить продукты", "Молоко, хлеб", "Иван")
# print(note1)
#
# note2 = create_note("Купить цветы", "Тюльпаны: красные и белые", "Виктор")
# print(note2)
#
# note3 = create_note("Заметка", "а" * 301, "Иван")
# print(note3)

# Создаем два объекта
note1 = Note("Купить продукты", "Молоко, хлеб", "Иван")
note2 = Note("", "Контент", "Петр")  # Пустой заголовок

# Проверяем валидацию
print(note1.is_valid())  # True
print(note2.is_valid())  # False

# Преобразуем в словарь (только если заметка валидна, но метод должен работать всегда)
print(note1.to_dict())
# Вывод: {'id': None, 'title': 'Купить продукты', 'content': 'Молоко, хлеб', 'author': 'Иван', 'created_at': '2026-02-28T12:00:00.123456'}

print(note2.to_dict())
# Вывод: {'id': None, 'title': '', 'content': 'Контент', 'author': 'Петр', 'created_at': '2026-02-28T12:00:01.123456'}