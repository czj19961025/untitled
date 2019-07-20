'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    pass
# 定义一个对象
mingyue = Student()

# 定义一个类，用来描述听python课程的学生
class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("我在做作业啦")
        return
# 实例化一个叫yueyue的学生
yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.name)
yueyue.doHomework() #此处没有传入参数
