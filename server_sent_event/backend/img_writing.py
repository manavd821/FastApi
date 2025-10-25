import itertools
import time
import aiohttp
import asyncio
from pathlib import Path

start = time.perf_counter()

dir_path = Path('uploads')
dir_path.mkdir(exist_ok=True)

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

async def write_img(img_url : str):

    async with aiohttp.ClientSession() as session:
        async with session.get(img_url) as resp:
            img_name = img_url.split('/')[-1]
            file_path = dir_path / f'{img_name}.jpeg'
            file_path.touch(exist_ok=True)
            with open(file_path, 'wb') as f:
                async for chunk in resp.content.iter_chunked(65536):
                    print(itertools.count(), end = " ")
                    f.write(chunk)
async def main():
    tasks = [asyncio.create_task(write_img(img)) for img in img_urls]
    await asyncio.gather(*tasks)
            

if __name__ == "__main__":
    asyncio.run(main())
    end = time.perf_counter()
    print('\n',end-start)