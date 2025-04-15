import requests

PORT = 8003
BASE_URL = f"http://127.0.0.1:{PORT}"


# Test endpoint GET /books/
def test_get_books():
    response = requests.get(f"{BASE_URL}/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test POST /books/ con dati validi
def test_post_books_valid():
    data = {
        "libri": [
            {
                "titolo": "Le mille e 1 notte",
                "autore": 1,
                "editore": 2,
                "anno_edizione": "2000",
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/books/", json=data)
    print(response.text)
    assert response.status_code == 200
    assert "books processed successfully" in response.text


# Test POST /books/ con dati non validi
def test_post_books_invalid():
    response = requests.post(f"{BASE_URL}/books/", json={"titolo": "Solo Titolo"})
    assert response.status_code == 400
