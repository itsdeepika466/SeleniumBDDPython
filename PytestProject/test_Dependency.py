import pytest

class TestClass:

    @pytest.mark.dependency()   #passed
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])  #passed
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])   #failed
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login','TestClass::test_search' ]) #skipped
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])   #passed
    def test_logout(self):
        assert True


