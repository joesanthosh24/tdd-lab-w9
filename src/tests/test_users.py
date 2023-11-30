import json

def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users', 
        data=json.dumps({
            'username': 'john', 
            'email': 'john@algonquincollege.com'
        }),
        content_type='application/json'
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'john@algonquincollege.com was added!' in data['message']