def frange(val, base=0.0, step=0.1):
    results = []
    if val < base:
        start = val
        stop = base
    else:
        start = base
        stop = val
    # 동일한 로컬 범위 내에서는 블록 개념 무의미
    while start < stop:
        results.append(start)
        start+=step
    for f in results:
        print('%.1f'%f,end='\t\t')
    return results

frange(1.0,2.0)