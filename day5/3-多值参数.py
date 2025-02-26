def demo(num, *args,  **kwargs):
     print(num)
     print(args)
     print(kwargs)
     print(*args)
     #print(**kwargs)  #字典这样拆包是不可以传给print的
     for key,value in kwargs.items():
         print(f"{key}:{value},",end="")
demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)

