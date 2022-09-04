import random


# def pai():
#     list1 = ['♠', '♥', '♦', '♣']
#     list2 = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
#     list3 = ["Big", "Low"]
#     list4 = [x + y for x in list1 for y in list2]
#     list4.extend(list3)
#     return list4


class Puke:
    @staticmethod
    def pai():
        list1 = ['♠', '♥', '♦', '♣']
        list2 = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
        list3 = ["Big", "Low"]
        list4 = [x + y for x in list1 for y in list2]
        list4.extend(list3)
        return list4

    @staticmethod
    # 底牌
    def di_pai(list):
        dipai = []
        total = 53
        for i in range(3):
            di_pai = list.pop(random.randint(0, total))
            dipai.append(di_pai)
            total -= 1
        return dipai, list

    num = [1, 2, 3]
    list = pai()
    di, list1 = di_pai(list)


class User:
    total = 50

    def __init__(self, name):
        self.name = name
        self.num = random.choice(Puke.num)
        Puke.num.remove(self.num)
        self.user = User.distrbute(self, name)
        self.new_user = User.change(self)

    # 判断地主
    def check(self, name):
        if self.num == 1:
            print(f"{name}是地主")
            return True
        else:
            return False

    # 发牌
    def distrbute(self, name):
        user = []
        dizhu = User.check(self, name)
        dipai = Puke.di
        if dizhu:
            user.extend(dipai)
        for i in range(17):
            pop1 = Puke.list1.pop(random.randint(0, User.total))
            user.append(pop1)
            User.total -= 1
        print(f"{name}的牌为:{user}")
        return user

    # 将带有图案的牌转变为数字
    def change(self):
        new_user = []
        for i in self.user:
            new_user.append(i.strip("♦♣♥♠"))
        return new_user

    # 出牌
    def out(self):
        pai = input(f"{self.name}出牌:").strip()
        if pai in self.new_user:
            location = self.new_user.index(pai)
            self.new_user.remove(pai)
            pop1 = self.user.pop(location)
            return pai, pop1
        elif pai == "pass":
            return None, None
        else:
            print("你没有这张牌")
            return None, None


def new_num(pai):
    if pai == "J":
        return 11
    elif pai == "Q":
        return 12
    elif pai == "K":
        return 13
    elif pai == "A":
        return 14
    elif pai == "2":
        return 15
    elif pai == "Big":
        return 17
    elif pai == "Low":
        return 16
    else:
        return int(pai)


def check_pai(user1, user2, user3):
    global begin, pai1, reslut
    for x in range(1, 4):
        for i in user1, user2, user3:
            if i.num == x:
                pai, out1 = i.out()
                if pai and out1 is not None:
                    if begin >= 1:
                        reslut = compare(pai1, pai)
                        pai1 = pai
                    else:
                        pai1 = pai
                    if reslut:
                        i.user.append(out1)
                begin += 1
    if begin % 3 == 0:
        print(f"{user1.name}的牌为:{user1.user}")
        print(f"{user2.name}的牌为:{user2.user}")
        print(f"{user3.name}的牌为:{user3.user}")


def compare(pai_one, pai_two):
    num = ["A", "2", "J", "Q", "K", "Big", "Low"]
    if pai_one in num:
        pai_one = new_num(pai_one)
    if pai_two in num:
        pai_two = new_num(pai_two)
    if int(pai_one) < int(pai_two):
        pass
    else:
        print("你的牌大不过对方")
        return True


if __name__ == '__main__':
    begin = 0
    reslut = False
    print(f"底牌为{Puke.di}")
    user1 = User('张三')
    user2 = User("李四")
    user3 = User("王二")
    while True:
        check_pai(user1, user2, user3)

































