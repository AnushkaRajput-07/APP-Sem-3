a = input("Enter first string: ")
b = input("Enter second string: ")
m = len(a)
n = len(b)

dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
max_length = 0
end_index = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_index = i
        else:
            dp[i][j] = 0

substring = a[end_index - max_length:end_index]
           
print("Length of Longest Common Substring:", max_length)
print("Longest Common Substring:", substring)
