from datetime import datetime

id = 0

def create_note(title: str, content: str, author: str) -> dict:
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
            "created_at": datetime.now().isoformat(),
        }

note1 = create_note("Купить продукты", "Молоко, хлеб", "Иван")
print(note1)

note2 = create_note("Заметка", "а" * 301, "Иван")
print(note2)