import psutil

# print(psutil.cpu_percent(0.1))

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.virtual_memory())
print(psutil.swap_memory())
psutil.test()