import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"

# Тест-кейс 1: Позитивный, существующий sellerID
@pytest.mark.parametrize("seller_id", [555353])
def test_get_items_by_seller_success(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert "id" in item and "sellerId" in item and item["sellerId"] == seller_id

# Тест-кейс 2: Неверный формат sellerID
@pytest.mark.parametrize("seller_id", ["wrong_sellerID"])
def test_get_items_by_seller_invalid_format(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 3: Неподдерживаемый метод
@pytest.mark.parametrize("seller_id", [55535335])
def test_get_items_by_seller_wrong_method(seller_id):
    response = requests.delete(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 405

# Тест-кейс 4: Нулевое значение sellerID
@pytest.mark.parametrize("seller_id", [None])
def test_get_items_by_seller_null_id(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 5: sellerID в виде %00
@pytest.mark.parametrize("seller_id", ["%00"])
def test_get_items_by_seller_null_byte(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 6: Несуществующий sellerID
@pytest.mark.parametrize("seller_id", [312783])
def test_get_items_by_seller_not_found(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert response.json() == []

# Тест-кейс 7: sellerID равен 0
@pytest.mark.parametrize("seller_id", [0])
def test_get_items_by_seller_zero(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 8: sellerID равен -1
@pytest.mark.parametrize("seller_id", [-1])
def test_get_items_by_seller_negative(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 9: sellerID равен 1
@pytest.mark.parametrize("seller_id", [1])
def test_get_items_by_seller_one(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 10: sellerID равен 111110
@pytest.mark.parametrize("seller_id", [111110])
def test_get_items_by_seller_below_range(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 11: sellerID равен 111111
@pytest.mark.parametrize("seller_id", [111111])
def test_get_items_by_seller_lower_bound(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 12: sellerID равен 111112
@pytest.mark.parametrize("seller_id", [111112])
def test_get_items_by_seller_valid(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 13: sellerID равен 999998
@pytest.mark.parametrize("seller_id", [999998])
def test_get_items_by_seller_upper_bound(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 14: sellerID равен 999999
@pytest.mark.parametrize("seller_id", [999999])
def test_get_items_by_seller_max_limit(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 15: sellerID равен 1000000
@pytest.mark.parametrize("seller_id", [1000000])
def test_get_items_by_seller_above_range(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 16: Лишний пробел в sellerID
@pytest.mark.parametrize("seller_id", ["121212 ", " 121212"])
def test_get_items_by_seller_extra_space(seller_id):
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers={"Accept": "application/json"})
    assert response.status_code == 400
