import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1/item"

# Тест-кейс 1: Позитивный, корректные данные
@pytest.mark.parametrize("payload", [{"sellerID": 798132, "name": "Люстра", "price": 22000}])
def test_post_valid_ad(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert "status" in data

# Тест-кейс 2: Негативный, использование GET вместо POST
def test_post_invalid_method():
    response = requests.get(BASE_URL, headers={"Accept": "application/json"})
    assert response.status_code == 405

# Тест-кейс 3: Позитивный, без идентификатора продавца
@pytest.mark.parametrize("payload", [{"name": "Люстра", "price": 22000}])
def test_post_missing_sellerID(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 4: Позитивный, без названия товара
@pytest.mark.parametrize("payload", [{"sellerID": 764398, "price": 22000}])
def test_post_missing_name(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 5: Позитивный, без стоимости товара
@pytest.mark.parametrize("payload", [{"sellerID": 764398, "name": "Люстра"}])
def test_post_missing_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 6: Негативный, отрицательная стоимость
@pytest.mark.parametrize("payload", [{"sellerID": 798132, "name": "Люстра", "price": -22000}])
def test_post_negative_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 7: Негативный, некорректный идентификатор продавца
@pytest.mark.parametrize("payload", [{"sellerID": -798132, "name": "Люстра", "price": 22000}])
def test_post_invalid_sellerID(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 200

# Тест-кейс 8: Негативный, некорректное имя товара
@pytest.mark.parametrize("payload", [{"sellerID": 798132, "name": 442323, "price": 22000}])
def test_post_invalid_name(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 9: Негативный, строковый идентификатор продавца
@pytest.mark.parametrize("payload", [{"sellerID": "798132", "name": "Люстра", "price": 22000}])
def test_post_string_sellerID(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400

# Тест-кейс 10: Негативный, строковая стоимость
@pytest.mark.parametrize("payload", [{"sellerID": 798132, "name": "Люстра", "price": "22000"}])
def test_post_string_price(payload):
    response = requests.post(BASE_URL, json=payload, headers={"Content-Type": "application/json", "Accept": "application/json"})
    assert response.status_code == 400
