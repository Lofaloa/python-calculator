from unittest import TestCase, main

from ..business.expression import Expression

class ExpressionTests(TestCase):

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
        self.assertEquals("2 + 2 *", expression.value())

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

if __name__ == "__main__":
    main()