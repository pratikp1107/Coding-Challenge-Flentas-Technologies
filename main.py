n = int(input("Enter number of test cases :"))
for i in range(n):
  str1 = input(f"Enter {i} test case pattern : ")
  str2 = input(f"Enter {i} test case string : ")
  if str1 in str2 or str1[::-1] in str2:
    print("YES")
  else:
    print("NO")
