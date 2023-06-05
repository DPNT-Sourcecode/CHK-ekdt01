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

    def test_multiple_items(self):
        assert checkout('AAA') == 130
        assert checkout('AAAAA') == 200
        assert checkout('AAAAAAAAA') == 380
        assert checkout('CCCC') == 80
        assert checkout('DD') == 30
        assert checkout('EEEE') == 120

    def test_invalid(self):
        assert checkout('Z') == -1

        