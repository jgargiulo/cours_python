#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x): return 3*x +2
def g(x): return x**2
def h(x,y): return x + 2 * y
def i(x): return str(x)

def j(x): return f(g(x))
def h(x, y): return i(h(x,y))



