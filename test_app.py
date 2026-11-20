from app import app


def test_home():
    res = app.test_client().get("/")
    assert res.status_code == 200


def test_health():
    res = app.test_client().get("/health")
    assert res.get_json()["status"] == "ok"


def test_add_and_get_note():
    client = app.test_client()
    res = client.post("/notes", json={"text": "hello"})
    assert res.status_code == 201
    res = client.get("/notes")
    assert any(n["text"] == "hello" for n in res.get_json())


def test_add_note_without_text():
    res = app.test_client().post("/notes", json={})
    assert res.status_code == 400