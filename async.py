import time
st = time.perf_counter()
def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} end")

task("A")
task("B")
task("C")
ft = time.perf_counter()
print(ft-st)

import asyncio
st = time.perf_counter()
async def task(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name} end")

async def main():
    await asyncio.gather(task("A"),
task("B"),
task("C"))
    
asyncio.run(main())
ft = time.perf_counter()
print(ft-st)

# fetching multiple URLs
# using sync as usual
import requests

def get(url):
    return requests.get(url).json()

user = get("https://api.github.com/users/octocat")
repos = get("https://api.github.com/users/octocat/repos")
followers = get("https://api.github.com/users/octocat/followers")

print("Done")

# using async

import asyncio
import aiohttp

async def fetch(session, url):
    print("Requesting:", url)
    async with session.get(url) as response:
        data = await response.json()   # pause while waiting for network
        print("Received:", url)
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            fetch(session, "https://api.github.com/users/octocat"),
            fetch(session, "https://api.github.com/users/octocat/repos"),
            fetch(session, "https://api.github.com/users/octocat/followers")
        )

asyncio.run(main())

