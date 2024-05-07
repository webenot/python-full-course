class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


my_list = ExtendedList([1, 2, 3])
my_list.print_list_info()

print(list.__subclasses__())
