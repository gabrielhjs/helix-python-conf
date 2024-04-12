import pymongo


test = "str"


print(pymongo.version)


def test1(param: str) -> str:
    return param


print(test1(test))
