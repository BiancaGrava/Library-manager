def cifre(nr):
    """
    from a number given, creates the list of its digits
    :param nr: number given
    :return: list of its digits
    """
    digits=[]
    while nr>9:
        digits.append(nr%10)
        nr=nr//10
    digits.append(nr)
    return digits
def test_cifre():
    assert cifre(123)==[3,2,1]