def outer():
    def inner():
        print("I'm nested function")

    print("I'm outside function")
    inner()

outer() 