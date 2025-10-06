from app.main import add, divide, async_add, async_divide
import pytest

@pytest.fixture
def set_data(): return {"a" : 10, "b" : 15}

def test_add_with_fixture(set_data):
    assert add(set_data["a"], set_data["b"]) == 25
    
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (1,1,2)])
def test_add_params(a,b, expected):
    assert add(a,b) == expected
    
@pytest.mark.skip(reason="Feature not implemented yet")
def future_feature():
    pass

@pytest.mark.asyncio
async def test_async_add():
    assert await async_add(2,3) == 5
    assert await async_add(-1,1) == 0

@pytest.mark.asyncio
async def test_async_divide_by_zero():
    with pytest.raises(ValueError):
        await async_divide(10,0)