class Rectangle:
    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        p = 2 * self.width + 2 * self.height
        return p

    def get_diagonal(self):
        d = (self.width ** 2 + self.height ** 2) ** 0.5
        return d

    def get_picture(self):
        rows = self.height
        columns = self.width
        list_rows = []
        if rows > 50 or columns > 50:
            return "Too big for picture."

        for i in range(rows):
            line = ""
            for a in range(columns):
                line = line + "*"
            line = line + "\n"
            list_rows.append(line)
        lines = "".join(list_rows)

        return lines

    def get_amount_inside(self, shape):
        eval_width = shape.width
        eval_height = shape.height

        if eval_height > self.height or eval_width > self.width:
            return 0

        times_width = self.width // eval_width
        times_height = self.height // eval_height
        can_fit = times_height * times_width

        return can_fit

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(width=side, height=side)

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side

    def set_height(self, new_side):
        self.height = new_side
        self.width = new_side

    def set_width(self, new_side):
        self.height = new_side
        self.width = new_side

    def __str__(self) -> str:
        return f"Square(side={self.width})"


rect = Rectangle(3, 6)
sq = Square(5)
rect.set_height(10)
rect.set_width(15)
actual = rect.get_amount_inside(sq)
expected = 6
