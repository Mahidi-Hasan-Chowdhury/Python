#function is a first class object

def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

print(double_decker())
print(double_decker()())


def do_work(work):
    print('Work Start')
    print(work)
    #work()
    print('Work End')


do_work(2)
do_work('I am Busy')

def coding():
    print("Coding in Python")

do_work(coding)