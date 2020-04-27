# Exercise 6.8 Cargo Hold

In this exercise, we create the classes `Item`, `Suitcase` and `Hold` to practise the use of objects containing other objects.

## Item-class

Create an `Item` class from which objects can be instantiated to represent different items. The information to store is the name and weight of the item (kg).

Add the following methods to the class:

- Constructor that takes the name and the weight of the item as parameters

- Method `def get_name()`, which returns the item's name

- Method `def get_weight()`, which returns the item's weight

- Method `def __str__()`, which returns the string "name (weight kg)"

The following is an example of the class in use:

```python
def main():
    book = Item("The lord of the rings", 2)
    phone = Item("Nokia 3210", 1)

    print("The book's name: " + str(book.get_name()))
    print("The book's weight: " + str(book.get_weight()))

    print("Book: " + str(book))
    print("Phone: " + str(phone))
```

The program's print output should be the following:

```plaintext
The book's name: Lord of the rings
The book's weight: 2
Book: Lord of the rings (2 kg)
Phone: Nokia 3210 (1 kg)
```

## Suitcase-class

Create a `Suitcase` class. The suitcase has items and a maximum weight that determines the maximum total weight of the items.

Add the following methods to the class:

- Constructor, to which the maximum weight is provided

- The method `def add_item(Item item)`, which adds the item passed as a parameter to the suitcase. The method does not return a value.

- The method `def __str__()`, which returns the string "x items (y kg)"

It's advisable to store the items in a `list` object.

```python
items = []
```

The class `Suitcase` should ensure that the total weight of the items within it does not exceed the maximum weight limit. If that limit would be exceeded as a result of the item to be added, the method `add_item` should not add the new item to the suitcase.

The following is an example use case of the class:

```python
def main():
    book = Item("Lord of the rings", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)
```

The program's output should be the following:

```plaintext
0 items (0 kg)
1 items (2 kg)
2 items (3 kg)
2 items (3 kg)
```

## Language Formatting

The statement "1 items" is not exactly proper English -- a better form would be "1 item". The lack of items could also be expressed as "no items". Implement this change to the __str__ method of the `Suitcase` class.

The output of the previous program should now look as follows:

```plaintext
no items (0 kg)
1 item (2 kg)
2 items (3 kg)
2 items (3 kg)
```

## All items

Add the following methods to the `Suitcase` class:

- a `print_items` method, which prints all the items in the suitcase
- a `total_weight` method, which returns the total weight of the items

The following is an example use case of the class:

```python
def main():
    book = Item("Lord of the rings", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    print("Total weight: " + str(suitcase.total_weight()) + " kg")
```

The program's output should be the following:

```plaintext
The suitcase contains the following items:
Lord of the rings (2 kg)
Nokia 3210 (1 kg)
Brick (4 kg)
Total Weight: 7 kg
```

Make a further modification to your class so that you only use two instance variables. One holds the maximum weight, the other is the list of items in the suitcase.

## Heaviest item

Add to the `Suitcase` class a `heaviest_item` method, which returns the largest item based on weight. If several items share the heaviest weight, the method can return any one of them. The method should return an object reference. If the suitcase is empty, return the value *None*.

The following is an example of the class in use:

```python
def main():
    book = Item("Lord of the rings", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    Item heaviest = suitcase.heaviest_item()
    print("Heaviest item: " + heaviest)
```

The program should print the following:

```plaintext
Heaviest item: Brick (4 kg)
```

## Hold-class

Make a `Hold` class with the following methods:

- a constructor, to which the maximum weight is given
- method `def add_suitcase(self, suitcase)` that adds the specified luggage to the hold
- method `def __str__()` that returns the string "x suitcases (y kg)"

Store your suitcases in a suitable `list` structure.

The class `Hold` has to ensure that the total weight of the suitcases it contains does not exceed the maximum weight. Should the maximum weight be exceeded due to the addition of new luggage, the `add_suitcase` method should not add the new suitcase.

The following is an example of the class in use:

```python
def main():
    book = Item("Lord of the rings", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("brick", 4)

    adas_case = Suitcase(10)
    adas_case.add_item(book)
    adas_case.add_item(phone)

    pekkas_case = Suitcase(10)
    pekkas_case.add_item(brick)

    hold = Hold(1000)
    hold.add_suitcase(adas_case)
    hold.add_suitcase(pekkas_case)

    print(hold)
```

The program's output should be the following:

```plaintext
2 suitcases (7 kg)
```

## The Hold's Contents

Add to the `Hold` class the method `def print_items()` that prints all the items contained in the hold's suitcases.

The following is an example of the class in use:

```python
def main():
    book = Item("Lord of the rings", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("brick", 4)

    adas_case = Suitcase(10)
    adas_case.add_item(book)
    adas_case.add_item(phone)

    pekkas_case = Suitcase(10)
    pekkas_case.add_item(brick)

    hold = Hold(1000)
    hold.add_suitcase(adas_case)
    hold.add_suitcase(pekkas_case)

    print("The suitcases in the hold contain the following items:")
    hold.print_items()
```

The program's output should be as follows:

```plaintext
The suitcases in the hold contain the following items:
Lord of the rings (2 kg)
Nokia 3210 (1 kg)
brick (4 kg)
```
