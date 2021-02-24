def print_star_lozenge(n_number: int):

    assert n_number % 2 == 1 and n_number > 1, "number must be odd"
    # print upside
    for i in range(1, n_number + 1 , 2):
        # print upside left
        print(("*" * i).center(n_number), end="")
        # print upside right
        print(("*" * i).center(n_number))
    # print downside
    for i in reversed(range(1, n_number , 2)):
        # print downside left
        print(("*" * i).center(n_number), end="")
        # print downside right
        print(("*" * i).center(n_number))


def main():
    """Main program

    """

    # get number as string and cast to int
    n_number = int(input())
    assert n_number > 0 and n_number <= 19 
    

    print_star_lozenge(n_number)


if __name__ == "__main__":
    main()
