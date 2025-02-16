from model.rectangle import Rectangle

# fake data, replaced in Chapter 10 by a real database and SQL
_rectangles [
    Rectangle(name="Claude Hande",
             country="FR",
             description="Scarce during full moons"),
    Rectangle(name="Noah Weiser",
             country="DE",
             description="Myopic machete man"),
    ]

def get_all() -> list[Rectangle]:
    """Return all explorers"""
    return _rectangles

def get_two(width: float, height: float) -> Rectangle |None:
    for _rectangle in _rectangles:
        if _rectangle.width == width & _rectangle.height == height:
            return _rectangle
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorers list:
def create(rectangle: Rectangle) -> Rectangle:
    """Add an explorer"""
    return rectangle

def modify(rectangle: Rectangle) -> Rectangle:
    """Partially modify an explorer"""
    return rectangle

def replace(rectangle: Rectangle) -> Rectangle:
    """Completely replace an explorer"""
    return rectangle

def delete(width: float) -> bool:
    """Delete an explorer; return None if it existed"""
    return None

def delete(height: float) -> bool:
    """Delete an explorer; return None if it existed"""
    return None