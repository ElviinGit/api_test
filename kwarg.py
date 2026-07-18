def my_kwarg(*args, **kwargs):
    return f"my arguments are: {args}, my keyword arguments are: {kwargs}"


simple = my_kwarg("first", "second", env="qa", debug=True)  

print(simple)