# TODO: format each element in the list(start_string the_list end_string)
def format_the_list_elements(the_list, start_string, end_string):
    for element in the_list:
        print(start_string, element, end_string)

format_the_list_elements([2, 3, 4], "<!", "!>")