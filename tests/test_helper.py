import libraries.helper as hp


class TestMain:
    def test_password_is_empty(self):
        assert hp.password_is_valid('', 12, 6) is False

    def test_password_too_short(self):
        assert hp.password_is_valid('12345', 12, 6) is False

    def test_password_too_long(self):
        assert hp.password_is_valid('1234567891234', 12, 6) is False

    def test_password_invalid(self):
        assert hp.password_is_valid('my pass', 12, 6) is False

    def test_password_valid(self):
        assert hp.password_is_valid('1234567890', 12, 6) is True

    def test_username_valid(self):
        assert hp.username_is_valid('email@somewhere.com') is True
        assert hp.username_is_valid('email@somewhere.co.uk') is True
        assert hp.username_is_valid('email_123@somewhere.com') is True



