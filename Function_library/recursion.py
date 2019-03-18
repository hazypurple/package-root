def sum_array(array):
    """
    Return the sum of all items in array

    Args:
        array (array): specified array to add together

    Returns:
        int: the result of the sum of the itmes in the array
    """
    if len(array) <= 1:
        return array
    else:
        array[-2] = array[-1] + array[-2]
        array.pop()
        return sum_array(array)


def fibonacci(n):
    """
    Return the nth term  in the fibonacci sequence

    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    """
    if n <= 1:
        return n
    else:
        return fibonnacci (n-1) + fibonnacci(n-2)

def factorial(n):
    """Return n!
    Calculate factorial of n

    Args:
        n (int): nth term to calculate

    Returns:
        int: result of the factorial of n


    """
    if n <= 0:
        return(1)
    else:
        return (factorial(n-1) * n)

def reverse(word):
    """
    Return word in reverse

    Args:
        word (string): word to reverse

    Returns:
        string : the specified word in reverse

    """

    if len(word) <= 1:
        return word
    else:
        return word[-1] + reverse(word[:-1])
