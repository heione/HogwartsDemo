import unittest


class Search:

    def search_func(self, info):
        print(info)


class TestDemoOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_a(self):
        self.search.search_func("aaaaaaaaaaaaaaaa")

    def test_b(self):
        print("bbbbbbbbbbbbbb")


class TestDemoTwo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("TestDemoTwo set up class")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls):
        print("TestDemoTwo tear down class")

    def setUp(self) -> None:
        print("TestDemoTwo setUp")

    def tearDown(self):
        print("TestDemoTwo tearDown")

    def test_a(self):
        self.search.search_func("TestDemoTwo aaaaaaaaaaaaaaaa")

    def test_b(self):
        print("TestDemoTwo bbbbbbbbbbbbbb")


if __name__ == '__main__':
    unittest.main()
