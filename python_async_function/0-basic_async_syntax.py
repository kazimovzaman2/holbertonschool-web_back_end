#!/usr/bin/env python3
"""Python async task"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and `max_delay` seconds"""
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
