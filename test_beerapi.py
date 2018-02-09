import beerapi


def test_root_gives_hello_world():
    beerapi.app.testing = True
    app = beerapi.app.test_client()

    result = app.get('/')
    assert b"Hello World" in result.data
