from utilities import add
import pytest

@pytest.mark.mark1
def test_add1():
    result = add(10,10)
    assert result == 20
    
@pytest.mark.parametrize("a,b,result",[(10,20,30),("python","java","pythonjava"),("python", 10, "Invalild Input!")])
                                 
def test_add2(a,b, result):
    res = add(a,b)
    assert res == result
    
  
