import typing

def hello(): # type: () -> None
    print 'hello'

class Example:
    def method(self, lst, opt=0, *args, **kwargs):
        # type: (List[str], int, *str, **bool) -> int
        return 1

def test(i): # type:(int) -> int
    return i + 1

a = test(1)
#print isinstance(test, (int) -> int)
print type(test)