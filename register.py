def signup(name, password, email):
    if email.endswith("@gmail.com"):
        if len(password) >= 8:
            return "Account created successfully"
        else:
            return "Password should be 8 characters long"
    else:
        return "Invalid email"
    
if __name__ == "__main__":
    signup("Ancy","12345678","Ancy@gmail.com")
    signup("Ancy","12678","Ancy@gmail.com")
    signup("Ancy","12345678","Ancy@gmail.")



