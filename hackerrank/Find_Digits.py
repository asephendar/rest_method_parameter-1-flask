# soal = 1012

def findDigits(n):
    results = 0
    
    for el in str(n):
        if (int(el) != 0) and ((n % int(el)) == 0):
            results += 1
    
    return results

# print(findDigits(soal))
