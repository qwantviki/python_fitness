import datetime
import json
from tkinter.ttk import Notebook


# id = 0


class Note:
    """
    Класс заметок с заголовками, содержанием и автором
    """
    def __init__(self, title: str, content: str, author: str) -> None:
        self.id = None
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.datetime.now().isoformat()

    def is_valid(self) -> bool:
        """
        Проверка на правильность заполнения:
        title и author не пустые, а длина содержимого не более 300 символов.
        :return: Bool
        """
        if self.title == "" or len(self.content) > 300 or self.author == "":
            return False
        else:
            return True

    def to_dict(self) -> dict:
        """
        Возвращает объект класса в виде словаря
        :return: dict
        """
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_at": self.created_at
        }


class Notebook:
    """
    Класс представляет собой коллекцию заметок.
    Автоматически присваивает номер новой заметке.
    """
    def __init__(self):
        self._next_id = 1
        self.notes_list = []

    def add_note(self, title: str, content: str, author: str) -> Note | None:
        """
        Добавляет новую заметку в коллекцию.
        Перед добавлением проверяет на правильность заполнения.
        :param title: название заметки
        :param content: содержание заметки
        :param author: автор заметки
        :return: возвращает либо новую заметку, либо ничего
        """
        note = Note(title, content, author)
        if note.is_valid():
            note.id = self._next_id
            self._next_id += 1
            self.notes_list.append(note)
            return note
        else:
            return None

    def get_all_notes(self) -> list[Note]:
        """
        Получение полного списка заметок
        :return: возвращает список добавленных заметок
        """
        return self.notes_list

    def find_by_author(self, author: str) -> list[Note] | None:
        """
        Ищет все заметки указанного автора.
        :param author: имя автора
        :return: возвращает либо список заметок, либо ничего.
        """
        found_notes = []
        for note in self.notes_list:
            if author == note.author:
                found_notes.append(note)
        if len(found_notes) == 0:
            return None
        else:
            return found_notes

    def delete_note(self, note_id: int) -> bool:
        """
        Функция удаления заметки с заданным id.
        :param note_id: номер по порядку заметки
        :return: возвращает true в случае удаления
        """
        for note in self.notes_list:
            if note.id == note_id:
                self.notes_list.remove(note)
                return True
        return False

    def save_to_file(self, filename: str) -> None:
        """
        Сохраняет список заметок в JSON файл
        :param filename: путь к файлу
        :return: ничего, просто сохраняет данные
        """
        notes_to_save = []
        for note in self.notes_list:
            notes_to_save.append(note.to_dict())
        with open(filename, "w") as file:
            json.dump(notes_to_save, file)

    def load_from_file(self, filename: str) -> None:
        """
        Из списка словарей создает заметку по каждому
        :param filename: путь к файлу
        :return: None
        """
        self.notes_list = []
        with open(filename, "r") as file:
            data = json.load(file)
        for note in data:
            self.add_note(note["title"], note["content"], note["author"])

# def create_note(title: str, content: str, author: str) -> dict | None:
#     """
#     Сумка создает словарь заметок с автоматическим счетчиком id,
#     а также указанием даты создания заметки
#     :param title: название заметки
#     :param content: суть заметки, ее содержание
#     :param author: имя автора заметки
#     :return: Заметку в виде словаря или None, если ошибка
#     """
#     global id
#     id += 1
#     if title == "" or author == "" or len(content) > 300:
#         return None
#     else:
#         return {
#             "id": id,
#             "title": title,
#             "content": content,
#             "author": author,
#             "created_at": datetime.datetime.now().isoformat(),
#         }

# note1 = create_note("Купить продукты", "Молоко, хлеб", "Иван")
# print(note1)
#
# note2 = create_note("Купить цветы", "Тюльпаны: красные и белые", "Виктор")
# print(note2)
#
# note3 = create_note("Заметка", "а" * 301, "Иван")
# print(note3)

# Создаем два объекта
# note1 = Note("Купить продукты", "Молоко, хлеб", "Иван")
# note2 = Note("", "Контент", "Петр")  # Пустой заголовок
#
# # Проверяем валидацию
# print(note1.is_valid())  # True
# print(note2.is_valid())  # False
#
# # Преобразуем в словарь (только если заметка валидна, но метод должен работать всегда)
# print(note1.to_dict())
# # Вывод: {'id': None, 'title': 'Купить продукты', 'content': 'Молоко, хлеб', 'author': 'Иван', 'created_at': '2026-02-28T12:00:00.123456'}
#
# print(note2.to_dict())
# Вывод: {'id': None, 'title': '', 'content': 'Контент', 'author': 'Петр', 'created_at': '2026-02-28T12:00:01.123456'}

# # Создаем записную книжку
# notebook = Notebook()
#
# # Добавляем заметки
# note1 = notebook.add_note("Купить продукты", "Молоко, хлеб", "Иван")
# note2 = notebook.add_note("", "Пустой заголовок", "Петр")  # Невалидная
# note3 = notebook.add_note("Заметка 2", "Какой-то контент", "Иван")
#
# print(f"Всего заметок: {len(notebook.get_all_notes())}")  # Должно быть 2
# print(f"ID первой заметки: {note1.id}")  # Должно быть 1
# print(f"ID третьей заметки: {note3.id}")  # Должно быть 2
#
# # Поиск по автору
# ivan_notes = notebook.find_by_author("Иван")
# print(f"Заметок у Ивана: {len(ivan_notes)}")  # Должно быть 2
#
# # Удаление
# notebook.delete_note(1)
# print(f"Осталось заметок: {len(notebook.get_all_notes())}")  # Должно быть 1

# Создаем и наполняем заметками
notebook = Notebook()
notebook.add_note("Купить продукты", "Молоко, хлеб", "Иван")
notebook.add_note("Заметка 2", "Какой-то контент", "Иван")
notebook.add_note("Список книг", "1984, Скотный двор", "Петр")

# Сохраняем
notebook.save_to_file("notes.json")
print("Заметки сохранены")

# Создаем новую пустую записную книжку
notebook2 = Notebook()
print(f"Заметок до загрузки: {len(notebook2.get_all_notes())}")  # 0

# Загружаем
notebook2.load_from_file("notes.json")
print(f"Заметок после загрузки: {len(notebook2.get_all_notes())}")  # 3

# Проверяем ID и следующий счетчик
print(f"ID загруженных заметок: {[note.id for note in notebook2.get_all_notes()]}")
# Должно быть [1, 2, 3]

# Добавляем новую заметку в загруженную книжку
note4 = notebook2.add_note("Новая заметка", "После загрузки", "Иван")
print(f"ID новой заметки: {note4.id}")  # Должно быть 4