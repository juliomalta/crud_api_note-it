class Task:
  def __init__(self, id, title, description, status=False) -> None:
    self.id = id
    self.title = title
    self.description = description
    self.status = status

  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'description': self.description,
      "status": self.status
    }
# 'status': self.status