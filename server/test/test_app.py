import pytest
from app import app  # import the Flask instance


@pytest.fixture
def client():
    # Create a test client for the Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Python Operations with Flask Routing and Views' in response.data


def test_print_string(client):
    """Test the /print/<string:param> route"""
    response = client.get('/print/hello')
    assert response.status_code == 200
    assert response.data == b'hello'


def test_count(client):
    """Test the /count/<int:param> route"""
    response = client.get('/count/5')
    assert response.status_code == 200
    expected_output = b'0\n1\n2\n3\n4'
    assert response.data == expected_output


@pytest.mark.parametrize("num1,operation,num2,expected", [
    (5, 'add', 3, '8'),
    (10, 'sub', 4, '6'),
    (6, 'mult', 7, '42'),
    (8, 'div', 2, '4.0'),
    (10, 'mod', 3, '1'),
])
def test_math_operations(client, num1, operation, num2, expected):
    """Test the /math/<int:num1>/<operation>/<int:num2> route"""
    response = client.get(f'/math/{num1}/{operation}/{num2}')
    assert response.status_code == 200
    assert response.data.decode() == expected


def test_invalid_operation(client):
    """Test invalid operation handling"""
    response = client.get('/math/5/invalid/2')
    assert response.status_code == 200
    assert response.data == b'Invalid operation'
