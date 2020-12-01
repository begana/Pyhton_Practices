def packer(*args):
    for val in args:
        print(val)
    print(" ".join(args))
    
packer('hi','i','love','you')

def calculate_total(*args):
    total = sum(args)
    print(total)
    
calculate_total(20, 30, 25, 15)