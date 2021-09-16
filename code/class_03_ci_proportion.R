library(boot)
library(tidyverse)

# выборка в 30 наблюдений
set.seed(777) # для реплицируемости
data = tibble(y = sample(c(0, 1), size = 30, replace = TRUE))
data

# классический интервал для доли p
p_hat = mean(data$y)
p_hat

n_obs = nrow(data)
se_p_hat = sqrt(p_hat * (1 - p_hat) /  n_obs)
se_p_hat

q_r = qnorm(0.975, mean = 0, sd = 1)
q_r

p_hat_left = p_hat - q_r * se_p_hat
p_hat_left


p_hat_right = p_hat + q_r * se_p_hat # p_hat - q_l * se_p_hat is also ok
p_hat_right

# naive or basic bootstrap
# упр. напишите наивный бустрэп без всякий пакетов

get_p_hat = function(orinal_sample, indices) {
  resample = orinal_sample[indices]
  p_hat = mean(resample)
  return(p_hat)
}

get_p_hat(data$y, c(1, 3, 7))

boot_setup = boot(data$y, get_p_hat, R = 10000)
boot_res = boot.ci(boot_setup, conf = 0.95)
boot_res

# t-stat boostrap aka studentized


get_p_hat_with_se = function(orinal_sample, indices) {
  resample = orinal_sample[indices]
  p_hat = mean(resample)
  n_obs = length(orinal_sample)
  se_p_hat = sqrt(p_hat * (1 - p_hat) / n_obs)
  return(c(p_hat, se_p_hat))
}

get_p_hat_with_se(data$y, c(1, 3, 7))
data$y[c(1, 3, 7)]

boot_setup = boot(data$y, get_p_hat_with_se, R = 10000)
boot_res = boot.ci(boot_setup, conf = 0.95)
boot_res


# step 1
indices = sample(1:30, size=30, replace=TRUE)
indices

# step 2
get_p_hat_with_se(data$y, indices)
# (p_hat_star, se_p_hat_star)
# t = (p_hat_star - p_hat) / se_p_hat_star

# Do step 1 and 2 10000 times

get_p_hat_with_se(data$y, 1:30) # p_hat
1:30
