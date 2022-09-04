"""
字符编码？
解决一个问题： 如何让电脑看懂你的文字
解决乱码的现像
回顾一个知识点
    一个程序要想运行
    先从 硬盘 到 内存 到 CPU
    笔记本  大脑的记忆区域   大脑去思考去判断
计算机(电脑)只能看的懂    0,1   二进制数据
但是我们人，看得懂各种文字和符号
我              老外
中文            英语
需要翻译     将我的中文翻译/转换成英文

人          电脑
中文        0101011
也需要进行翻译/转换   让电脑能理解我们人类的文字和符号

人类的文字和符号     转换的表格    计算机能看懂的二进制
转换的表格  ===》  字符编码表
字符编码： 参照一个标准，将人类的字符翻译成计算机能理解的二进制语言
编码:翻译/转换的意思
计算机最开始是美国人发明的  英文的
26小写字母  大写字母  符号

单位的换算
计算机最小的单位  比特位    0   1     bit
8个比特 =  1个字节
1024个kb  =  1M
1024M = 1G
1024G = 1T
2的多少次方的换算
16G   计算机中的换算  二进制

字符编码经历了三大阶段
1. 一家独大
    最开始计算机是美国人发明的，只需要考虑计算机能不能看懂英文
    ASCII表
对应了所有的英文字符以及一些符号，阿拉伯数字和二进制的对应关系
计算机就能看懂英文了
在ASCII表中的任意一个字符  都占据一个字节  ==》8个比特
2. 诸侯割据，天下大乱
    其他的国家也需要用计算机
    中国人要需要计算机能看懂中文
    ASCII之后进行扩展，以前的不变
    一个字节  256中不同的字符
    2**16次方
    GBK 的字符编码表
        1. 在ASCII的表格之上进行扩展
        2.  计算机能看懂 阿拉伯数字，英文字符(以前ASCII表里面的字符)
            再加上汉字
        3.  GBK 每一个字符占据了两个字节
    日本人也要用计算机
    套路是一样的  只做自己的字符编码表  shift-jis
    不同的国家，都有自己的字符编码表，都是在ASCII表后面扩展的
    导致了一个现象，各个国家有各个国家的字符编码表，所以就可以让计算机看的懂
    英文和自己国家的文字
天下大乱  乱码就出现了
字符编码不用，翻译不出来     乱码
任何一项技术的诞生  都是为了解决一个实际存在的问题的

阶段3  分久必合
    字符编码： unicode
    1. 它存在所有的字符和数字的对应关系 ==》兼容万国字符
    2. 他和传统的字符编码的二进制有对应关系

1990 发明的一个字符编码表
1990年以前  就已经有用其他的字符编码写的文件

unicode  有个特定   固定使用两个字节来表示一个字符

文件    100个字母      ASCII     大小是多少  ： 100个字节
文件    100个字母     unicode    大小是多少  ： 200个字节

就因为字符编码的不一样，大小就直接翻倍

utf-8  变长的  根据文字的不同，每一个文字占据的字节也不一样
    1. 如果是ASCII   用一个字节来表示
    2. 如果是汉字     用三个字节

所以：
    1. utf-8
    2. GBK  更省空间
我们需要记住的一点就是:
    我们以后使用字符编码，推荐使用utf-8

假如没有了字符编码 ===》 计算机看不懂你的文字
注释 ===》Python解释器不会运行
修改一份文件
硬盘 ==》内存 ==》CPU ==》内存 ==》硬盘

编码：从内存到硬盘
解码：从内存到硬盘

当你的编码和你的解码的字符编码标准不一样的 时候，就会出现乱码现像了
所谓的乱码现像就是因为编码和解码的标准不一样导致的
如何避免乱码现像: 编码和解码要同一个字符编码
utf-8

1. 编码和解码，推荐都使用UTF-8
2. 如果有乱码，你就将你的编码或者解码换成同一个

字符串.encode()    编码
字符串.encode(字符编码)    编码
按照你写的字符编码去对这个字符串编码，默认不写就是utf-8
字节.decode()    解码
字节.decode(字符编码)    解码
按照你写的字符编码去对这个字符串解码，默认不写就是utf-8

''"""
# a = '我'
# print(a.encode())
# print(a.encode('utf-8'))  # 三个字节
# print(a.encode('gbk'))  # 两个字节
# 一串二进制的数字
# b = a.encode('gbk')
# 将二进制的数字变成字符
# print(b.decode('shift-jis'))
# print(b.decode('utf-8'))

'''
文件
1. 什么是文件？文件的本质是什么？
    电脑中的文件 ： 电脑中永久保存数据的载体     
    对应的硬盘     外存
    有了操作系统之后，才有文件这个概念   
    文件：操作系统给我们提供的一个永久的保存数据的形式 ，保存在外存上的 
    一段硬盘的区域     
2. 为什么要有文件？
    没有了文件，会怎样？    
    数据就不能永久保存了    失去了永久承载数据的载体  
3. 都有什么文件？
    文件的本质： 操作系统帮我们在外存上刻录的一堆的01010 的数据
    文件：二进制的数据
    所有的文件都是二进制的文件 ：  
    其实在这些文件中，有一种特殊的文件 需要字符编码：因为有文字
    文本文件
    有文字的文件，需要字符编码才能展示，所以文本文件

操作文件
    到底操作的是什么？===》硬盘的一块区域      
那么我们操作文件都需要那些步骤    必须要有的三个步骤   
1. 得到那块硬盘的空间 
2. 操作那块区域   写  看  
3. 还回去 

我们现在操作文件有哪些是必须的？
1. 文件路径  (你要操作哪一份文件)
2. 你要进行什么操作  操作模式是什么  
3. 如果是文本文件，那你还需要告诉操作系统，你要使用什么字符编码，如果是文本文件
    又不要字符编码，电脑就看不懂了啊
    如果不是文本文件，就不要有字符编码
变量=open()      打开一份文件  
这个返回的变量 ===》理解成操作系统给你的那个硬盘的区域  
open(文件的路径)  
文件路径： 根据这个路径可以找到这个文件
路径分为两大类
    绝对路径:  不管你这份文件在哪里，都可以利用绝对路径找到对应的文件
    中国/湖南/长沙/岳麓区 
    D:/1/2.txt      
    相对路径: 以你现在的这份文件为参照物，找到对应的文件
    在你的前面那条街/后面的斑马线  
    ./第三天.py        在第八天这个文件的同一个文件夹里面
    第三天.py
    ./   当前的文件夹
    ../  上一级的文件夹  
open(文件的路径,操作的模式) 
操作的模式
b   二进制文件   
t   这是一份文本文件  默认不写，就是文本文件的意思
w   覆盖写     
    如果你的这份文件不存在，就创建这个文件，然后在这个文件里面写数据
    如果你的这份文件存在，就将这份文件里面的内容删除掉，然后写数据
    注意的是：只能帮你创建文件，不能创建文件夹   
a   追加写
    如果你的这份文件不存在，就创建这个文件，然后在这个文件里面写数据
    如果你的这份文件存在，就再以前的数据的后面去增加
    注意的是：只能帮你创建文件，不能创建文件夹   
r   读取
    如果你的这份文件不存在，就报错    
    如果存在，就可以读取里面的数据了
wb  ab   rb  以什么模式操作二进制文件
wt  at   rt  以什么模式操作文本文件
w   a    r   以什么模式操作文本文件   

如果是文本文件，意味着需要字符编码  
open(文件的路径,操作的模式)
如果是文本文件，有没有指定字符编码，那么就会按照你当前的
操作系统的默认的字符编码来    
在windows默认是GBK 在linux才是utf-8 

如果是二进制的文件，就不能写字符编码  会报错  

f = open()   找操作系统要一块硬盘的空间 得到硬盘的空间，用一个变量接受下
文件的路径
操作的模式
w/wt   以覆盖写的方式去操作一份文本文件，
a/at   以追加写的方式去操作一份文本文件，
r/rt   以读取的方式去操作一份文本文件
wb     以覆盖写的方式去操作一份二进制文件，
ab     以追加写的方式去操作一份二进制文件，
rb     以读取的方式去操作一份二进制文件，

如果是文本文件，就需要指定encoding='utf-8'

操作文件
写文件   open之后接受的那个变量.write(字符串)
        硬盘的区域.write(字符串)
        文件对象.write(字符串)
要将这个字符串刻录进那个硬盘的区域
如果是写，那么在open的时候，就必须是w或者a的模式 
读文件   变量 = open之后接受的那个变量.read()
        变量 = 硬盘的区域.read()
要将那块硬盘区域里面的数据拿到  ，为了方便以后使用，就用一个变量接受
如果是读，那么在open的时候，就必须是r的模式 


关闭文件
open之后接受的那个变量.close() 
硬盘的区域.close()  
'''
# f = open('哈哈哈.txt','w',encoding='utf-8')
# f = open('哈哈哈.txt','w')
f = open('哈哈哈.txt','w',encoding='utf-8')
f.write('1111111111我要写一句话11111111111111')
# data = f.read()
# print(f.read())
f.close()
'''
今天的重点就是立即这四行代码
任务：
用python的代码 实现一下的需求
1.以覆盖写的方式  创建一份文件  文件里面写的数据是 '我的名字是XX'
2. 读取1当中的文件的内容
3. 将2中读取到的内容以追加写的方式 写入到另外一份文件 


886  散朝了  晚安  
'''


