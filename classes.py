# Classes

class Task:
     # Class attribute (shared by all instances)
    STATUS_CHOICES = ("todo", "doing", "done")

    def __init__(self, title: str, status: str = "todo"):
        self.title = title            # instance attribute
        self._status = "todo"         # private instance attribute
         # Validate and set status using the property setter
        self.status = status            # goes through the setter

    @property
    def status(self) -> str:   
        return self._status     

    @status.setter
    def status(self, value: str) -> None:   
        if value not in self.STATUS_CHOICES:
            raise ValueError(f"status must be one of {self.STATUS_CHOICES}")
        self._status = value
    def mark_done(self) -> None:
        self.status = "done"

    def summary(self) -> str:
        return f"[{self.status.upper()}] {self.title}"
    


# Example usage
t = Task("Buy milk")
print(t.summary())       # [TODO] Buy milk
t.mark_done()
print(t.summary())       # [DONE] Buy milk


