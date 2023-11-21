#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            d = my_list_1[i] / my_list_2[i]
            new_list.append(d)
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            new_list.append(0)
        except IndexError:
            print("{}".format("out of range"))
            new_list.append(0)
        except TypeError:
            print("{}".format("wrong type"))
            new_list.append(0)
        finally:
            i = i + 1
    return new_list
