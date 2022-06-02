# 0 <= H <= 23, 0 <= M <= 59
# Approach: Cal whole T, then convert to H & M
# Converted clock time in Minutes = 60 * M + M - 45
# Actual time => H = cctm / 60, M = cctm % 60
# edge case when total time < 0
H, M = map(int, input().split())
totalT = (H * 60) + M - 45
if totalT < 0:
    actualH = 23
else:
    actualH = int(totalT / 60)
actualM = totalT % 60
print(actualH, actualM)
