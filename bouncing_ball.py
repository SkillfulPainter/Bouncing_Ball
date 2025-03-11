import scipy.constants as C
import math

def BounceOnce(h, total_distance, time):    # 计算从某高度h下落并弹起至最高点的过程中的弹起高度，路程与时间
    t_down = math.sqrt(2 * h / C.g)    # 计算下落时间
    t_up = math.sqrt(h / C.g)          # 计算弹起时间
    total_distance += 3 * h / 2        # 计算路程
    h = h / 2                          # 计算弹起高度
    time += t_down + t_up              # 计算总时间

    return h, total_distance, time

def BounceTotal(h, n):
    total_distance = 0
    time = 0                # 初始化总路程和总时间变量
    for i in range(n):      # 分n次计算每一个下落+弹起过程的弹起高度、路程与时间，累加得到总路程和总时间
        h, total_distance, time = BounceOnce(h, total_distance, time)      # 将上一个过程的弹起高度，当前总路程和总耗时输入函数，得到下一个过程的弹起高度，总路程和时间，如此循环n次

    return h, total_distance, time


h = 100    # 初始下落高度 (m)
n = 10     # 计算第n次掉落并弹起至最高点时的反弹高度，总路程和总时间
h_n, total_distance, time = BounceTotal(h, n)     # 输出结果
print("第" + str(n) + "次掉下并反弹到最高点时，小球反弹了" + str(h_n) + "米高。此时球一共经过"
      + str(total_distance) + "米，运动了" + str(time) + "秒。")     # 打印结果