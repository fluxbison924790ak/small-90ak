"""tiny responsive component library."""
from shutil import get_terminal_size

class Component:
    def render(self, width):
        return ""

class Label(Component):
    def __init__(self, text):
        self.text = text
    def render(self, width):
        return self.text

class Button(Component):
    def __init__(self, label):
        self.label = label
    def render(self, width):
        return f"[ {self.label} ]"

class Container(Component):
    def __init__(self, *children):
        self.children = children
    def render(self, width):
        lines = []
        cur = ""
        for child in self.children:
            s = child.render(width)
            if len(cur) + len(s) + (1 if cur else 0) > width:
                lines.append(cur.rstrip())
                cur = s
            else:
                cur += (" " if cur else "") + s
        if cur:
            lines.append(cur.rstrip())
        return "\n".join(lines)

if __name__ == "__main__":
    w = get_terminal_size().columns
    container = Container(
        Label("Hello"),
        Button("Click"),
        Label("World"),
        Button("Exit")
    )
    print(container.render(w))