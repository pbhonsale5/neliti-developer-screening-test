def is_possible(numbers, sum_req):
    """ This is a recursive function, which add/sub item from list one by one and check 
       if it is 0 then we got a combination
       Args:
           numbers(list): it is a list of remaining itmes 
           sum_req(int) : it is a remaing total
       return:
            True if match found else None
    """
    if not numbers:
        return sum_req == 0
    *remaining, item = numbers
    return any([is_possible(remaining, sum_req + item) , is_possible(remaining, sum_req - item)])


def f(numbers, sum_req):
    """ Given a list of integers and a target integer, write a function that expresses 
       the target integer by inserting `+` and `-` operations between the list items
       Args:
           numbers(list): it is a list of remaining itmes 
           sum_req(int) : it is a remaing total
       return:
            sum_req if match found else None

    """
    if is_possible(numbers, sum_req):
        return sum_req
