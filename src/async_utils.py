"""Asynchronous concurrency controls, semaphore-bounded execution, and task helpers."""

import asyncio
from typing import Any, Callable, Coroutine, Iterable, List, TypeVar

T = TypeVar("T")


async def gather_with_concurrency(concurrency: int, *tasks: Coroutine[Any, Any, T]) -> List[T]:
    """Execute multiple coroutines concurrently with a maximum active semaphore limit."""
    if concurrency <= 0:
        raise ValueError("Concurrency limit must be greater than zero.")
    semaphore = asyncio.Semaphore(concurrency)

    async def sem_task(task: Coroutine[Any, Any, T]) -> T:
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def batch_process(items: Iterable[Any], batch_size: int, async_fn: Callable[[List[Any]], Coroutine[Any, Any, T]]) -> List[T]:
    """Process an iterable in chunks of batch_size through an async callback."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive.")
    results = []
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == batch_size:
            res = await async_fn(chunk)
            results.append(res)
            chunk = []
    if chunk:
        res = await async_fn(chunk)
        results.append(res)
    return results
