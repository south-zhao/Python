'''
a = {
    '老杨':{'姓名':'老杨','年龄':18,'爱好':['唱歌','打篮球',['中国风歌曲']]}
}
索引和根据键取值，修改值
1. 输出老杨的第二个爱好
2. 将老杨的中国风歌曲改成rap
print(a['老杨']['爱好'][1])
a['老杨']['爱好'][2][0]= 'rap'
a['老杨']['爱好'][-1][0]= 'rap'
a['老杨']['爱好'][-1][-1]= 'rap'
# 实现一个功能  方式可能是多种的  不一定唯一的


选择合适的数据类型，定义一个变量来表示自己的名字，年龄，爱好
laoyang = {'名字':'老杨','年龄':18,'爱好':['打篮球']}

以下代码有什么问题？避免思维误区
_1 = 2
12  = 3
int = python
a = [1,[[2]
b = {[1]:1}
c = {11,22:33}
'''
# 需要注意的   索引越界   得不到没有的数据
# a  = [1,2,3]
# print(a[-4])
# 会发生什么   结果是什么？  ===》  报错
# a = {1:2}
# print(a['hahah'])  # 字典中没有这个键

'''
变量的命名规范    基本的思维    
1. 只能是字母数字下划线组合而成   
2. 数字不能开头        
3. 不能是Python的关键字
import  keyword
print(keyword.kwlist)
'''
'''
用户交互
    什么叫做用户交互    
    输入   我将信息给计算机        input()
    输出   计算机将信息给我   打印  print()  更多的用法
输入数据的目的  为了得到一个数据，使用这个数据   
input()
    1.当程序执行到这个代码的时候，就会卡住，等待你输入信息给计算机 
    输入信息以后，敲个回车   程序才继续往下走 
    2. input() 会将你输入的数据 获取到  我们可以用变量保存起来，以后使用   
    3. 可以给出一些提示信息    input(提示信息)
    4. input() 接受的数据永远是str字符串类型   
# print(11)
a = input('请输入您的账号')
print(a)
print(type(a)) 
'''
'''
输出  print()   将数据打印输出到屏幕上      
    1. 可以同时输出多个数据    print() 里面可以同时输出任意个数的任意类型数据  用,号隔开
    2. 可以指定用什么符合隔开多个数据  print(数据,sep='你自己的符号')  默认是空格
    3. 写一个print()  会换行    本质是在print() 这里面的数据之后自动加了一个换行符
        print(1,end='我是结尾')   这一个数据打印完后，不会换行，而是以你的字符结尾
基本上不会去更改，以默认为主
'''
# print(1)
# print('1\n\n\n\n\n\n\n')
# print([1])
# print(1,'1',[1])
# 1 1 [1]
# 每一个数据用空格隔开的
# print(1,2,3,4,sep='中文')
# 1+2+3
# print('1\n*3',end='我是结尾')
# print(2)
'''
格式化输出              将变量和字符串组合到一起去      
    xxx先生，您的余额是XX
按照格式输出的字符串        
'''
name = '老杨'
money = 100
# print('xxx先生，您的余额是XX')
# 老杨先生，您的余额是100
# 3种方式
# %  占位的方式
# print('%s先生，您的余额是%s'%(name,money))
# print('%s先生，您的余额'%(name))
# print('%s先生，您的余额'%name)
# format
# print('{}先生，您的余额是{}'.format(name,money))
# print('{1}先生，您的余额是{0}'.format(money,name))
# {1}  (money,name)  第二个名字
# {0}  (money,name)  第一个名字
# 3.5以后的   需要记住的
# print(f'{name}先生，您的余额是{money}')
# 需要用到变量的地方，就用{变量名}，这个字符串前面需要有一个f
# a = '老杨'
# b = 18
# c = ['篮球']
# # 打印一句话，
# # XXX,今年XX岁，爱好是XXX
# print(f'{a},今年{b}岁，爱好是{c}')
# print(f'{a*3},今年{b+10}岁，爱好是{c}')
# 以后会大量的使用到   6   暂停了

'''
运算符  
    算术运算符  + - * / // %  **
    比较运算符  > < >= <= != == is is not  
    赋值运算符  =  += -= *= /= //= %=  **=
链式赋值
      变量名 = 变量名 = 具体的值  
a = 10
b = a
c = b
print(a,b,c)
# 10   10  10
a = b = c  = 10k
print(a,b,c)
交叉赋值  
    变量名1,变量名2...  = 数据1,数据2...
    需要注意的地方  = 左边的个数和右边要相等  
    按照对应关系来的
    变量名1 = 数据1
    变量名2 = 数据2
a = 10
b = 8
# 我需要让 a,b 交换数据   需要借助于第三个变量
# c = a
# a = b
# b = c
# print(a,b)
# a,b = b,a
# print(a,b)
a  = 1
b = 2
c = 3
d = 4
a,b,c,d = a,a,a,a
print(a,b,c,d)

解压赋值    
1.   变量名,变量名 = 字符串/列表/字典/元组 
    将字符串的每一个字符依次的去给=左边的变量
    将列表的每一个元素依次的去给=左边的变量
    将字典的每一个键依次的去给=左边的变量
    将元组的每一个元素依次的去给=左边的变量   
    必须一一对应    
2. *_  可以用来接受剩余的数据    
变量名可以少于=右边的数据个数，因为可以用*_接受其余的

# a = [1,2,3]
# a = {'name':'老杨','age':18,'sex':'帅哥'}
# a = '123'
# a = (1,2,3)
# a  = 123   # 数字是不可分割
# b = a[0]
# c = a[1]
# d = a[2]
# print(b,c,d)  # 将列表中的每一个元素分别绑定给别的变量
# b,c,d = a  # b,c,d = [1,2,3]
# # 如果是字典，就分别得到字典的键   ==》 字典 根据键去取值的
# print(b,c,d)
# print(a[b],a[c],a[d])
# a,b,*_ = [1,2,3,4,5,6,7,8,9]
# *_,a,b = [1,2,3,4,5,6,7,8,9]
# a,*_,b = [1,2,3,4,5,6,7,8,9]
# a,*_,b,c,d = [1,2,3,4,5,6,7,8,9]
# print(a,b,c)
# print(*_)
# 问题  不需要去考虑Python的语法  假设问你自己  假设你自己是机器  你能懂吗？
# a,b,c = [1]
# print(a)  # 报错 
'''

'''
逻辑运算符    
    与  或  非  
and    与   左边  与 右边  两个同时都是对的  结果才是对的  只要有一个错了，结果是错的
or     或   左边  与 右边  有一个是对的     结果就是对的  两个都错 结果是错的
not    非   以前是对的，现在就错了，以前是错的，现在就对了
print(True and True)  # True
print(True and False) # False
print(False and True) # False
print(False and False)# False

print(True or True)  # True
print(True or False)  # True  
print(False or True)  # True
print(False or False)  # False

print(not True)  #  False
print(not False) #  True
'''
# 有一些教程出现这个问题  注意 ：
# and  or  not  的结果一定是个bool值
# print(1 and 100)  100
# print(0 and 100)
# print(0.0 and 100)
# 结果不是True 或者 False
# 短路运算
# and   判断只有两个条件都对，结果才是对的
# 如果左边发现就已经是错的了，还需要去判断右边吗？
# 如果and左边的是对应是错的，那么就直接返回左边的值，因为右边的对错对结果没有影响了
# 如果and左边的是对应是对的，那么就直接返回右边的值，因为右边的对错才是结果
# 怎么去判断对应的是对还是错呢？  True   Flase
# 0,0.0,空字符串，空列表，空字典，空集合，空元祖，None 都对应False
# 其他的都对应True
# print(1 or 0)
# print(0 or 1)
# or 的逻辑 两个有一个是对的，结果就是对
# or 的左边是对的，右边的不用管了  直接输出左边的值
# or 的左边是错的，右边的决定结果  直接输出右边的值
# 总结   逻辑推断关系
# 如果是and   左边对，输出右边，左边错，输出左边
# 如果是or    左边对，输出左边，左边错，输出右边
# 这种方式  我们了解即可  因为在实际开发中
# and  or  not  我们都是用于 判断语句中   最终需要的只是一个结果而已

# 知其然，更知其所以然
# 我们可以只记住最终的结论，但是我们需要了解他的原理

'''
成员运算符
    in  
        判断in左边的数据是不是属于右边的数据    判断是否存在 结果是True或False 
    not in 
        取反
'''
# print('1' in '123')
# print(1 in [1,2,3])
# print('name' in {'name':'老杨'}) # 字典判断的是键
# print('1' not in '123')
# print(1 not in [1,2,3])
# print('name' not in {'name':'老杨'}) # 字典判断的是键

'''
算术运算符    +  -  只用于数学运算   常用的 必须记住  
比较运算符    常用的 必须记住  
赋值运算符
    增量赋值  
    链式赋值   
    交叉赋值   
    解压赋值   函数中会使用更多   
逻辑运算符      用于条件语句
成员运算符   
任务 下课后  一定要去练习     
'''

'''
流程控制
    和其它编程语言一样，按照执行流程划分
    Python 程序也可分为 3 大结构，即顺序结构、选择（分支）结构和循环结构
代码的执行顺序  按照人类的习惯一样  从左到右  从上往下  
你们人类的世界中   做一件事情的流程
    1. 顺序结构    从左到右  从上往下    
    2. 分支结构(选择结构)    根据选择做事情
    3. 循环结构(重复做某件事情)
'''
'''
分支结构    选择
什么是分支结构
分支结构就是根据条件判断的真假去执行不同分支对应的子代码
1.2 为什么要用分支结构
人类某些时候需要根据条件来决定做什么事情，比如：如果今天下雨，就带伞
所以程序中必须有相应的机制来控制计算机具备人的这种判断能力  
如何使用分支结构 
'''
# 如果 条件
#     要做的事情1  # 只有条件成立了  我才会做事情1
# 要做的事情2   # 事情2和条件成不成立没有任何关系
# 会导致，如果条件成立了，那么我到底是做事情1和2 还是只做事情1
# if True:  # True
#     print(111)
# print(666)
# Python的单分支的语法规定
# if 条件:
#     任意的符合规范的代码
# 单分支
# 只有if 后面的条件成立了，才会执行if里面的代码
# 条件不成立，则不会执行
# 判断条件成立与否  可以是 True ，Flase
# 0,0.0,空字符串，空列表，空字典，空集合，空元祖，None 都对应False
# 其他的都对应True
# 需要注意的是，缩进量必须一样 我们规范是一个TAB 键 ==4个空格键
# 不要空格键和tab键混合使用
# if True:  # True
#     print(111)
#     print(222)
# print(666)
# 为什么需要有缩进  666 没有缩进 意味着和条件无关
# 选择做或者不做   条件成立就做  条件不成立就不做
# 如果 条件1:
#     我做事情1
#     如果 条件2:
#         我就做事情2   要不要做是不是取决于条件2的结果      嵌套关系了
# 将这些我敲过的代码理解 吃透


# 题目：
# 提示用户，让用户输入账户和密码，
# 如果账户是admin，密码是123，就打印XXX恭喜您登陆成功

# 让用户输入自己的名字
# 如果用户输入的是 张三，李四，王五，三者其中一个，就提示XX已经注册过




