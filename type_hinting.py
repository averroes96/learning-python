def say_Hello(name) -> str: # Type hinting : name must be of type string
    print(f"Hello {name.lower().capitalize()}")

say_Hello("AdA")