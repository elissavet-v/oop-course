class Page:
    """Just a demo class with some arbitrary attribute"""

    def __init__(self, some_attribute: int):
        self.some_attribute = some_attribute


class Tab:
    """A Tab class that contains a page (by means of composition) of class Page
    and some other attributes. The page attribute is added with a technique called
    dependency injection."""

    def __init__(self, title: str, is_current: bool, page: Page):
        self.title = title
        self.is_current = is_current
        self.page = page

    def close(self):
        """Close the tab"""
        print("Closing tab")

    def reload(self):
        """Reload the tab"""
        print("Reloading tab")


# Now we instantiate a Tab object with a Page object

my_fabulous_page = Page(42)
my_fabulous_tab = Tab("My Fabulous Tab", True, my_fabulous_page)

# Or in one line
my_other_fabulous_tab = Tab("My Other Fabulous Tab", False, Page(43))

# Now we can access the page attribute of the two Tab object instances
print(my_fabulous_tab.page.some_attribute)
print(my_other_fabulous_tab.page.some_attribute)
