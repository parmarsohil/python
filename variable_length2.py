def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_info(name="XYZ",age=102,city="ABC")