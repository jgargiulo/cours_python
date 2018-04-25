#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def pi_monte_carlo(n):
    nbr_inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        nbr_inside += (x*x + y*y) <= 1
    return 4*nbr_inside/n

print(pi_monte_carlo(10000))
