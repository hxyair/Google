class Cat():
    leg_number = 4
    def __init__(self, name, age, fur, height, weight):
        self.name = name
        self.age = age
        self.fur = fur
        self.height = height
        self.weight = weight

tom_cat = Cat("Tom", 2, "white", 0.4, 2.1)
jerry_cat = Cat("Jerry", 3, "yellow", 0.5, 3.2)
print("{}原来的腿数量是{}".format(tom_cat.name, tom_cat.leg_number))
print("{}原来的腿数量是{}".format(jerry_cat.name, jerry_cat.leg_number))
Cat.leg_number = 3
print("哦，所有的猫咪发生了变异，{}现在的腿数量是{}" .format(tom_cat.name, tom_cat.leg_number))
print("哦，所有的猫咪发生了变异，{}现在的腿数量是{}" .format(jerry_cat.name, jerry_cat.leg_number))

class BankAccount():
    interest_rate = 0.04
    def __init__(self, name, this_id, password, money):
        self.name = name
        self.this_id = this_id
        self.password = password
        self.money = money
tom_account = BankAccount("Tom", "12345", "000000", 1000)
jerry_account = BankAccount("Jerry", "54321", "888888", 2000)
print("对于{}来说，原来的利率是{}" .format(tom_account.name, tom_account.interest_rate))
print("对于{}来说，原来的利率是{}" .format(jerry_account.name, jerry_account.interest_rate))
BankAccount.interest_rate = BankAccount.interest_rate + 0.01
print("对于{}来说，现在的利率是{}" .format(tom_account.name, tom_account.interest_rate))
print("对于{}来说，现在的利率是{}" .format(jerry_account.name, jerry_account.interest_rate))



class BankAccount(object):
    interest_rate = 0.05
    def __init__(self, name, this_id, password, money):
        self.name = name
        self.this_id = this_id
        self.password = password
        self.money = money
    # 定义了一个修改密码的实例方法
    def change_password(self, new_password):
    	self.password = new_password
        # 请你补充以下代码，将实例变量self.password赋值为输入参数new_password
        
tom = BankAccount("Tom", "123456", "123456", 1000)
print("{}原来的密码是{}".format(tom.name, tom.password))
tom.change_password('666666')
print("{}现在的密码是{}".format(tom.name, tom.password))


class BankAccount(object):
    interest_rate = 0.05
    def __init__(self, name, this_id, password, money):
        self.name = name
        self.this_id = this_id
        self.password = password
        self.money = money

    # 提高利率的静态方法
    @staticmethod
    def raise_interest(money, rate):
        if money >= 1000000:
            print("大客户，利率提高百分之2。")
            rate += 0.02
        return rate

    # 存款的实例方法
    def save_money(self, money):
        self.money = self.money + money
        # 调用静态方法
        self.interest_rate = self.raise_interest(self.money, self.interest_rate)

tom = BankAccount("Tom", "123456", "888888", 1000)
print("{}原来的存款利率为{}".format(tom.name, tom.interest_rate))
# 调用实例方法
tom.save_money(1000000)
print("{}现在的存款利率为{}".format(tom.name, tom.interest_rate))


class BankAccount(object):
    interest_rate = 0.05
    def __init__(self, name, this_id, password, money):
        self.name = name
        self.this_id = this_id
        self.password = password
        self.money = money

    # 提高利率的静态方法
    @staticmethod
    def raise_interest(money, rate):
        if money >= 1000000:
            print("大客户，利率提高百分之2。")
            rate += 0.02
        return rate

    # 存款的实例方法
    def save_money(self, money):
        self.money = self.money + money
        # 调用静态方法
        self.interest_rate = self.raise_interest(self.money, self.interest_rate)

tom = BankAccount("Tom", "123456", "888888", 1000)
print("{}原来的存款利率为{}".format(tom.name, tom.interest_rate))
# 调用实例方法
tom.save_money(1000000)
print("{}现在的存款利率为{}".format(tom.name, tom.interest_rate))

jerry = BankAccount("Jerry", "123457", "999999", 1000)
print("{}原来的存款利率为{}".format(jerry.name, jerry.interest_rate))
jerry.save_money(100)
print("{}现在的存款利率为{}".format(jerry.name, jerry.interest_rate))



class BankAccount(object):
    interest_rate = 0.05
    def __init__(self, name, this_id, password, money):
        self.name = name
        self.this_id = this_id
        self.password = password
        self.money = money
    @classmethod
    def change_interest_rate(cls, x):
        cls.interest_rate = cls.interest_rate + x
tom = BankAccount("Tom", "123456", "888888", 1000)
print("银行账户类原来的类变量interest_rate是{}".format(BankAccount.interest_rate))
# 补充下面一行代码，使用实例调用类方法
BankAccount.change_interest_rate(-0.02)
print("银行账户类现在的类变量interest_rate是{}".format(BankAccount.interest_rate))