info=raw_input()
num=[int(x) for x in info.split(' ')]
n=int(input())
output = []
i = 0; j = len(num) - 1
while i < j:
            if num[i] + num[j] == n:
                output.append([num[i],num[j]])
                j=j-1
            elif num[i] + num[j] < n:
                i = i + 1
            elif num[i] + num[j] > n:
                j = j - 1
print ','.join(map(str, output))
