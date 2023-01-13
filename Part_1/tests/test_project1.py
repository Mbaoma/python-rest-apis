# def test_homepage_content(client):
#     response = client.get("/")
#     assert b" Hello, world!" in response.data

def test_homepage_route_status_code(client):
    route = "/api/home"
    rv = client.get(route)
    assert rv.status_code == 200

def test_people_page_status_code(client):
    route = "/api/people"
    rv = client.get(route)
    assert rv.status_code == 200