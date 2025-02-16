import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1/statistic"

# Тест-кейс 1: Позитивный, существующий id
@pytest.mark.parametrize("item_id", ["ee4d0c6a-1606-4573-af8f-11c3485a62e4"])
def test_get_statistic_valid_id(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(key in data[0] for key in ["likes", "viewCount", "contacts"])

# Тест-кейс 2: Негативный, неверный формат идентификатора
@pytest.mark.parametrize("item_id", [None])
def test_get_statistic_invalid_format(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 3: Негативный, использование недопустимого метода
@pytest.mark.parametrize("item_id", ["ee4d0c6a-1606-4573-af8f-11c3485a62e4"])
def test_get_statistic_wrong_method(item_id):
    response = requests.options(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 405

# Тест-кейс 4: Негативный, нулевое значение id
@pytest.mark.parametrize("item_id", [None])
def test_get_statistic_null_id(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 5: Негативный, id принимает значение "%00"
@pytest.mark.parametrize("item_id", ["%00"])
def test_get_statistic_null_byte(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 6: Негативный, несуществующий идентификатор
@pytest.mark.parametrize("item_id", ["ee4d0c6a-1606-4573-af8f-11c3485a62e2"])
def test_get_statistic_nonexistent_id(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 404

# Тест-кейс 7: Позитивный, идентификатор без символов "-"
@pytest.mark.parametrize("item_id", ["ee4d0c6a16064573af8f11c3485a62e4"])
def test_get_statistic_id_without_hyphens(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(key in data[0] for key in ["likes", "viewCount", "contacts"])

# Тест-кейс 8: Негативный, лишний пробел в идентификаторе
@pytest.mark.parametrize("item_id", [" ee4d0c6a-1606-4573-af8f-11c3485a62e4"])
def test_get_statistic_id_with_space(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", headers={"Accept": "application/json"})
    assert response.status_code == 400
