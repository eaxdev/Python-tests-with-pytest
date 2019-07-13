from api.FakeApi import FakeApi


# use fake api: https://jsonplaceholder.typicode.com/

def test_get_all_fake_todos():
    fake = FakeApi()
    todos = fake.get_all_fake_todos()
    assert todos[0]['userId'] == 1
    assert todos[0]['id'] == 1
    assert todos[0]['title'] == 'delectus aut autem'
    assert todos[0]['completed'] is False
    assert len(todos) == 200
