# Defina un schema Pydantic llamado Product con campos id (int), name (str) y
# precio (float)

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

telefono = Product(id=1, name='Teléfono', price=955.99)

print(telefono)

