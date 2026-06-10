# yield用法
# from typing import Union
# def apply(): 
#     while True:
#         n = yield
#         print(f"it's jiang hu:{n}")

# f = apply()
# # f.__next__()
# f.send(None)
# for i in range(10):
#     f.send(i)

#类型注解
from typing import List,Union,Optional,Any,Callable
def add(a:list[int]|None)->Union[int,None]:
    return a[0] if a else None

def mer_get(a:int,b:int)->int:
    return a+b

listOne = [1]
# print(add(listOne))

#乘积
def multiply(a:float,b:float)->float:
    return round(a * b ,4)
# print(multiply(2.3333,5.66666))

#相除
def safe_divide(a:int,b:int)->int|None:
    return int(a/b) if b != 0 else None

# 接收多个字符串，用逗号分隔开

def contact_str(*args:str)->str:
    # add = ''
    # for i in args:
    #     add = add + i + ','
    # add = add[:-1]
    # return add
    return ','.join(args)
# print(contact_str('a','s','2','3','f','t','p'))

#输出字典

def cteateUserList(name:str,age:int,**kwargs:str|int|float)->dict:
    userList:dict[str,Any] = {'name':name,'age':age}
    userList.update(kwargs)
    return userList
# print(cteateUserList(age=123,d=3.3,c=3,name='tom'))


#数字运算

def process_item(items:list[Union[int,float]],operation:str)->float|None:
    if not items:
        return None
    if operation == 'sum':
        return sum(items)
    elif operation == 'avg':
        return sum(items)/len(items)
    elif operation == 'max':
        return max(items)
    else:
        return None
    
# print(process_item([3,2,5,7,-1],'sum'))
# print(process_item([3,2,5,7,-1],'avg'))
# print(process_item([3,2,5,7,-1],'max'))

#类型注解
def register_tool(func)->Callable:
    registry[func.__name__] = func
    return func

registry:dict[str,Callable]={}

def execute_tool(name:str,args:dict[str,str|int])->Any:
    if name not in registry:
        raise ValueError(f"Tool {name} not found")
    return registry[name](**args)

@register_tool
def addOne(a,b):
    return a+b

@register_tool
def get_weather(city,unit='celsius'):
    return f"weather in {city} 22°{unit}"
# print(execute_tool('addOne',{"a":2,"b":3}))
# print(execute_tool('get_weather',{'city':'aboluo'}))

#对象

class calculator:
    def __init__(self)->None:
        #操作名和方法名的映射字典
        self._operation:dict[str,Callable] = {
            'add':self._add,
            'suntract':self._suntract,
            'multiply':self._multiply
        }

    def _add(self,a:float,b:float)->float:
        return a + b
    
    def _suntract(self,a:float,b:float)->float:
        return a-b
    
    def _multiply(self,a:float,b:float)->float:
        return a * b
    
    def run(self, op:str,a:float,b:float)->float:
        if op in self._operation:
            return(self._operation[op](a,b))
        else:
            raise ValueError(f"{op}不在方法字典内")
    pass
if __name__ == "__main__":
    calc = calculator()
    print(calc.run('add',10,5))
    print(calc.run('suntract',10,5))
    print(calc.run('multiply',10,5))







