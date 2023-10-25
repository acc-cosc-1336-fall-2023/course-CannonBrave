import unittest

from src.examples.g_lists_and_tuples.lists import get_list_return_value, get_list_total_for, get_list_total_while, list_ref_param, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_list_total_w_while(self):
        list1 = [5, 10, 20]
        self.assertEqual(get_list_total_while(list1), 35)

    def test_get_list_total_w_for(self):
        list1 = [5, 10, 20]
        self.assertEqual(get_list_total_for(list1), 35)

    def test_list_param_not_a_copy(self):
        list1 = [5, 10, 20]
        list_ref_param(list1)
        print(list1)
        self.assertEqual(list1, [0, 10, 20])

    def test_list_return_value(self):
        list1 = [5, 10, 20]
        print("before", id(list1))
        get_list_return_value(list1)
        print("after", id(list1))
        self.assertEqual(list1, [0, 10, 20])

    #def test_list_slicing_start_end(self):
    #   days = 

    def test_list_slicing_start_no_end(self):
        list = [1,2,3,4,5]

        self.assertEqual(list[2:], [3,4,5])

    
     def test_list_slicing_w_step(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(list[1:8:2], [2,4,6,8])

    def test_list_slicing_start_from_end(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(list[-5:], [6, 7, 8, 9, 10])

    def test_item_in_list(self):
        prod_nums = ['V475', 'F987', 'Q143', 'R688']

        self.assertEqual(search_for_item_in_list('F987', prod_nums), True)
        self.assertEqual(search_for_item_in_list('G999', prod_nums), False)

    def test_list_copy_doesnt_create_another_list(self):
        list1 = [1,2,3,4]
        list2 = list1

        list2[0] = 0

        self.assertEqual(list1 == list2, True)
        self.assertEqual(list1[0] == list2[0], True)
        self.assertEqual(list1[0] == 0, True)
        self.assertEqual(list2[0] == 0, True)

    def test_create_list_from_existing_list(self):
        list1 = [1,2,3,4]
        list2 = []#empty list

        for i in range(0, len(list1)):
            list2.append(list1[i])

        self.assertEqual(list1 == list2, True)

        list1[0] = 0

        self.assertEqual(list1[0] == list2[0], False)
        self.assertEqual(list1[0] == 0, True)
        self.assertEqual(list2[0] == 1, True)

    def test_create_list_from_existing_list_conc(self):
        list1 = [1,2,3,4]
        list2 = [] + [1,2,3,4]

        list1[0] = 0

        self.assertEqual(list1[0] == list2[0], False)
        self.assertEqual(list1[0] == 0, True)
        self.assertEqual(list2[0] == 1, True)

    def test_list_find_item_at_index(self):
        list1 = [1,2,3,4]

        self.assertEqual(list1.index(2), 1)

    def test_insert_item_at_index(self):
        list1 = [1,2,3,4]
        list1.insert(2, 5)
        print(list1)

        self.assertEqual(list1[2] == 5, True)

    def test_del_list_item(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(id(list))
        del list[2]
        print(id(list))

        self.assertEqual(list == [1, 2, 4, 5, 6, 7, 8, 9, 10], True)

    def test_get_max_from_list(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(max(list), 10)

    def test_get_min_from_list(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(min(list), 1)