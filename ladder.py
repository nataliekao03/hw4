# to run program, go to terminal and run "python3 ladder.py"
def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError("Invalid input")

    return my_steps(n - 1) + my_steps(n - 2)
