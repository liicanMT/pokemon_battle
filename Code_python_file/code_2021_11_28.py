import time
import random
print("当前游戏版本：1.4\r\n作者：liican\r\n更新日期：2021.8.24")
time.sleep(2)
print("\r\n\r\n")
time.sleep(1)


# coding=utf-8
# 所有备注"edit_admitted"的行，可进行文本编辑
hp = 300    # 己方hp  # edit_admitted
hpe = 300   # 对方hp  # edit_admitted
med1 = 3  # 第一种药的数量  # edit_admitted
med2 = 3  # 第二种药的数量  # edit_admitted


# 储存精灵名称的字典文件
pokemon_dict = {"pokemon_name_1": "耿鬼",
                "pokemon_name_2": "皮卡丘",
                "pokemon_name_3": "幸福蛋",
                }


# 储存对手精灵数据的字典文件
e_dict = {"e_name_1": "喷火龙",
          "e_name_2": "暴鲤龙",
          "e_name_3": "巨沼怪"
          }


#己方精灵技能的字典
## 耿鬼技能字典
pokemon_1_skill_dict = {"skill_1_name": "影子球",
                        "skill_1_overview": "必然命中，造成70点伤害",
                        "skill_1_demage": 70,
                        "skill_1_acc": 1,
                        "skill_2_name" : "十万伏特",
                        "skill_2_overview": "90%命中，造成120伤害",
                        "skill_2_demage": 120,
                        "skill_2_acc": 0.9,
                        "skill_3_name" : "催眠术(未实装)",
                        "skill_3_overview": "0",
                        "skill_3_damage" : 0,
                        "skill_3_acc": 0,
                        "skill_4_name" : "食梦(未实装)",
                        "skill_4_overview": "0",
                        "skill_4_demage": 0,
                        "skill_4_acc": 0,
                        }  


## 皮卡丘技能字典
pokemon_2_skill_dict = {"skill_1_name" : "电光火石",
                        "skill_1_overview": "必然命中，造成60点伤害",
                        "skill_1_demage": 60,
                        "skill_1_acc": 1,
                        "skill_2_name" : "十万伏特",
                        "skill_2_overview": "90%命中，造成120伤害",
                        "skill_2_demage": 120,
                        "skill_2_acc": 0.9,
                        "skill_3_name": "电磁波(未实装)",
                        "skill_3_overview": "0",
                        "skill_3_demage": 0,
                        "skill_3_acc": 0,
                        "skill_4_name":"地球上投",
                        "skill_4_overview": "必定命中，对敌人造成固定的100点伤害",
                        "skill_4_demage": 100,
                        "skill_4_acc": 1
                        }


## 幸福蛋技能字典(未完成)
pokemon_3_skill_dict = {"skill_1_name" : "电光火石",
                        "skill_1_overview": "必然命中，造成60点伤害",
                        "skill_1_demage": 60,
                        "skill_1_acc": 1,
                        "skill_2_name" : "十万伏特",
                        "skill_2_overview": "90%命中，造成120伤害",
                        "skill_2_demage": 120,
                        "skill_2_acc": 0.9,
                        "skill_3_name" : "电磁波(未实装)",
                        "skill_3_overview": "0",
                        "skill_3_demage": 0,
                        "skill_3_acc": 0,
                        "skill_4_name" : "地球上投",
                        "skill_4_overview": "必定命中，对敌人造成固定的100点伤害",
                        "skill_4_demage": 100,
                        "skill_4_acc": 1
                        }


# 敌人技能的字典
## 喷火龙技能字典
e_1_skill_dict = {"skill_1_name": "喷射火焰",
                  "skill_1_overview": "喷射出火焰，70%机率命中，对敌人造成120点伤害",
                  "skill_1_demage": 120,
                  "skill_1_acc": 0.7,
                  "skill_2_name": "火苗",
                  "skill_2_overview": "喷射出小火苗，90%机率命中，对敌人造成60点伤害",
                  "skill_2_demage": 60,
                  "skill_2_acc": 0.9,
                  "skill_3_name": "地球上投",
                  "skill_3_overview": "必定命中，对敌人造成固定的100点伤害",
                  "skill_3_demage": 100,
                  "skill_3_acc": 1,
                  "skill_4_name": "龙之怒",
                  "skill_4_overview": "释放龙族的愤怒，90%几率命中，对敌人造成70点伤害",
                  "skill_4_demage": 70,
                  "skill_4_acc": 0.9,
                  }


## 暴鲤龙技能字典
e_2_skill_dict = {"skill_1_name": "冲浪术",
                  "skill_1_overview": "90%命中，对敌人造成95点伤害",
                  "skill_1_demage": 95,
                  "skill_1_acc": 1,
                  "skill_2_name": "登瀑术",
                  "skill_2_overview": "必定命中，造成60点伤害",
                  "skill_2_demage": 60,
                  "skill_2_acc": 1,
                  "skill_3_name": "地球上投",
                  "skill_3_overview": "必定命中，对敌人造成固定的100点伤害",
                  "skill_3_demage": 100,
                  "skill_3_acc": 1,
                  "skill_4_name": "龙之吐息",
                  "skill_4_overview": "对敌人释放威力巨大的吐息，70%几率命中，造成120点伤害",
                  "skill_4_demage": 120,
                  "skill_4_acc": 0.7,
                  }


##巨沼怪技能字典
e_3_skill_dict = {"skill_1_name": "冲浪术",
                  "skill_1_overview": "90%命中，对敌人造成95点伤害",
                  "skill_1_demage": 95,
                  "skill_1_acc": 1,
                  "skill_2_name": "地震",
                  "skill_2_overview": "95机率命中，造成120点伤害",
                  "skill_2_demage": 60,
                  "skill_2_acc": 0.9,
                  "skill_3_name": "地球上投",
                  "skill_3_overview": "必定命中，对敌人造成固定的100点伤害",
                  "skill_3_demage": 100,
                  "skill_3_acc": 1,
                  "skill_4_name": "冰冻拳",
                  "skill_4_overview": "90命中，对敌人造成90点伤害",
                  "skill_4_demage": 90,
                  "skill_4_acc": 0.9,
                  }


# 游戏前的文字介绍
def shuoming():
    print("游戏介绍：")
    time.sleep(2)
    print("欢迎来到宝可梦对战小游戏——pokemonbattle！")
    time.sleep(2)
    print("本游戏还在测试阶段，难度属于非常简单")
    time.sleep(2)
    print("当然，我也做不出来很难的版本了")
    time.sleep(2)
    print("不管怎样，请努力战胜敌人吧~")
    time.sleep(2)
    print("狭路相逢勇者胜！")
    time.sleep(2)
    print("\r\n\r\n\r\n")
    time.sleep(1)
    print("***警告***\r\n 全程请不要输入英文。只输入数字就好。\r\n\r\n\r\n")
    time.sleep(1.5)


# 错误输入提示
def mess():
    time.sleep(1)
    print("你再别胡输入了\r\n\r\n")


# 挑选己方精灵
# 1 耿鬼
# 2 皮卡丘
# 3 幸福蛋
def select_pokemon():
    a = 0  # 判断while的参数
    global pokemon_skill_dict
    print("\r\n请挑选你的精灵！\r\n\r\n")
    time.sleep(1)
    print("1.耿鬼\r\n  鬼系神奇宝贝，擅长使用鬼系高伤害技能或各类异常状态击败对手\r\n\r\n\
2.皮卡丘\r\n  电系神奇宝贝，擅长使用十万伏特击败对手(￣ε(#￣) \r\n\r\n\
3.幸福蛋\r\n  这个精灵我就8多说了吧，懂得都懂。nb就完事了。\r\n\r\n")  # edit_admitted
    while a == 0:
        main_menu = (input("输入对应数字，选择你出战的精灵\r\n"))  # edit_admitted
        if main_menu.isdigit():
            main_menu = int(main_menu)
        else:  
            print("请输入正确的数字！")
            continue
        if main_menu == 1:
            pokemon_name = "pokemon_name_1"
            judge = input("你选择的是 {0} ,确定吗？（输入y/n）\r\n".format(pokemon_dict[pokemon_name]))  # edit_admitted
            if judge == "y":
                a = 1
                pokemon_skill_dict = pokemon_1_skill_dict
                break
            if judge == "n":
                a = 0
            else:
                print("请输入正确的字母！")
                continue
        if main_menu == 2:
            pokemon_name = "pokemon_name_2"
            judge = input("你选择的是 {0} ,确定吗？（输入y/n）\r\n".format(pokemon_dict[pokemon_name]))  # edit_admitted
            if judge == "y":
                a = 1
                pokemon_skill_dict = pokemon_2_skill_dict
                break
            if judge == "n":
                a = 0
            else:
                print("请输入正确的字母！")
                continue
        if main_menu == 3:
            pokemon_name = "pokemon_name_3"
            judge = input("你选择的是 {0} ,确定吗？（输入y/n）\r\n".format(pokemon_dict[pokemon_name]))  # edit_admitted
            if judge == "y":
                a = 1
                pokemon_skill_dict = pokemon_3_skill_dict
                break
            if judge == "n":
                a = 0
            else:
                print("请输入正确的字母！")
                continue
    return pokemon_dict[pokemon_name]


# 挑选对方精灵
# 1 喷火龙
# 2 暴鲤龙
# 3 巨沼怪
def select_e():
    global e_skill_dict
    a = 0  # 判断while的参数
    print("\r\n请挑选你的对手！\r\n\r\n")
    time.sleep(1)
    print("1.喷火龙\r\n  小智频频逆天究竟为何？是谁只爱睡觉不战斗？一切的答案都在这个精灵的身上！!\r\n\r\n\
2.暴鲤龙\r\n  兄弟们这个东西有多diao我就不说了好吧。nb就完事了\r\n\r\n\
3.巨沼怪\r\n  386的水主，我的最爱之一。属性好打击面广弱点少，看看你怎么打败他吧！\r\n\r\n")
    while a == 0:
        main_menu = (input("输入对应数字，选择你对手的精灵\r\n"))
        if main_menu.isdigit():  
            main_menu = int(main_menu)
        else:
            print("请输入正确的数字！")
            continue
        if main_menu == 1:
            e_name = "e_name_1"
            judge = input("你选择的是 {0} ,确定吗？（输入y/n）\r\n".format(e_dict[e_name]))  # edit_admitted
            if judge == "y":
                a = 1
                e_skill_dict = e_1_skill_dict 
                break
            if judge == "n":
                a = 0
        if main_menu == 2:
            e_name = "e_name_2"
            judge = input("你选择的是 {0} ,确定吗？（输入y/n）\r\n".format(e_dict[e_name]))  # edit_admitted
            if judge == "y":
                a = 1
                e_skill_dict = e_2_skill_dict 
                break
            if judge == "n":
                a = 0
        if main_menu == 3:
            e_name = "e_name_3"
            judge = input("你选择的是 {0} ,确定吗？（输入y/n）\r\n".format(e_dict[e_name]))  # edit_admitted
            if judge == "y":
                a = 1
                e_skill_dict = e_3_skill_dict 
                break
            if judge == "n":
                a = 0
        else:
            print("请输入正确的数字\r\n")
            continue
    return e_dict[e_name]


# 剩余hp，每次行动之后显示
def sy():  
    per_pokemon_hp = int(10 * (hp/100))
    per_e_hp = int(10 * (hpe/100))
    time.sleep(1)
    print("/", "#" * per_pokemon_hp, "-" * (30 - per_pokemon_hp), "/", "{1}  剩余HP:{0} / 300".format(hp, pokemon_name))
    time.sleep(1)
    print("/", "#" * per_e_hp, "-" * (30 - per_e_hp), "/", "{1}  剩余HP:{0} / 300".format(hpe, e_name))
    time.sleep(1)
    print("" * 3)


# 己方战斗函数
def demage(attack, defend, attack_skill_dict):
    i = 0
    while i == 0:
        jineng_number = (input("请输入编号使用技能：\r\n1.{0}（{1}）\r\n2.{2}（{3}）\r\n3.{4}（{5}）\r\n4.{6}（{7}）\r\n5.返回上一级\r\n\r\n".format(attack_skill_dict["skill_1_name"],attack_skill_dict["skill_1_overview"],attack_skill_dict["skill_2_name"],attack_skill_dict["skill_2_overview"],attack_skill_dict["skill_3_name"],attack_skill_dict["skill_3_overview"],attack_skill_dict["skill_4_name"],attack_skill_dict["skill_4_overview"])))
        if jineng_number.isdigit():
            jineng_number = int(jineng_number)
        else:
            print("请输入正确的数字！")
            continue
        if jineng_number == 1:
            print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_1_name"]))
            time.sleep(1)
            if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_1_acc"])):
                print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_1_demage"]))
                time.sleep(1)
                demage = attack_skill_dict["skill_1_demage"]
                i = 1
            else:
                time.sleep(1)
                print("但是没有命中......\r\n")
                time.sleep(1)
                demage = 0
                i = 1
        if jineng_number == 2:
            print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_2_name"]))
            if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_2_acc"])):
                time.sleep(1)
                print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_2_demage"]))
                time.sleep(1)
                demage = attack_skill_dict["skill_2_demage"]
                i = 1
            else:
                time.sleep(1)
                print("但是没有命中......\r\n")
                time.sleep(1)
                demage = 0
                i = 1
        if jineng_number == 3:
            print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_3_name"]))
            time.sleep(1)
            if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_3_acc"])):
                time.sleep(1)
                print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_3_demage"]))
                time.sleep(1)
                demage = attack_skill_dict["skill_3_demage"]
                i = 1
            else:
                time.sleep(1)
                print("但是没有命中......\r\n")
                time.sleep(1)
                demage = 0
                i = 1
        if jineng_number == 4:
            print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_4_name"]))
            time.sleep(1)
            if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_4_acc"])):
                time.sleep(1)
                print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_4_demage"]))
                time.sleep(1)
                demage = attack_skill_dict["skill_4_demage"]
                i = 1
            else:
                time.sleep(1)
                print("但是没有命中......\r\n")
                time.sleep(1)
                demage = 0
                i = 1
        if jineng_number == 5:
            print("\r\n")
            continue
    return demage

# 敌人战斗函数
def e_demage(attack, defend, attack_skill_dict):
    jineng_number = int(random.randint(1,4))
    if jineng_number == 1:
        print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_1_name"]))
        time.sleep(1)
        if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_1_acc"])):
            print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_1_demage"]))
            time.sleep(1)
            demage = attack_skill_dict["skill_1_demage"]
        else:
            time.sleep(1)
            print("但是没有命中......\r\n")
            time.sleep(1)
            demage = 0
    if jineng_number == 2:
        print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_2_name"]))
        time.sleep(1)
        if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_2_acc"])):
            print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_2_demage"]))
            time.sleep(1)
            demage = attack_skill_dict["skill_2_demage"]
        else:
            time.sleep(1)
            print("但是没有命中......\r\n")
            time.sleep(1)
            demage = 0
    if jineng_number == 3:
        print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_3_name"]))
        time.sleep(1)
        if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_3_acc"])):
            print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_3_demage"]))
            time.sleep(1)
            demage = attack_skill_dict["skill_3_demage"]
        else:
            time.sleep(1)
            print("但是没有命中......\r\n")
            time.sleep(1)
            demage = 0
    if jineng_number == 4:
        print("{0}使用了{1}！".format(attack, attack_skill_dict["skill_4_name"]))
        time.sleep(1)
        if random.uniform(0, 1) >= (1 - (attack_skill_dict["skill_4_acc"])):
            print("对{0}造成了{1}点伤害!\r\n".format(defend, attack_skill_dict["skill_4_demage"]))
            time.sleep(1)
            demage = attack_skill_dict["skill_4_demage"]
        else:
            time.sleep(1)
            print("但是没有命中......\r\n")
            time.sleep(1)
            demage = 0
    return demage


# 战斗过程函数
# 之后要做出“属性”概念，每个精灵的血量要有区别
def battle():  
    global med1, med2, hp, hpe, e_name, pokemon_name
    print("\r\n野生的{0}出现了！".format(e_name))
    time.sleep(1)
    print("去吧，{0}！！！\r\n".format(pokemon_name))
    while (hp > 0 and hpe >0):
        hpe -= demage(attack = pokemon_name, defend = e_name, attack_skill_dict = pokemon_skill_dict)
        if hpe > 0:
            hp -= e_demage(attack = e_name, defend = pokemon_name, attack_skill_dict = e_skill_dict)
            sy()
        if hpe <0:
            hpe = 0
    if hp <= 0 and hpe <= 0:
        time.sleep(1)
        print("dbq,平局算你输哦")
        time.sleep(1)
    if hpe <= 0 and hp > 0:
        time.sleep(1)
        print("野生的{}不行了！！".format(e_name))
        time.sleep(1)
        print("你获得了胜利！！！")
        time.sleep(1)
    if hp <= 0 and hpe > 0:
        time.sleep(1)
        print("彩笔，这都打不赢吗？？？")
        time.sleep(1)


# 主代码
shuoming()
time.sleep(1)
pokemon_name = select_pokemon()
e_name = select_e()
battle()








## 尝试建立
def beilv():
    # 先做水火草三系
    shuxing_dict = {"水" : 1,
    "火" : 2,
    "草" : 3
    }
    shuxing = shuxing_dict[00000000] #此处填入每个宝可梦属性的字典就好
    defend_huo = [2,1,0.5]
    defend_shui = [1,0.5,2]
    defend_cao = [0.5,2,1]