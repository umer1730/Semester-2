_internal_helper_function = lambda x:x*2
def public_function():
    return "This is public"
class Myclass:
    _protected_attr = 100
    public_attr = 200
print(_internal_helper_function(5))