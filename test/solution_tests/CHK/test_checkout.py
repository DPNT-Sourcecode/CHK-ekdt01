from solutions.CHK import checkout

class TestCheckout():
    def test_empty_order(self):
        assert checkout('') == 0

    def test_single_item(self):
        assert checkout('A') == 50
        assert checkout('B') == 30
        assert checkout('C') == 20
        assert checkout('D') == 15
        assert checkout('E') == 40
        assert checkout('F') == 10
        assert checkout('G') == 20
        assert checkout('I') == 35
        assert checkout('J') == 60
        assert checkout('L') == 90
        assert checkout('M') == 15
        assert checkout('O') == 10
        assert checkout('S') == 30
        assert checkout('T') == 20
        assert checkout('W') == 20
        assert checkout('X') == 90
        assert checkout('Y') == 10
        assert checkout('Z') == 50

    def test_multiple_items(self):
        assert checkout('AAA') == 130
        assert checkout('AAAAA') == 200
        assert checkout('AAAAAAAAA') == 380
        assert checkout('CCCC') == 80
        assert checkout('DD') == 30
        assert checkout('EEEE') == 160

    def test_invalid(self):
        assert checkout('Z') == -1

    def test_free_items(self):
        assert checkout('EEB') == 80
        assert checkout('EEEB') == 120
        assert checkout('EEEEBB') == 160

    def test_multiple_fs(self):
        assert checkout('FF') == 20
        assert checkout('FFF') == 20
        assert checkout('FFFF') == 30
        assert checkout('FFFFF') == 40
        assert checkout('FFFFFF') == 40

    def test_multiple_different_items_with_F(self):
        assert checkout('ABCF') == 50 + 30 + 20 + 10
        assert checkout('ABCDEFFF') == 50 + 30 + 20 + 15 + 40 + 20
