
def test(x):
    if x == 1:
        return False
    return False

def test2(x):
    return not test(x)

print(test2(1))