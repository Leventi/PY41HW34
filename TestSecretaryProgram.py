import unittest
from main import *


class TestSecretaryProgram(unittest.TestCase):


    def test_get_all_doc_owners_names(self):
        users_list = ['Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин']
        self.assertEqual(get_all_doc_owners_names('ap'), set(users_list))


    def test_get_doc_owner_name(self):
        user_doc_number = '10006'
        doc_owner_name = 'Аристарх Павлов'
        self.assertEqual(get_doc_owner_name('p', user_doc_number), doc_owner_name)


    def test_check_document_existance(self):
        user_doc_number = '10006'
        self.assertEqual(check_document_existance(user_doc_number), True)

    def test_add_new_shelf(self):
        shelf_number = '3'
        self.assertIn(shelf_number, directories)

    def test_append_doc_to_shelf(self):
        doc_number = '10006'
        shelf_number = '2'
        self.assertIn(doc_number, directories[shelf_number])

    def test_get_doc_shelf(self):
        user_doc_number = '11-2'
        directory_number = '1'
        self.assertEqual(get_doc_shelf('s', user_doc_number), directory_number)

    def test_delete_doc(self):
        user_doc_number = '10006'
        self.assertNotIn(user_doc_number, directories)


    def test_move_doc_to_shelf(self):
        user_doc_number = '2207 876234'
        user_shelf_number = '2'
        res = ('2207 876234', '2')
        self.assertEqual(move_doc_to_shelf('m', user_doc_number, user_shelf_number), res)

    def test_add_new_doc(self):
        res = {"type": "pasport", "number": "123123", "name": "John Doe"}
        new_doc_number = "123123"
        new_doc_type = "pasport"
        new_doc_owner_name = "John Doe"
        new_doc_shelf_number = "3"
        self.assertEqual(add_new_doc('a', new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number), new_doc_shelf_number)

