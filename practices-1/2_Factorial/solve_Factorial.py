def factorial(number : int) -> int:
    """get number and caculate factorial of number

    Args:
        number (int): input number and must to postive number

    Raises:
        ValueError: if number is negative then raise ValueError

    Returns:
        int: calcualted factorial
    """
    if number < 0:
        raise ValueError

    if number == 0 or number == 1:
        return 1
    
    factorial_number = 1
    for i in range(number, 1, -1):
        factorial_number = i * factorial_number
    
    return factorial_number

def main():
    """Main program

    """
    
    # get number as string and cast to int
    n_number = int(input())
    assert n_number > 0 and n_number <= 10
    factorial_n = factorial(n_number)
    print(factorial_n)
if __name__ == "__main__":
    main()
