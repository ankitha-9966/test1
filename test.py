from register import signup

def test_cases():
    assert(signup("Ancy","12345678","Ancy@gmail.com"))
    assert(signup("Ancy","12678","Ancy@gmail.com"))
    assert(signup("Ancy","12345678","Ancy@gmail."))

if __name__ == "__main__":
    test_cases

