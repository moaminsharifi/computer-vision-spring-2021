from math import comb

def fact(number: int) -> int:
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

def cacl(number : int) -> int:
    """calculate math function
        latex: Calc(n) = \sum_{i=1}^{n} \prod_{j=1}^{i} {i \choose j}
        utf-8: Calc(n)= i=1 ∑ n ​ j=1 ∏ i ​	 ( j i ​	 )
        link: https://quera.ir/course/assignments/26777/problems/88893

    Args:
        number (int): input number to

    Returns:
        int: calculated number
    """

    sum = 0
    for i in range(1 , number + 1):
        comb_of_this_iter = 1
        for j in range(1, i + 1):
            comb_of_this_iter = comb(i , j) * comb_of_this_iter 
        sum += comb_of_this_iter

    return sum

def main():
    """Main program

    """

    # get number as string and cast to int
    n_number = int(input())
    assert n_number > 0 and n_number <= 100
    result_number = cacl(n_number)
    
    print(result_number)


if __name__ == "__main__":
    main()

