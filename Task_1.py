class FlatIterator:
	
	
    def __init__(self, list_of_list):
        self.main_list = list_of_list
	
	
    def __iter__(self):
        self.list_cursor_1 = 0  
        self.list_cursor_2 = -1 
        return self
	
	
    def __next__(self):
        self.list_cursor_2 += 1 
		
        if self.list_cursor_2 >= len(self.main_list[self.list_cursor_1]):  
            self.list_cursor_1 += 1      
            self.list_cursor_2 = 0     
		
        if self.list_cursor_1  >= len(self.main_list):
            raise StopIteration
			
        return self.main_list[self.list_cursor_1][self.list_cursor_2]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()