def handleNonIntegerArguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):

                raise HandleNonIntegerArgumentsException(f"Arguments must be integers. Found {type(arg).__name__}.")

        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise HandleNonIntegerArgumentsException(
                    f"Arguments must be integers. Found {type(value).__name__} for key '{key}'.")

        # 2. Nếu tất cả các đối số đều là số nguyên, gọi hàm gốc
        return func(*args, **kwargs)

    return wrapper


class HandleNonIntegerArgumentsException(TypeError):
    """
    Custom exception raised when a non-integer argument is passed to a decorated function.
    """
    pass


# -----------------------------------------------------
# VÍ DỤ CỦA BÀI TẬP:
# -----------------------------------------------------

# Áp dụng Decorator vào hàm sum
@handleNonIntegerArguments
def sum_and_return(a, b, c):
    return a + b + c
