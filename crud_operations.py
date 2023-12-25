
import requests
from faker import Faker
from entities import User, Product
import logging

fake = Faker()
logger = logging.getLogger(__name__)

def create_user():
    user_id = fake.uuid4()
    username = fake.user_name()
    email = fake.email()
    user = User(user_id, username, email)
    logger.info(f"Created user: {user.__dict__}")
    return user

def read_user(user_id):
    response = requests.get(f"http://localhost:3000/users/{user_id}")
    user_data = response.json()
    logger.info(f"Read user: {user_data}")
    return User(**user_data)

def update_user(user_id, new_username):
    data = {"username": new_username}
    response = requests.patch(f"http://localhost:3000/users/{user_id}", json=data)
    updated_user_data = response.json()
    logger.info(f"Updated user: {updated_user_data}")
    return User(**updated_user_data)

def delete_user(user_id):
    response = requests.delete(f"http://localhost:3000/users/{user_id}")
    logger.info(f"Deleted user: {user_id}")

def create_product():
    product_id = fake.uuid4()
    name = fake.word()
    price = fake.random_number(digits=3)
    product = Product(product_id, name, price)
    logger.info(f"Created product: {product.__dict__}")
    return product
