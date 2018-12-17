#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python3.7.0
#@Author: Tix_Hjq
# @Time    : 18-12-17 下午8:11
import numpy as np


class equivalence(object):
    def __init__(self, A, R):
        '''
        param:
            A:集合
            R_X:关系的横坐标
            R_y:关系的纵坐标
        '''
        self.A = A
        self.R = R
        self.R_X = []
        self.R_y = []
        self.matrix = 0
        self.sum = 0
# protect

# Flag
    def Flag(self):
        '''
        p.s
            Flag:
          -1:no R and R
           1:R
           0:no R
        '''
        Flag = -1
        if(self.sum == 3):
            Flag = 1
            return Flag
        elif(self.sum == 0):
            Flag = 0
            return Flag
        return Flag

# point_change
    def point_change(self):
        flag = 0
        for point in self.R:
            for point_ in point:
                if(flag == 0):
                    self.R_X.append(point_)
                else:
                    self.R_y.append(point_)
                flag += 1
            flag = 0


# matrix
    def get_matrix(self):
        self.matrix = np.zeros((len(self.A), len(self.A)))
        for i, j in zip(self.R_X, self.R_y):
            self.matrix[i - 1, j - 1] = 1
# 自反

    def judge_reflexive_atrix(self):
        l = len(self.A) + 1
        self.sum = 0
        for X, y in zip(range(len(self.A)), range(len(self.A))):
            self.sum += self.matrix[X][y]
        flag = self.Flag()
        return flag
# 对称

    def Symmetry(self):
        point = range(1, len(self.A))
        point_ = range(len(self.A) - 1, 0, -1)
        self.sum = 0
        for X1, y1, X2, y2 in zip(point, point_, point_, point):
            if(self.matrix[X1][y1] == self.matrix[X2][y2]):
                self.sum += 1
        flag = self.Flag()
        return flag

# 传递

    def Transfer(self):
        Flag = 1
        for X1, y1 in zip(self.R_X, self.R_y):
            for X2, y2 in zip(self.R_X, self.R_y):
                if(X1 != X2 & y1 == X2):
                    if(self.matrix[X1 - 1][y2 - 1] == 0):
                        Flag = 0
                        return Flag
# public

    def fit_transform(self):
        self.point_change()
        self.get_matrix()
        flag_judge_reflexive_atrix = self.judge_reflexive_atrix()
        flag_Symmetry = self.Symmetry()
        flag_Transfer = self.Transfer()
        return flag_judge_reflexive_atrix, flag_Symmetry, flag_Transfer
