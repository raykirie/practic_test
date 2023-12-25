# test_base.py
import unittest
import requests
from entities import User, Product
from crud_operations import create_user, read_user, update_user, delete_user, create_product

class TestCRUDOperations(unittest.TestCase):
    def setUp(self):
        self.user = create_user()

    def test_user_crud(self):
        # Тестирование CRUD для пользователей
        user_id = self.user.user_id

        # Test Create User
        created_user = create_user()
        self.assertIsNotNone(created_user.user_id)
        self.assertIsNotNone(created_user.username)
        self.assertIsNotNone(created_user.email)

        # Test Read User
        read_user_obj = read_user(user_id)
        self.assertEqual(read_user_obj.user_id, user_id)
        self.assertEqual(read_user_obj.username, self.user.username)
        self.assertEqual(read_user_obj.email, self.user.email)

        # Test Update User
        updated_username = "new_username"
        updated_user = update_user(user_id, updated_username)
        self.assertEqual(updated_user.user_id, user_id)
        self.assertEqual(updated_user.username, updated_username)
        self.assertEqual(updated_user.email, self.user.email)

       
        delete_user(user_id)
        
        response = requests.get(f"http://localhost:3000/users/{user_id}")
        self.assertEqual(response.status_code, 404)

    def test_product_crud(self):
        
        product = create_product()

        self.assertIsNotNone(product.product_id)
        self.assertIsNotNone(product.name)
        self.assertIsNotNone(product.price)

        product_id = product.product_id
        read_product_response = requests.get(f"http://localhost:3000/products/{product_id}")
        read_product_data = read_product_response.json()
        self.assertEqual(read_product_response.status_code, 200)
        self.assertEqual(read_product_data['product_id'], product_id)
        self.assertEqual(read_product_data['name'], product.name)
        self.assertEqual(read_product_data['price'], product.price)

        updated_name = "new_product_name"
        updated_price = 300
        updated_product_data = {"name": updated_name, "price": updated_price}
        update_product_response = requests.put(f"http://localhost:3000/products/{product_id}", json=updated_product_data)
        self.assertEqual(update_product_response.status_code, 200)

        delete_product_response = requests.delete(f"http://localhost:3000/products/{product_id}")
        self.assertEqual(delete_product_response.status_code, 200)

        deleted_product_response = requests.get(f"http://localhost:3000/products/{product_id}")
        self.assertEqual(deleted_product_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
