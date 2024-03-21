import pytest

class TestClass:
    @pytest.fixture()
    def setup(self):
        print("Launching browser..") #execute once before every test method
        yield
        print("Closing browser..")  #execute once after every test method

    def test_login(self,setup):
        print("This is login test")

    def test_Search(self,setup):
        print("This is Search test")

    def test_Advanceserach(self):
        print("This is Advance Search test")