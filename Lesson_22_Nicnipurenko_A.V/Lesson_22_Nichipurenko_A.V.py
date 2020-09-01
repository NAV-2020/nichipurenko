"""
class Star:
    def __init__(self, name: str, galaxy: str):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return f"Star{self.name} in {self.galaxy}"

    def __repr__(self):
        retern f"Name:{self.name} Galaxy:{self.galaxy}"

sum = Star("Sum", galaxy="Milky Way")
print(sum)
#print(repr(sum))
"""


