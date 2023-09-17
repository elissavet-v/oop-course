# create a class where one of its attributes is actually
# another custom type you define
# like a Tab class storing a Page object


class Page:
    def __init__(self, content):
        self.content = content


class Tab:
    def __init__(self, title, Page, current):
        self.title = title
        self.page = Page()
        self.current = current

    def show_page_number(self):
        print(f"The page number is {self.page}")


page1 = Page("fashion")
tab_1 = Tab("news", page1, True)
tab_1.show_page_number()
