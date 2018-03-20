
from nearly_equal import nearly_eq


class TestClass():
    def test_insertion1(self):
        assert nearly_eq("jack","jacky") == True

    def test_insertion2(self):
        assert nearly_eq("snow","snowy") == True

    def test_insertion3(self):
        assert nearly_eq("python","pyithon") == True

    def test_insertion_false(self):
        assert nearly_eq("pearl","ruby") == False

    def test_replacing1(self):
        assert nearly_eq("python","pithon") == True

    def test_replacing2(self):
        assert nearly_eq("perl","peel") == True

    def test_replacing3(self):
        assert nearly_eq("cheif","theif") == True

    def test_replacing_false(self):
        assert nearly_eq("kite","kitty") == False

    def test_deleting1(self):
        assert nearly_eq("joel","joe") == True

    def test_deleting2(self):
        assert nearly_eq("window","widow") == True

    def test_deleting1(self):
        assert nearly_eq("harrypotter","arrypotter") == True

    def test_deleting_false(self):
        assert nearly_eq("woman","man") == False

    def test_other1(self):
        assert nearly_eq("burger","burgler") == True

    def test_other2(self):
        assert nearly_eq("beach","leach") == True

    def test_other3(self):
        assert nearly_eq("dumbledore","bumbledore") == True

    def test_other4(self):
        assert nearly_eq("apple","appler") == True
