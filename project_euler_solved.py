
def get_prime_factor_ary(num):
    """returns a list of num's prime factors"""
    temp_num = num
    prime_factor_array = []
    while temp_num > 1:
        temp_ary = findprimefactor(temp_num)
        temp_num = temp_ary[0]
        if temp_ary[1] != 1:
            prime_factor_array.append(temp_ary[1])
    return prime_factor_array

def get_prime_factor_dict(num):
    """returns a dictionary of num's prime factors"""
    temp_num = num
    prime_factor_dict() = dict()
    while temp_num > 1:
        temp_ary = findprimefactor(temp_num)
        temp_num = temp_ary[0]
        if temp_ary[1] != 1:
            prime_factor_dict[temp_ary[1]] = prime_factor_dict[temp_ary[1]] + 1
    return prime_factor_dict

def findprimefactor(num):
    """
    returns (<num divided by it's smallest prime factor>, <smallest prime factor>)
    if no smallest prime factor, returns (1,1)
    """
    num = int(num)
    for i in range(2,num+1):
        if num%i == 0:
            return [num/i,i]
    return[1,1]

def isprime(num):
    """returns true if num is prime"""
    num = int(num)
    sqrt = int((num**0.5)//1)
    for i in range(2,sqrt+1):
        if num%i == 0: return False
    return True

def euler1():
    answer = 0
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
            answer = answer + i
    print(answer)

def euler2():
    f1 = 2
    f2 = 3
    sum = 0
    while (f1 < 4000000):
        #every third term should be here
        sum = f1 + sum
        f4 = 2*f2+f1
        f5 = f4+f1+f2
        f1 = f4
        f2 = f5
    print(sum)

def euler3(num):
    #600851475143
    num = int(num)
    while (num > 1):
        ary = findprimefactor(num)
        num = ary[0]
        biggest = ary[1]
        print(num)
        print(biggest)


def euler4():
    biggest = 0
    for i in range(100,999):
        for j in range(100,999):
            if ispalindrome(i*j):
                if biggest < i*j:
                    biggest = i*j
    print(biggest)
def ispalindrome(num):
    nstring = str(num)
    for i in range(0,len(nstring)-1):
        inv = len(nstring)-1 - i
        if nstring[inv] != nstring[i]: return False
    return True


def euler5(num):
    num = int(num)
    product = num
    product_ary = []
    for i in range(1,num):
        prime_ary = get_prime_factor_ary(i)
        for j in range(1,num):
            while prime_ary.count(j) > product_ary.count(j):
                product_ary.append(j)
    print(product_ary)
    final_product = 1
    for i in product_ary:
        final_product = i*final_product
    print(final_product)





def euler6(num):
    total_sum = 0
    square_sum = 0
    for i in range (1,num+1):
        square_sum = square_sum + i*i
        total_sum = i + total_sum
    print(total_sum*total_sum-square_sum)
    print(square_sum)
    print(total_sum)


def euler7(num):
    j = 1
    total_primes = 0
    while total_primes < num:
        j = j+1
        if isprime(j):
            total_primes = total_primes + 1
    print(j)

def euler9():
    for c in range(335,997):
        for b in range(2,c):
            a = 1000 - b - c
            if a*a + b*b == c*c: return (a,b,c)

def euler10(num):
    total_primes = 0
    for i in range(2,num):
        if isprime(i):
            total_primes = total_primes + i
    print(total_primes)


def path(a,b,pascal_ary):
    """returns a number in pascals triangle looked up by index (a,b). define a dictionary before using this function to improve efficiency"""

    if b > a:
        c = a
        a = b
        b = c
    if (a,b) in pascal_ary: return pascal_ary[(a,b)]
    if a == 0: return 1
    if b == 0: return 1

    new_num = (path(a-1,b,pascal_ary) + path(a,b-1,pascal_ary))
    pascal_ary[(a,b)] = new_num
    return new_num

def euler15():
    pascal_ary = dict()
    print(path(20,20,pascal_ary))

def euler16(num):
	result = 2**num
	result_str = str(result)
	total = 0
	for i in result_str:
		total += int(i)
	return total



def euler20(num):
    product = 1
    for i in range(1,num):
        product = product*i
        #while product%10 == 0:      apparently this will cause rounding errors when converting from ints to doubles...need to use integer math here.
            #product = product//10
    print(str(product))
    product_str = str(product)
    sum = 0
    print(product_str)
    #print(sum([int(i) for i in product_str]))
    for i in product_str:
        sum += int(i)
    return sum

def euler40(num):
	stringy = "."
	i = 0
	while len(stringy) < num + 1:
		i += 1
		stringy = stringy + str(i)
	print(stringy)
	i = 0
	mult_result = 1
	for  i in range(0,len(str(num))):
		mult_result = mult_result * int(stringy[10**i])
	return mult_result

def euler46():
	obt_result = False
	num = 7
	while obt_result == False:
		num += 2
		if isprime(num): continue
		obt_result = isgoldbachnum(num)
	return num
def isgoldbachnum(num):
		i = 1
		minus = 2*(i**2)
		while  minus < num:
			obt_result = True
			if isprime(num - minus):
				obt_result = False
				break
			i += 1
			minus = 2*(i**2)
		return obt_result

def euler67(): #also the solution to problem 18? basically computes path values as we go.
    triangle = grabt()
    var_list = format_triangle(triangle)
    ary_d = var_list[0]
    size = var_list[1]

    path = dict()
    for i in range(0,size):
        for j in range(0,i+1):
            path = determine_path_v(i,j,ary_d[(i,j)],path)
    greatest = 0
    for i in range(0,size):
        if path[(size-1,i)] > greatest: greatest = path[(size-1,i)]
    return greatest

def format_triangle(triangle):
    iterator = iter(triangle.splitlines())
    dino = dict()
    i_count = 0
    for i in iterator:
        j_count = 0
        for j in i.split():
            dino[(i_count,j_count)] = int(j)
            j_count +=1
        i_count += 1
    return [dino,i_count]

def determine_path_v(i,j,j_num,path):
    if i > 0:
        if j > 0:
            if j == i:
                path[(i,j)] = path[(i-1,j-1)] + j_num
            else:
                path[(i,j)] = max(path[(i-1,j)],path[(i-1,j-1)]) + j_num
        else: path[(i,j)] = path[(i-1,0)] + j_num
    else: path[(0,0)] = j_num
    return path
def grabt():
    triangle = """
"""
    return triangle
