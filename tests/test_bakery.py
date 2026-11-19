# Tests for the bakery's API. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test sends one request to the app, the request in its name, and checks the status code or the body that comes
# back. TestClient hands each request straight to the app, so no server needs to be running. A failing test says what
# it sent, what it expected and what came back.
# You don't need to change this file. Module 2 shows how tests like these are written.
from fastapi.testclient import TestClient

from data import SPECIALS
from main import app

client = TestClient(app)

WELCOME = {"bakery": "Maple Street Bakery", "message": "Welcome! Today's specials are at /specials."}


def check_status(request, response, status):
    """Fails with a message that says what the request answered, when its status code isn't the one expected."""
    assert response.status_code == status, (
        f"{request} should answer {status}, but it answered {response.status_code} with {response.text}"
    )


def check_body(request, response, body):
    """Fails with a message that says what came back, when the body isn't the one expected."""
    assert response.json() == body, f"{request} should answer {body!r}, but it answered {response.json()!r}."


def test_1_get_root_answers_200():
    check_status("GET /", client.get("/"), 200)


def test_2_get_root_answers_the_maple_street_bakery_welcome():
    response = client.get("/")
    check_status("GET /", response, 200)
    check_body("GET /", response, WELCOME)


def test_3_get_specials_answers_200():
    check_status("GET /specials", client.get("/specials"), 200)


def test_4_get_specials_answers_sourdough_bagels_and_scone():
    response = client.get("/specials")
    check_status("GET /specials", response, 200)
    check_body("GET /specials", response, SPECIALS)


def test_5_the_docs_page_lists_get_root_and_get_specials():
    paths = client.get("/openapi.json").json()["paths"]
    listed = ", ".join(paths) or "no routes"
    slash = " A route written @app.get(\"/specials/\") answers at /specials/, with a slash: write \"/specials\" instead." \
        if "/specials/" in paths else ""
    for path in ["/", "/specials"]:
        assert "get" in paths.get(path, {}), (
            f"The docs page should list GET {path}, but it doesn't. It lists: {listed}.{slash}"
        )
