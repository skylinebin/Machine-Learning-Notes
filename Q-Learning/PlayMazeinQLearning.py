'''# _*_ coding:UTF-8 _*_ '''
# coding:utf-8

#study from 

#使用一个二维走迷宫学习Q-Learning
#有单独的环境文件和RL_brain思考决策
#利用思考去执行决策　
#@author SkylineBin

from maze_env import Maze
from RL_brain import QLearningTable

import numpy as np
import pandas as pd


def update():
	for episode in range(30):
		observation = env.reset()
		#环境给出的观测值

		while True:
			#刷新环境
			env.render()

			#基于观测值选择行为
			action = RL.choose_action(str(observation))

			#跳到下一个状态，得到下一个状态的观测值以及所返回的reward
			observation_, reward, done = env.step(action)
			#done标志位用来判断是否完成整个行为

			#进行模式学习
			RL.learn(str(observation), action, reward, str(observation_))

			#完成这个状态，下一个观测值作为当前观测值，进入下一个状态
			observation = observation_

			if done:
				break

		print(action,observation)

	# end this game
	print('game over\n')
	env.destroy()

if __name__ == '__main__':
	env = Maze()
	RL = QLearningTable(actions = list(range(env.n_actions)))


	#展示运行可视化环境
	env.after(100, update)
	env.mainloop()


