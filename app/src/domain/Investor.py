import typing as t

class Investor():
    def __init__(self, name: str, address: t.Optional[str], status: str, id: int = -1):
        self.id = id
        self.name = name
        self.address = address
        self.status = status

    def __str__(self): 
        return f'[id: {self.id}, name: {self.name}, address: {self.address}, status: {self.status}]'