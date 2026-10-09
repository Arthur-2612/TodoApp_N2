class Todo:
    def __init__(self, id: int, title: str, description: str = "", completed: bool = True):
        if not title or not title.strip():
            raise ValueError("The title cannot be empty or whitespace.")
        
        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
