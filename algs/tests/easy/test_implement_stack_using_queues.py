import unittest

from algs.easy.implement_stack_using_queues import MyStack


class TestImplementStackUsingQueues(unittest.TestCase):
    def test_push_top_pop_and_empty_sequence(self):
        stack = MyStack()

        self.assertIsNone(stack.push(1))
        self.assertIsNone(stack.push(2))
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())


if __name__ == "__main__":
    unittest.main()
