import aiohttp

with open('test.png', 'w') as f:
    with aiohttp.ClientSession() as session:
        f.write(session.get(url='localhost/get_image?team=4444', self=session))
