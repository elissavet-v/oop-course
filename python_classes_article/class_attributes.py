class ObjectCounter:
    num_instances = 0

    def __init__(self):
        ObjectCounter.num_instances += 1


my_instance = ObjectCounter()
print(my_instance.num_instances)
