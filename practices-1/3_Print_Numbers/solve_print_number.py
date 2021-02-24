def print_numbers(numbers: str):
    
    # check if can not cast into int then mean have invalid input
    _ = int(numbers)
    

    for char in numbers:
        print(f"{char}: {int(char) * char}")
    


def main():
    """Main program

    """

    # get string as input
    number = input()
    print_numbers(number)


if __name__ == "__main__":
    main()
