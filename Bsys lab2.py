import random
import time
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor
from locale import locale_alias

start = time.time()
def is_primeTone():
    start = time.time()
    isPrime = 0
    A = []
    fiv = 5

    for i in range(0, 100000000):
        A.append(random.randint(1, 10000000))

    for primer in range(0, 5000000):
        if A[primer] <= 1:
            isPrime = isPrime
        elif A[primer] <= 3:
            isPrime = isPrime + 1
        elif A[primer] % 2 == 0 or A[primer] % 3 == 0:
            isPrime = isPrime
        elif A[primer] == 5:
            isPrime = isPrime + 1
        else:
            while fiv * fiv <= A[primer]:
                if A[primer] % fiv == 0 or A[primer] % (fiv + 2) == 0:
                    isPrime = isPrime
                fiv = fiv + 6
            isPrime = isPrime + 1
    end = time.time()
    totaltime = end - start
    print("prime one time: " + str(totaltime))
    return A

def is_primeTtwo():
    start = time.time()
    isPrime = 0
    B = []
    fiv = 5

    for i in range(0, 100000000):
        B.append(random.randint(1, 10000000))

    for primer in range(5000000, 10000000):
        if B[primer] <= 1:
            isPrime = isPrime
        elif B[primer] <= 3:
            isPrime = isPrime + 1
        elif B[primer] % 2 == 0 or B[primer] % 3 == 0:
            isPrime = isPrime
        elif B[primer] == 5:
            isPrime = isPrime + 1
        else:
            while fiv * fiv <= B[primer]:
                if B[primer] % fiv == 0 or B[primer] % (fiv + 2) == 0:
                    isPrime = isPrime
                fiv = fiv + 6
            isPrime = isPrime + 1
    end = time.time()
    totaltime = end - start
    print("prime two time: " + str(totaltime))
    return B

with ThreadPoolExecutor(max_workers=2) as executor:
    Ao = executor.submit(is_primeTone())
    Bo = executor.submit(is_primeTtwo())
    for future in as_completed(Ao):
        A = future.Ao()
    for future in as_completed(Bo):
        B = future.Bo()

arrresult = A + B
print("First half: ")
print(A)
print("Second half")
print(B)
print("Both: ")
print(arrresult)
end = time.time()
totaltime = end - start
print("total sustime: " + str(totaltime))