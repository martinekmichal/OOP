
def stars(my_function):
    def foo():
        print("********************")
        result = my_function()
        print("********************")
        return result
    return foo


@stars
def current_time():
    print("23:00")


current_time()