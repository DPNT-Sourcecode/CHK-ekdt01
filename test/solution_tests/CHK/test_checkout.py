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
        assert checkout('9') == -1

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

    def test_single_item_with_special(self):
        assert checkout('H') == 10
        assert checkout('HHHHH') == 45 
        assert checkout('HHHHHHHHHH') == 80 
        assert checkout('K') == 80
        assert checkout('KK') == 150 
        assert checkout('P') == 50
        assert checkout('PPPPP') == 200 
        assert checkout('Q') == 30
        assert checkout('QQQ') == 80 
        assert checkout('U') == 40
        assert checkout('UUU') == 120
        assert checkout('UUUU') == 120
        assert checkout('V') == 50
        assert checkout('VV') == 90 
        assert checkout('VVV') == 130 
        assert checkout('VVVV') == 180
        assert checkout('VVVVV') == 220

    def test_combined_specials(self):
        assert checkout('EEEEBBBB') == 40 * 4 + 45

    def test_multi_special_offers(self):
        assert checkout('STX') == 45
        assert checkout('YZS') == 45
        assert checkout('ZTS') == 45
        assert checkout('XTSXTS') == 90
        assert checkout('XTSXTSX') == 90 + 17
        assert checkout('XTSXTSXXX') == 90 + 17 + 45  

