# https://www.instapaper.com/read/1247386154

async def async_function():
    return 1


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


async def async_function():
    s = 1
    for i in range(1, 100000):
        print(i)
        s *= i
    return s

async def await_coroutine():
    result = await async_function()
    print(result)


if __name__ == '__main__':
    run(await_coroutine())