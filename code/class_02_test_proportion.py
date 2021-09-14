#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:26:41 2021

@author: boris
"""

import numpy as np # log
from numpy import sqrt, log, exp, mean
import pandas as pd # data frames
import seaborn as sns # графики
from scipy import stats # законы распределения случайных величин

# data
S_obs = 7
n = 16
p_hat = S_obs / n

# hyp
# H_0: p = 1/2
# H_a: p < 1/2

# exact p-value
# P(S <= S_obs)
# S ~ binom(16, 1/2) under H_0
stats.binom.cdf(S_obs, n=n, p=1/2)

# normal approximation
mu_S = n * 1/2 # under H_0
mu_S
se_S = sqrt(n * p_hat * (1 - p_hat))
Z_obs = (S_obs - mu_S) / se_S
Z_obs
stats.norm.cdf(Z_obs)

# naive bootstrap
s_star = stats.binom.rvs(size=10000, n=16, p=1/2)
s_star
s_star <= S_obs
mean(s_star <= S_obs) # fraction of True in vector s_star

