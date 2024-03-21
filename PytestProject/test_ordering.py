import pytest

class TestClass:

    @pytest.mark.second
    def test_methodA(self):
        print("Running method A")

    @pytest.mark.third
    def test_methodB(self):
        print("Running method B")

    @pytest.mark.first
    def test_methodC(self):
        print("Running method C")

    @pytest.mark.fourth
    def test_methodD(self):
        print("Running method D")



