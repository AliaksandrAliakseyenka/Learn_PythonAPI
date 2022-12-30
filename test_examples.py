class TestExample:

    def test_check_math_sum(self):
        a = 4
        c = 10
        except_sum = 14
        assert a + c == except_sum, f"Sum of var a and b it not equal to {except_sum}"

    def test_check_math_sum2(self):
        a = 5
        c = 10
        except_sum = 14
        assert a + c == except_sum, f"Sum of var a and b it not equal to {except_sum}"
