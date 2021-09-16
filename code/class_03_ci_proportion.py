#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:17:09 2021

@author: boris
"""

import pandas as pd
import seaborn as sns
from numpy import log, exp, mean, median, sqrt
import numpy as np
from scipy import stats
from arch.bootstrap import IIDBootstrap

np.random.seed(777) # для воспроизводимости

# один набор данных!

data = pd.DataFrame({'y': stats.binom.rvs(size=30, n=1, p=0.3)})
data

# всё ок?
# classic asymptotic ci for proportion

n_obs = data.shape[0]
n_obs
p_hat = mean(data['y'])
p_hat

se_p_hat = sqrt(p_hat * (1 - p_hat) / n_obs)
se_p_hat

q_r = stats.norm.ppf(0.975, loc=0, scale=1)
q_r

p_hat_left = p_hat - q_r * se_p_hat
p_hat_left

p_hat_right = p_hat + q_r * se_p_hat # - q_l
p_hat_right

# [0.08; 0.38]



# naive bootstrap 

# упр. реализовать лапками без пакета arch

def get_p_hat(sample):
    p_hat = mean(sample)
    return p_hat

boot = IIDBootstrap(data['y'])
ci = boot.conf_int(get_p_hat, reps=10000, method='basic', size=0.95)
ci

# bootstrap t-stat


def get_p_hat(sample):
    p_hat = mean(sample)
    return p_hat

def get_p_hat_se(estimate, sample):
    p_hat = mean(sample)
    n_obs = len(sample)
    p_hat_se = sqrt(p_hat * (1 - p_hat) / n_obs)
    return p_hat_se

boot = IIDBootstrap(data['y'])
ci = boot.conf_int(get_p_hat, reps=10000, method='studentized', size=0.95,
                   std_err_func=get_p_hat_se)
ci








