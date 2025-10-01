from source_code.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(3,3)==6
    assert add(7,3)==10
    assert add(150,3)==153


def test_sub():
    assert sub(2,3)==-1
    assert sub(15,3)==12
    assert sub(22,3)==19
    assert sub(3,3)==0

    