'''
先讲一个知识点  闭包
在讲完闭包之后  ===》推导一个知识点出来 ==》装饰器
这个装饰器  我们只需要要记住的是他的结论   因为这个结论就是一个模板，我们以后会用到
但是这个推导的过程  结合我们所学的函数的知识点  (如果这个推导的过程都看懂了)
学习  
推导的过程是环环相扣的  如果其中一环没懂，后面就导致错误  

课上一定不要记笔记，带上脑子思考就可以了
一旦记笔记 ，可能知识点就错过了 
闭包   封闭  包裹
函数内部可以写符合语法规范任意的代码    函数内部也可以定义函数  调用函数

闭包函数：
    闭：内嵌函数     在一个函数里面定义函数
    包：里面的那个函数 用到了外层的函数的名字
闭包函数：
    在函数里面用到了外层函数的名字
'''''
# c  =  1   # 思考还有没有其他方式？
# def a(c): # 本质  自动的在函数内部  c = 2
#     # c = 1
#     # b()   # 还没定义呢？
#     def b():
#         # c = 1
#         print(c)
# b()   # 可以的，就变成死循环了
# b()
# b()    # 写在这里为什么不行？   全局作用域不能用局部的名字
# a(2) # 没有打印的原因是什么？  定义函数会执行代码
# 请问  调用b函数，b() 这个代码可以写在任意的位置吗？
#
# 函数b里面没有c这个名字会怎么办？    作用域： 自己函数内部没有，就怎么办？
# 函数a里面也没有c这个名字呢？
# def a(c):
#     def b():
#         print(c)

# 闭包函数   在函数内部又定义了一个函数 用到了外层函数的名字
# 闭包函数的意义  得到了一种为函数传参的另外一种方式
# 直接传递参数    不能够直接传参了
# def c(b):
#     def a():
#         print(b)   # 在函数内部要使用一个名字
#     a()
# c(3)    # 闭包的意义  得到了另外一种为函数传参的方式了
# 思考下：也行  有区别没有？
# 闭包  什么是闭包  多了个手段，可以为函数传参

'''
装饰器    特殊的函数
    器：功能   函数 
    装饰:  添加额外的东西，不影响以前的   
一个可以将你原来的函数添加一些功能的函数 
为什么要用装饰器：
假设你现在开发了一个视频网站       不需要登录的   直接执行这个函数
业务更改了： 需要登录了  才能看这个视频    ===》才能触发这个功能  
需要付费才能看   
就要更改原来的代码了   
这种方式好不好？   
开发中：规范  
开放封闭原则    对功能是开发的  对修改是封闭的
你的程序的功能是可以变动的    
不能直接改原来的代码     
提出了一个要求：可以在不更改源代码的基础上，增加功能  
装饰器：
就是在不更改你源代码的基础上，增加一些功能
函数的源代码  ：定义函数   调用函数 
在不更改你定义函数的代码以及调用函数的代码的基础上，给你的函数增加功能
      
'''
# 推导过程如下
# def a():
#     print('正在观看Python学习视频')
#
# a()
# 需求1： 执行原来的功能以前，先打印一句话，登陆了  执行完了之后，打印一句话，看完了
# 不好的地方出现没有  代码冗余了


# print('登陆了')
# a()
# print('看完了')
# print('登陆了')
# b()
# print('看完了')

# 优化一下
# def outer(inner):
#     def func(*args,**kwargs): # inner = 函数C的内存地址
#         print('登陆了')
#         inner(*args,**kwargs)    # 函数C的内存地址()    执行函数c   有可能有，有可能没有
#         print('看完了')


#
# a = func(a)  # 执行函数func 将它的返回值绑定给a   返回一个函数的内存地址
# a()
# 参数的个数不确定  形式不确定 ===》可变长度参数   *args,**kwargs
# func(a) #  变化了  埋一个伏笔  调用函数的方式变化了  坑
# a()  # 以前的写法
# 优化了一下了   参数可以变动了     开放封闭原则  定义函数的代码不能改  调用函数也不能改
# 功能还要增加
# c('Django')  # 函数C的内存地址(参数)
# func(c)
# func(a)
# func(c,'dajngo')
# 函数func(函数C的内存地址)
# 执行函数func
# 1. 解决了参数不确定的问题   参数的问题
# 调用函数的方式变化了     这个怎么解决呢？
# a()
# a = func(a)  # 执行函数func 将它的返回值绑定给a   返回一个函数的内存地址
# a()         # func的返回值()    函数的内存地址()   a()
# c = func(c,'django')
# c()


'''



'''
# def inner(wraper):
#     def outer(*args,**kwargs): # 可以接收任意多个，任意形式的参数
#         res = wraper(*args,**kwargs)  # 这里需要一个动态变化的名字  这个名字哪里来？
#         return res
#     return outer
# @inner
# def a():
#     print('正在观看Python学习视频')
#
# def b():
#     print('正在观看前端学习视频')
#
# # @inner
# def c(d): # 有参数的函数了
#     print(f'正在观看{d}学习视频')
#     return 666
# a()
# c = inner(c)   # 执行函数inner 得到inner的返回值   绑定给c
# d = c('Django') # inner的返回值()      内存地址
# # d = c('Django')      # 执行函数c 得到函数c的返回值   2
# print(d)
# 以前的函数  参数不确定  以前的函数 有返回值  也解决了
# 不管你以前的函数 有没有参数 有没有返回值  都解决了
# 还不够完善  还可以更完善   以前的函数 有可能有返回值
# return outer()
# 真正的执行功能 是outer这个函数
# 但是在外面可以直接用outer这个名字吗？

# outer(c,'django')    # 会产生一些问题出来  但是我有需要这么一个参数
# c('django')
# 只用到了  可变长度参数
# 现在的问题是  a  写死了


# 闭包  需要用到一个名字  自己不能传递  就找外面要
# def a(c):
#     def b():
#         print(c)
#     return b
# # b()     # 全局不能用局部的名字  但我就是需要这个名字啊
# #
# b = a(1)   # 执行函数a 将a的返回值丢出来  返回值 函数b的内存地址
# b()        # 执行函数b

# b()   # 会报错 因为全局没有b这个名字  必须先登录才能看
# def inner(func):
#     def outer(*args,**kwargs):
#         if 3>1:
#             print('可以看')
#             res = func(*args,**kwargs)  # 执行你以前的功能
#             print('看完了')
#             return res
#         print('您还没有登陆，不能使用这个功能')
#     return outer
#
# @inner
# def xiaopin():
#     print('正在看小品')
#
# @inner
# def dianying():
#     print('正在看电影')
#
# xiaopin()
# dianying()

# 我们需要记住的是：  最简单的格式
# def inner(wraper):
#     def outer(*args,**kwargs):
#         res = wraper(*args,**kwargs)  # 表示执行以前的功能
#         return res
#     return outer
# 使用装饰器 就是在需要添加这个装饰器的功能的函数上面加一句   @装饰器的名字

# 快速的回顾总结下装饰器的推导过程  有一环你漏掉了的  总结  下课了，回顾
# 装饰器的推导过程是绕  比较晕  我们需要记住的是模板
# def c1(b1):
#     def a1(*args,**kwargs):# 以前的函数可能有参数    参数的个数不确定
#         # 就可以解决以前的函数的参数问题
#         res = b1(*args,**kwargs)   #   执行以前的函数  得到以前的函数的返回值
#         return res  #   将以前的函数的返回值 返回出去
#     # 我们真正需要执行的是函数a
#     return a1
# # 解决了 参数的问题
# # 解决了返回值的问题
# # 解决了以前的函数写死问题
# @c1
# def b():
#     return  111
#
# b()
'''
装饰器  是对作用域，函数对象，参数，返回值  的总体的结合的总结
对于装饰器   我们以后需要做到的是  记住这个模板和使用的规则
但是为了增强我们对函数的知识点的理解和吃透，我们需要理解这个推导过程
自己不看视频去推导一遍   
注意点：
函数名       函数的内存地址
函数名()     执行这个函数，并且得到这个函数的返回值
可变长度参数
返回值的运用   
闭包   给我们提供了一种不需要直接传参，一样可以使用外层的参数的方式
def a(b):
    def c():
        print(b)
    return b
b = a(1)
b()  
直接在全局中 使用局部的函数     局部的函数可以不直接传参得到外层的可变的数据 
 
'''


def c1(b1):
    def a1(*args, **kwargs):  # 以前的函数可能有参数    参数的个数不确定
        # 就可以解决以前的函数的参数问题
        res = b1(*args, **kwargs)  # 执行以前的函数  得到以前的函数的返回值
        return res  # 将以前的函数的返回值 返回出去

    # 我们真正需要执行的是函数a
    return a1


@c1
def a(num):
    print(f'{num}正在观看Python学习视频')
    return 888


def inner():
    def b():
        print('正在观看前端学习视频')

    return b


d = a(2)
print(d)

