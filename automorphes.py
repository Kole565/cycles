import math
import time


limit = int(input("Enter limit: "))


start = time.time()
out = []
n_5 = 5
n_6 = 6
num_to_add_5 = num_to_add_6 = 1
while n_5 < limit:
    if str(n_5**2).endswith(str(n_5)):
        out.append(n_5)
        num_to_add_5 *= 10
    
    if str(n_6**2).endswith(str(n_6)):
        out.append(n_6)
        num_to_add_6 *= 10

    n_5 += num_to_add_5
    n_6 += num_to_add_6


with open("out.txt", "w") as output:
    i = 1
    for result in sorted(out):
        formatted = "{:3} {} ** 2 => {}".format(i, result, result**2)
        print(formatted, file=output)
        i += 1
    
    print("\nCompleted in {:1.2} sec.".format(time.time() - start), file=output)
        