import random

while True:
    left = random.randrange(2, 10)
    right = random.randrange(1, 10)
    # 정답
    answer = left * right
    print(left, ' x ', right, ' = ?')

    results = []
    results.append(answer)
    for i in range(1, 9):
        results.append(random.randrange(2, 10) * random.randrange(1, 10))
    random.shuffle(results)

    # 보기 출력
    for idx in range(0, 9):
        print(results[idx], end='\t')
        idx += 1
        if idx % 3 == 0:
            print()

    # 정답 입력
    while True:
        if answer == int(input('정답 입력 >> ')):
            print('맞음')
            break
        else:
            print('틀림')

    if 'n' == input('게임 리셋(y/n) >> '):
        print('게임 종료')
        break