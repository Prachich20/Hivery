import app


def test_emp():
    client = app.app.test_client()
    url = '/emp'
    response = client.get(url, query_string={'company': 'ZENTRY'})
    assert response.status_code == 200


def test_nonexistent_emp():
    client = app.app.test_client()
    url = '/emp'
    response = client.get(url, query_string={'company': 'TEST'})
    assert response.status_code == 200


def test_people():
    client = app.app.test_client()
    url = '/people'
    response = client.get(url, query_string={'frnd1': '18', 'frnd2': '24'})
    assert response.status_code == 200


def test_food():
    client = app.app.test_client()
    url = '/food/1'
    response = client.get(url)
    assert response.status_code == 200