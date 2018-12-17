#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python3.7.0
#@Author: Tix_Hjq
# @Time    : 18-12-17 下午8:12
import Equivalence

A = [1, 2, 3]
R1 = [[1, 1], [1, 2], [1, 3], [2, 1], [3, 1]]
R2 = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3]]

eq = Equivalence.equivalence(A, R1)
eq2 = Equivalence.equivalence(A, R2)
score_R1 = eq.fit_transform()
score_R2 = eq.fit_transform()
for R1, R2 in zip(score_R1, score_R2):
    if(R1 != R2):
        print("no equivalence")
print("equivalence")
