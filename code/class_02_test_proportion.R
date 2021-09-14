# class 2. 2021-09-09

# data
n = 16
S_obs = 7
p_hat = S_obs / n

# hypothesis
# H_0: p = 1/2
# H_a: p < 1/2

# exact p-value
# r|p|q|d + norm|binom|geom|pois|...
pbinom(S_obs, size = n, prob = 1/2) # P(S <= S_obs)
dbinom(7, size = 20, prob = 1/3) # P(Binom(20, 1/3) = 7)
pbinom(7, size = 20, prob = 1/3) # P(Binom(20, 1/3) <= 7)

# normal approximation
mu_S = 8 # under H_0
se_S = sqrt(n * p_hat * (1 - p_hat)) # estimate of sqrt(Var(S))
Z_obs = (S_obs - mu_S) / se_S
Z_obs
pnorm(Z_obs) # P(N(0,1) <= Z_obs)

# bootstrap

S_star = rbinom(10000, size = 16, p = 1/2)
S_star
S_star <= S_obs
mean(S_star <= S_obs)
