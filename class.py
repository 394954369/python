#!/usr/bin/python

```
class person:

    def __init__(self, name, caption, leader, pri):
        self.name = name
        self.caption = caption
        self.leader = leader

        #两个下划线表示属于私有字段,外部对象无法直接调用
        self.__pri = pri

    a = person('yyp')

    def sports_meet(self):

    @staticmethod
    def Foo():

    @property
    def Bar(self):
        print "this is a property"

    def __sha(self):
        #两个下划线表示的是私有方法
        print "this is a pri function"

    #怎么调用私有方法,外部就可以直接用这个公有的方法进行调用

    def shaaa(self):
        self.__sha()

    #怎么调用私有的字段,外部想调用私有的字段就可以使用这种进行调用
    @property
    def pri(self):
        print self.__pri

    japan =  person('上海', '小小', 'leader', 'pri')
japan.pri #这样就可以直接调用私有字段
japan.shaaa() #这样就可以直接调用该方法
japan._person.__sha() #第一个用一个下划线,接类名,然后两个下划线接私有方法


```

#关于call 方法

class Foo:
    def __init__(self):
        pass

    def GO(self):
        print "go"

    def __call__(self):
        print "call"
    def __del__(self):
        print "执行完成后会自动释放"

f1 = Foo() #执行—__init__ 方法
f1.GO()   #执行go 方法
f1()      #()对象后面直接 () 表示执行__call__ 方法
