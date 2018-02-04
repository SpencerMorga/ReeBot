def tryParseInt(value):
    try:
        return int(value)
    except ValueError:
        return 0

def testSplit(items):
    if '~df -n' in items:
        token = items.split(" ")
        print(token)
        value = tryParseInt(token[-1])
        print(value)
        for i in range(0, value):
            print(i)

example = "~df -n 0"
testSplit(example)