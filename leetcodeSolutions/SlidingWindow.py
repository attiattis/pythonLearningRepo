li = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

startingIndex = 0
endingIndex = 0
result = []
windowSum = 0.0
for endingIndex in range(len(li)):
    windowSum += li[endingIndex]

    if endingIndex > K:
        result.append(windowSum / K)
        windowSum = windowSum - li[startingIndex]
        startingIndex += 1

print(result)
