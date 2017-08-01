'''# _*_ coding:UTF-8 _*_ '''
# coding:utf-8
#使用一个小例子学习Q-Learning
#@author SkylineBin

#Q Table state-> action
#选择动作的功能
#直线的环境
#根据算法更新

import numpy as np
import pandas as pd
import time

np.random.seed(2) #reproducible 
#计算机产生一组伪随机数列

#创建几个全局变量
N_STATES = 6   # 1维世界的宽度 初始距离
ACTIONS = ['left', 'right'] #探索者的可用动作
EPSILON = 0.9   # 贪婪度 greedy
ALPHA = 0.1     # 学习率
GAMMA = 0.9    # 奖励递减值
MAX_EPISODES = 13   # 最大回合数
FRESH_TIME = 0.3    # 移动间隔时间

#EPSILON=0.9表示90%会选最优的动作
#10%会选不是最优的动作

#ALPHA是 学习效率
#GAMMA 奖励的衰减值
#MAX_EPISODES 只玩１３回合
#FRESH_TIME 每一步的时间间隔


#建立Q表格

def build_q_table(n_states,actions):
	table = pd.DataFrame(
		#q_table initial values
		np.zeros((n_states, len(actions))),
		columns = actions, #action's name
	)
	print(table)
	return table

# build_q_table(N_STATES,ACTIONS) #初始训练模型

def choose_action(state,q_table):
	#如何选择一个行为的函数
	state_actions = q_table.iloc[state,:]
	if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):
		action_name = np.random.choice(ACTIONS)#选择不贪婪的行为
	else:
		action_name = state_actions.argmax() #选择比较大的
	return action_name



