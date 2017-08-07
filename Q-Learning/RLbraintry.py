'''# _*_ coding:UTF-8 _*_ '''
# coding:utf-8

import numpy as np
import pandas as pd


class QLearningTable:
	#初始化空的Q-table　纵轴
	def __init__(self, actions, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
		self.actions = actions  # a list
        self.lr = learning_rate # 学习率
        self.gamma = reward_decay   # 奖励衰减
        self.epsilon = e_gdreedy     # 贪婪度
        self.q_table = pd.DataFrame(columns=self.actions)   # 初始 q_table


	def choose_action(self, observation):
        self.check_state_exist(observation) # 检测本 state 是否在 q_table 中存在(见后面标题内容)

        # 选择 action
        if np.random.uniform() < self.epsilon:  # 选择 Q value 最高的 action
            state_action = self.q_table.ix[observation, :]
            print(state_action)

            # 同一个 state, 可能会有多个相同的 Q action value, 打乱action的位置
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.argmax()

        else:   # 随机选择 action
            action = np.random.choice(self.actions)

        return action


	def learn(self, s, a, r, s_):
        self.check_state_exist(s_)  # 检测 q_table 中是否存在 s_ (见后面标题内容)
        q_predict = self.q_table.ix[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.ix[s_, :].max()  # 下个 state 不是 终止符
        else:
            q_target = r  # 下个 state 是终止符
        self.q_table.ix[s, a] += self.lr * (q_target - q_predict)  # 更新对应的 state-action 值
        #（真实值-估计值）*学习效率

	#检验状态是否已经经历过
	def check_state_exist(self, state):
        if state not in self.q_table.index:
        # append new state to q table
	        self.q_table = self.q_table.append(
	            pd.Series(
	                [0]*len(self.actions),
	                index=self.q_table.columns,
	                name=state,
	            )
	        )



