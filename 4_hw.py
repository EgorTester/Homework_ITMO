class Rectangle:
    def __init__ (self, width, hight): self.w, self.h = width, hight
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

for w, h in [(7, 3), (10, 9), (2, 8)]:

    r = Rectangle(w, h)
    print(r.area(),r.perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

math = Math(7, 5)
math.addition()
math.multiplication()
math.division()
math.subtraction()


class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


button_texts = ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons", "Links", "Broken Links - Images",
                "Upload and Download", "Dynamic Properties"]

buttons = []
for text in button_texts:
    buttons.append(Button(text))

for button in buttons:
    print(button.text)

for button in buttons:
    print(button.click())