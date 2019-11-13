import pytest


class TestContact:

    def test_login(self):
        print("123")


    def test_login1(self):
        print("123")



    def test_login2(self):
        print("123")

        assert 0
if __name__ == '__main__':
    # pytest.main("-s login.py")
    pytest.main(["-s",  "test.py"])
