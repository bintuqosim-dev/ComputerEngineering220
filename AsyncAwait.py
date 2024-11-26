import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


# A CPU-bound task
def cpu_bound_task(n):
    """Calculate Fibonacci numbers (a heavy CPU task)."""
    if n <= 1:
        return n
    else:
        return cpu_bound_task(n - 1) + cpu_bound_task(n - 2)


# A function to run the CPU-bound task in a thread
def run_in_thread(n):
    print(f"Thread started for Fibonacci({n})")
    result = cpu_bound_task(n)
    print(f"Thread finished for Fibonacci({n}): {result}")
    return result


# An async I/O-bound task
async def io_bound_task(duration):
    """Simulate an I/O-bound operation."""
    print(f"Async I/O task started, sleeping for {duration} seconds...")
    await asyncio.sleep(duration)  # Simulates I/O operation
    print(f"Async I/O task finished after {duration} seconds")
    return f"Finished sleeping for {duration} seconds"


# Orchestrating async/await with threads
async def main():
    n = 10
    sleep_duration = 3

    # Thread pool for running the CPU-bound task
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()

        # Run the thread task using run_in_executor
        thread_task = loop.run_in_executor(executor, run_in_thread, n)

        # Run the async task
        async_task = io_bound_task(sleep_duration)

        # Wait for both tasks to complete
        results = await asyncio.gather(thread_task, async_task)
        print(f"Results: {results}")


# Run the main async function
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Total time taken: {time.time() - start_time:.2f} seconds")
