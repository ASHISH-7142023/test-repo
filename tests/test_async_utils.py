"""Unit tests for asynchronous concurrency control and batching utilities."""

import asyncio
import unittest
from src.async_utils import gather_with_concurrency, batch_process


class TestAsyncUtils(unittest.TestCase):

    def test_gather_with_concurrency(self):
        async def run_test():
            active_count = 0
            max_active = 0

            async def mock_coro(val):
                nonlocal active_count, max_active
                active_count += 1
                max_active = max(max_active, active_count)
                await asyncio.sleep(0.01)
                active_count -= 1
                return val * 2

            results = await gather_with_concurrency(2, *(mock_coro(i) for i in range(5)))
            self.assertEqual(results, [0, 2, 4, 6, 8])
            self.assertLessEqual(max_active, 2)

        asyncio.run(run_test())

    def test_batch_process(self):
        async def run_test():
            async def process_batch(items):
                return sum(items)

            data = list(range(10))
            results = await batch_process(data, batch_size=3, async_fn=process_batch)
            # Batches: [0,1,2] -> 3, [3,4,5] -> 12, [6,7,8] -> 21, [9] -> 9
            self.assertEqual(results, [3, 12, 21, 9])

        asyncio.run(run_test())


if __name__ == "__main__":
    unittest.main()
