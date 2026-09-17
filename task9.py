value = 100
def show_scope():
    value = 50
    print("Global variable:", globals()["value"])
    print("Local variable:", value)

show_scope()