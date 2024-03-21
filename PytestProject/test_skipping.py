import pytest

class TestClass:
    def test_methodA(self):
        print("Running method A")

    @pytest.mark.skip    #unconditional skip   
    def test_methodB(self):
        print("Running method B")

    def test_methodC(self):
        print("Running method C")

    def test_methodD(self):
        print("Running method D")



