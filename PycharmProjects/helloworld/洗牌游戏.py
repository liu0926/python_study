import random

poker_num = [str(i) for i in range(2,11)] #数字牌
poker_str = ['A','J','Q','K']  #字母牌
poker_king = ['大王','小王'] #大小王
poker_color = ['红','黑','方','花'] #花色

pokers = ['%s%s'%(i,j) for i in poker_color for j in poker_num+poker_str] + poker_king #生成54张牌
print(len(pokers))

random.shuffle(pokers) #随机洗牌
#print(pokers)

poker_a = pokers[0:51:3] #斗地主玩法
poker_b = pokers[1:51:3]
poker_c = pokers[2:51:3]
last_3 = pokers[-3:]
print('A:',poker_a)
print('B:',poker_b)
print('C:',poker_c)
print('最后三张:',last_3)
