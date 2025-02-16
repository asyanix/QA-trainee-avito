import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1/item"

# Тест-кейс 1: Позитивный тест, существующий ID
@pytest.mark.parametrize("item_id", ["ee4d0c6a-1606-4573-af8f-11c3485a62e4"])
def test_get_item_success(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) and len(data) > 0 
    assert "id" in data[0] and data[0]["id"] == item_id
    assert "sellerId" in data[0] and isinstance(data[0]["sellerId"], int)
    assert "price" in data[0] and isinstance(data[0]["price"], int)
    assert "statistics" in data[0] and isinstance(data[0]["statistics"], dict)

# Тест-кейс 2: Неверный формат ID
@pytest.mark.parametrize("item_id", ["incorrect_id"])
def test_get_item_invalid_format(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 3: Неподдерживаемый метод
@pytest.mark.parametrize("item_id", ["ee4d0c6a-1606-4573-af8f-11c3485a62e4"])
def test_get_item_wrong_method(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 405

# Тест-кейс 4: Нулевое значение ID
@pytest.mark.parametrize("item_id", [None])
def test_get_item_null_id(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400  

# Тест-кейс 5: ID в виде %00
@pytest.mark.parametrize("item_id", ["%00"])
def test_get_item_null_byte(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 6: Несуществующий ID
@pytest.mark.parametrize("item_id", ["ee4d0c6a-1606-4573-af8f-11c3485a62e2"])
def test_get_item_not_found(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 404

# Тест-кейс 7: ID без символов "-"
@pytest.mark.parametrize("item_id", ["ee4d0c6a16064573af8f11c3485a62e4"])
def test_get_item_no_dashes(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 8: Лишний пробел в ID
@pytest.mark.parametrize("item_id", [" ee4d0c6a-1606-4573-af8f-11c3485a62e4", "ee4d0c6a-1606-4573-af8f-11c3485a62e4 "])
def test_get_item_extra_space(item_id):
    response = requests.get(f"{BASE_URL}/{item_id.strip()} ", headers={"Accept": "application/json"})
    assert response.status_code == 400
