def test_homepage_content(app, client):
    response = client.get("/")
    assert b" Hello, world!" in response.data

def test_homepage_route_status_code(app, client):
    route = "/"
    rv = client.get(route)
    assert rv.status_code == 200