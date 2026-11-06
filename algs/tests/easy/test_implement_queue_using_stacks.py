import unittest

from algs.easy.implement_queue_using_stacks import MyQueue


class TestImplementQueueUsingStacks(unittest.TestCase):
    def test_push_peek_pop_and_empty_sequence(self):
        queue = MyQueue()

        self.assertIsNone(queue.push(1))
        self.assertIsNone(queue.push(2))
        self.assertEqual(queue.peek(), 1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.pop(), 1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.pop(), 2)
        self.assertTrue(queue.empty())


if __name__ == "__main__":
    unittest.main()
