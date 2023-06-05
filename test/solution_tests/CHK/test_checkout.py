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

        