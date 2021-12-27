class TestRole:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, given_name):
        self.name = given_name


class TestAuthor:
    def __init__(self):
        self.top_role = None

    def get_top_role(self):
        return self.top_role

    def set_top_role(self, given_role):
        self.top_role = given_role


class TestMessage:
    def __init__(self):
        self.author = None

    def get_author(self):
        return self.author

    def set_author(self, given_author):
        self.author = given_author
