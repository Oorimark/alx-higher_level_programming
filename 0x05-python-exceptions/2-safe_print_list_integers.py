#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ safe print list integers

        prints integers only with array of any type

        Args:
            my_list (list): array of items
            x (int): number of items to be printed

        Returns:
            (int): The number of items printed
    """
    counter = 0

    try:
        for i in range(x):
            if i < x:
                try:
                    print("{:d}".format(my_list[i]), end="")
                    counter += 1
                except (ValueError, TypeError):
                    continue
                except IndexError as err:
                    raise err

            else:
                break
        print("")
        return counter
    except Exception as err:
        print("")
        raise err
        return counter
