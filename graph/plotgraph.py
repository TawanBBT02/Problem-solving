import matplotlib.pyplot as plt

x = range(0,20,0)
y = []

def motion(u,a,t):
    S = u * t + (1/2) * a * t**2
    return S
