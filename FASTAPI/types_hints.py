'''

Python types: -
	1. type hints (type annotations) are special syntax that allow declaring the type of a variable.

	2. Primary types are : -
		a. str
		b. int
		c. float
		d. bool
		e. bytes

	3. Generic types are : -
		a. List[data_type]
		b. Tuple[data_type]
		c. Set[data_type]
		d. Dict[key_data_type, value_data_type]
		e. Union[data_type1, data_type2, ..., data_typeN]
		f. Optional[str] = None <===> Union[data_type, None] = None
	   These are imported from typing module.
	   If we declare N data type on single generic type then that variable will contain N no. of variables.

	4. Class types -> these are user defined using class.
 
	5. Annotated[data_type, some_string_message]

'''
from typing import List, Tuple, Set, Dict, Union, Annotated

def process_items(items: List[str]):
    for item in items:
        return item

def process_items_1(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s

def process_items_2(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        return item_name, item_price

def process_item_3(item: Union[int, str]):
    return item

def say_hi(name: Union[str, None] = None):
    if name is not None:
        return f"Hey {name}!"
    else:
        return "Hello World"
        
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

def say_hello(name: Annotated[str, "this user annotation"]) -> str:
    return f"Hello {name}"

# a = process_items(['apple','banana','guava','grapes'])
# b = process_items_1(('apple','banana','guava','grapes'),{100,200,300,400})
# c = process_items_2({'apple':100.0})
# d1 = process_item_3(['apple','banana','guava','guava'])
# d2 = process_item_3([1,2,3,4])
# e1 = say_hi('Debrishi Biswas')
# e2 = say_hi()
# f = get_person_name(Person('Debrishi'))
# g = say_hello(', World!')