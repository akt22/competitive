from math import sin, cos, radians

a, b, d = list(map(int, input().split()))

a_prime = a * cos(radians(d)) - b * sin(radians(d))
b_prime = a * sin(radians(d)) + b * cos(radians(d))

print(a_prime, b_prime)
