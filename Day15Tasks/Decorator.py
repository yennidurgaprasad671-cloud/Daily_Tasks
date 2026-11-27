"""8. Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary """
from functools import wraps

# Store roles in a dictionary
user_roles = {"alice": "admin", "bob": "editor", "charlie": "viewer"}


def require_role(allowed_roles):

  def decorator(func):

    @wraps(func)
    def wrapper(username, *args, **kwargs):
      role = user_roles.get(username)
      if role in allowed_roles:
        return func(username, *args, **kwargs)
      else:
        print(f"Access Denied for '{username}' (Role: {role}).")

    return wrapper

  return decorator


@require_role(["admin"])
def delete_database(username):
  print(f"Database deleted by {username}.")


@require_role(["admin", "editor"])
def edit_article(username, title):
  print(f"Article '{title}' edited by {username}.")


delete_database("bob")  # Denied
delete_database("alice")  # Allowed
edit_article("bob", "News")  # Allowed
