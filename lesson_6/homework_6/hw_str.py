import functools


def reverse_string(func):
    @functools.wraps(func)
    def wrapper():
        line = func()
        if isinstance(line, str):
            rev_line = line[::-1]
            return rev_line
        return None

    return wrapper


@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


print(get_university_name(), get_university_founding_year(), sep="\n")
