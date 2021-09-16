#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:47:33 2021

@author: boris
"""

import pandas as pd
import numpy as np
import seaborn as sns
from numpy import log, exp, mean, median, sqrt
from scipy import stats # законы распределения случайных величин
from arch.bootstrap import IIDBootstrap

np.random.seed(777)
data = pd.DataFrame({'y': stats.binom.rvs(size=30, n=1, p=0.3)})
data

p_hat = mean(data['y'])
p_hat

n_obs = data.shape[0]
n_obs

se_p_hat = sqrt(p_hat * (1 - p_hat) / n_obs)
se_p_hat

q_crit = stats.norm.ppf(0.975, loc=0, scale=1)
q_crit

p_hat_left = p_hat - q_crit * se_p_hat
p_hat_right = p_hat + q_crit * se_p_hat

p_hat_left
p_hat_right


true_ps = pd.DataFrame({'p': np.arange(start=0.1, stop=0.91, step=0.1), 'key': 0})
true_ps

exp_nos = pd.DataFrame({'exp_no': np.arange(start=1, stop=1001), 'key': 0})
exp_nos

experiments = true_ps.merge(exp_nos, how='outer')
experiments = experiments.drop(columns='key')
experiments

# create_random_data(n_obs, seed=777)
# get_asymptotic_proportion_ci(vector, level=0.95)
# cycle

res = experiments.groupby('p').agg(aver=('exp_no', 'mean'))
res



from arch.bootstrap import IIDBootstrap
bs = IIDBootstrap(returns)
ci = bs.conf_int(sharpe_ratio, 1000, method='studentized',
                 std_err_func=sharpe_ratio_se)


def sharpe_ratio(x):
    mu, sigma = 12 * x.mean(), np.sqrt(12 * x.var())
    return np.array([mu, sigma, mu / sigma])


def sharpe_ratio_se(params, x):
    mu, sigma, sr = params
    y = 12 * x
    e1 = y - mu
    e2 = y ** 2.0 - sigma ** 2.0
    errors = np.vstack((e1, e2)).T
    t = errors.shape[0]
    vcv = errors.T.dot(errors) / t
    D = np.array([[1, 0],
                  [0, 0.5 * 1 / sigma],
                  [1.0 / sigma, - mu / (2.0 * sigma**3)]
                  ])
    avar = D.dot(vcv /t).dot(D.T)
    return np.sqrt(np.diag(avar))








