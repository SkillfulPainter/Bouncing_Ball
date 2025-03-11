# Bouncing_Ball
A Python program to calculate how high a ball bounces, how long does it bounce and how much distance it travels after n bounces.

# HW2：计算小球第n次弹起高度以及此时的总路程和总时间
赵殿燊 2025.3.11
将小球的n次弹跳过程分成n个类似的子过程。每个子过程为小球从某一高度h自由落体并弹起h/2的过程。根据自由落体运动中下落/弹起高度h与重力加速度g、下落/弹起时间t的关系式：
	h=1/2 gt^2	(1)
可以推导出t与h和g的关系式：
	t=√(2h/g)	  (2)
将下落高度h与弹起高度h/2代入式（2）可以求得下落与弹起的时间。将两者相加可得该子过程的总时间。该子过程的总路程为h+h/2=3h/2，小球弹起的高度为h/2。上述计算过程的代码实现见bouncing_ball.py中的BounceOnce函数。
为了求解整个n次弹跳过程后小球经过的总路程，总时间以及最终的弹跳高度，将上述过程循环n次，并用上一次循环输出的弹起高度进行下一个循环弹起高度、路程以及时间的计算，并将计算得到的各个子过程的路程和时间相加得到整个过程的总路程和总时间。上述过程的代码实现见bouncing_ball.py中的BounceTotal函数。
为计算小球在100米高处自由落体，经过10次弹跳后的弹起高度，经过的总路程和总时间，将bouncing_ball.py中参数h（释放高度/m）的值设为100，n（弹跳次数/m）的值设为10，运行程序即可。程序的输出为：“第 10 次掉下并反弹到最高点时，小球反弹了 0.09765625 米高。此时球一共经过 299.70703125 米，运动了 25.49868278930235 秒。”同理，通过改变h和n的值，可以计算小球从不同高度下落并弹跳n次后的弹跳高度，总路程和总时间。
