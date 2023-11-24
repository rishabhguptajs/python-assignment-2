def compute_value(a):
    a_str = str(a)
    aa = int(a_str * 2)
    aaa = int(a_str * 3)
    aaaa = int(a_str * 4)
    result = a + aa + aaa + aaaa
    return result

a = int(input("Enter a digit: "))
result = compute_value(a)
print(f"The computed value is: {result}")
