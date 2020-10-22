from unittest import TestCase, main

from ..business.expression import Expression

class ExpressionTests(TestCase):

    def test_addition(self):
        expression = Expression()
        expression.append_digit(2)
        expression.append_operator(Expression.Operator.ADDITION)
        expression.append_digit(2)
        self.assertEqual(2 + 2, expression.compute())

    def test_append_operator_wrong_type(self):
        expression = Expression("2 + 2")
        with self.assertRaises(TypeError):
            expression.append_operator("+")

    def test_append_operator_expression_is_empty(self):
        expression = Expression("")
        with self.assertRaises(ValueError):
            expression.append_operator(Expression.Operator.SUBSTRACTION)

    def test_append_operator_expression_ends_with_operator(self):
        expression = Expression("2 + 2 *")
        with self.assertRaises(ValueError):
            expression.append_operator(Expression.Operator.SUBSTRACTION)

    def test_append_operator_expression_twice_in_a_row(self):
        expression = Expression("2 + 2")
        with self.assertRaises(ValueError):
            expression.append_operator(Expression.Operator.SUBSTRACTION)
            expression.append_operator(Expression.Operator.ADDITION)

    def test_append_operator_expression_ends_with_member(self):
        expression = Expression("2 + 2")
        expression.append_operator(Expression.Operator.MULTIPLICATION)
        self.assertEqual("2 + 2 *", expression.value())

    def test_append_digit_wrong_type(self):
        expression = Expression("2 +")
        with self.assertRaises(TypeError):
            expression.append_digit("2")

    def test_append_digit_negative_digit(self):
        expression = Expression("2 +")
        with self.assertRaises(ValueError):
            expression.append_digit(-2)

    def test_append_digit_multiple_digits_integer(self):
        expression = Expression("2 +")
        with self.assertRaises(ValueError):
            expression.append_digit(22)

    def test_append_digit_after_operator(self):
        expression = Expression("2 +")
        expression.append_digit(2)
        self.assertEqual(expression.value(), "2 + 2")

    def test_append_digit_after_another_digit(self):
        expression = Expression("2")
        expression.append_digit(2)
        self.assertEqual(expression.value(), "22")

    def test_compute_empty_expression(self):
        expression = Expression("")
        with self.assertRaises(ValueError):
            expression.compute()

    def test_compute_one_member(self):
        expression = Expression("2 +")
        with self.assertRaises(ValueError):
            expression.compute()

    def test_compute_operators_only(self):
        expression = Expression("* / +")
        with self.assertRaises(ValueError):
            expression.compute()

    def test_compute_two_one_digit_members_addition(self):
        expression = Expression("2 + 2")
        self.assertEquals(4, expression.compute())

    def test_compute_two_multiple_digit_members_multiplication(self):
        expression = Expression("12 * 64")
        self.assertEquals(768, expression.compute())

    def test_compute_three_multiple_digit_members_multiplication(self):
        expression = Expression("12 * 64 + 12")
        self.assertEquals(768 + 12, expression.compute())

    def test_is_empty_empty_expression(self):
        expression = Expression("")
        self.assertTrue(expression._Expression__is_empty())

    def test_is_empty_not_an_empty_expression(self):
        expression = Expression("2")
        self.assertFalse(expression._Expression__is_empty())

    def test_ends_with_operator_ends_with_addition(self):
        expression = Expression("12 * 64 + 12 +")
        self.assertTrue(expression._Expression__ends_with_operator())

    def test_ends_with_operator_ends_with_substraction(self):
        expression = Expression("12 * 64 + 12 -")
        self.assertTrue(expression._Expression__ends_with_operator())

    def test_ends_with_operator_ends_with_division(self):
        expression = Expression("12 * 64 + 12 /")
        self.assertTrue(expression._Expression__ends_with_operator())

    def test_ends_with_operator_ends_with_multiplication(self):
        expression = Expression("2 + 2 *")
        self.assertTrue(expression._Expression__ends_with_operator())

    def test_ends_with_operator_ends_with_digit(self):
        expression = Expression("12 * 64 + 12")
        self.assertFalse(expression._Expression__ends_with_operator())

    def test_ends_with_operator_expression_is_empty(self):
        expression = Expression("")
        self.assertFalse(expression._Expression__ends_with_operator())

    def test_ends_with_digit_one_digit(self):
        expression = Expression("2")
        self.assertTrue(expression._Expression__ends_with_digit())

    def test_ends_with_digit_simple_addition(self):
        expression = Expression("2 + 2")
        self.assertTrue(expression._Expression__ends_with_digit())

    def test_ends_with_digit_ends_with_operator(self):
        expression = Expression("2 + 2 *")
        self.assertFalse(expression._Expression__ends_with_digit())

    def test_ends_with_digit_empty_expression(self):
        expression = Expression("")
        self.assertFalse(expression._Expression__ends_with_digit())

if __name__ == "__main__":
    main()