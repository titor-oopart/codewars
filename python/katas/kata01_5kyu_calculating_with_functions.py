def zero(oper=None):
    return int(eval(f"0{oper}")) if oper else 0


def one(oper=None):
    return int(eval(f"1{oper}")) if oper else 1


def two(oper=None):
    return int(eval(f"2{oper}")) if oper else 2


def three(oper=None):
    return int(eval(f"3{oper}")) if oper else 3


def four(oper=None):
    return int(eval(f"4{oper}")) if oper else 4


def five(oper=None):
    return int(eval(f"5{oper}")) if oper else 5


def six(oper=None):
    return int(eval(f"6{oper}")) if oper else 6


def seven(oper=None):
    return int(eval(f"7{oper}")) if oper else 7


def eight(oper=None):
    return int(eval(f"8{oper}")) if oper else 8


def nine(oper=None):
    return int(eval(f"9{oper}")) if oper else 9


def plus(num):
    return f"+{num}"


def minus(num):
    return f"-{num}"


def times(num):
    return f"*{num}"


def divided_by(num):
    return f"/{num}"
