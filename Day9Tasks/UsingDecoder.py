"""13. Secure Login System (Decorators)
A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function."""

is_logged_in = False  # Change to True to allow access


def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access Denied! Please log in first.")

    return wrapper


@login_required
def view_dashboard():
    print("Welcome to your private dashboard!")


# Run the function
view_dashboard()
