
class Car(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return type(self).__name__ + "_" + self.name


def property_change(original):
    new_copy = [item for item in original]
    for index,i in enumerate(new_copy):
        if index == 2:
            i.name = "ABC"
    print(new_copy)


def change_elements(original):
    new_copy = [item for item in original]
    for index,i in enumerate(new_copy):
        if index < len(new_copy)-1 :
            new_copy[index] = new_copy[index+1]
    print(new_copy)


def swap_elements(original):
    new_copy = [item for item in original]
    for index, i in enumerate(new_copy):
        if index < len(new_copy) - 1:
            temp = new_copy[index]
            new_copy[index] = new_copy[index+1]
            new_copy[index+1] = temp
    print(new_copy)


def add_elements(original):
    new_copy = [item for item in original]
    for index, i in enumerate(new_copy):
        if index == 10:
            break
        new_copy.append(Car(f"New_Car{index}"))
    print(new_copy)


def remove_elements(original):
    new_copy = [item for item in original]
    for index, i in enumerate(new_copy):
        if index == 2:
            new_copy.pop(index)
    print(new_copy)


if __name__ == '__main__':
    """
    This is used to Test the way python handles changes in a list, while iterating
    Each Method only does one type of operation
    """
    my_cars = [Car("Ferrari"), Car("Mercedes"), Car("BMW")]
    # property_change(my_cars)
    # change_elements(my_cars)
    swap_elements(my_cars)
    # add_elements(my_cars)
    # remove_elements(my_cars)