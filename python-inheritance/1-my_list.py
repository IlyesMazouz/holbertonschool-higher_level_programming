class MyList(list):
    """
    MyList class that inherits from list and provides additional functionality
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order
        """
        sorted_list = sorted(self)
        print(sorted_list)
