'''
정렬 조건
-3, 길이가 짧은 것부터
-2, 길이가 같으면 사전 순으로
-1,  같은 단어가 여러 번 입력된 경우에는 한 번만 -> 중복 제거
'''

'''
<초기>      <최종>
brown       car
apple       apple
car         brown
apple
'''

'''
정렬 조건을 3, 2, 1 순으로 할 경우 다음과 같은 오답
brown apple car apple
car brown apple apple
apple apple brown car
apple brown car
'''

n = int(input())
wordList = []

for i in range(n):
    wordList.append(input())

wordList = sorted(list(set(wordList)))  # (중복 제거) brown apple car    >>>     (사전 순) apple brown car
wordList.sort(key=len)                  # (길이 순) car apple brown

for j in wordList:
    print(j)