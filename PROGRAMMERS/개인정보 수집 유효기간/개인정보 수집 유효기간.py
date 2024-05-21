def solution(today, terms, privacies):
    result = []
    # {'약관종류': 유효기간}
    dict1 = dict()
    for t in terms:
        a, b = t.split()
        dict1[a] = int(b)
    
    # 오늘 날짜
    t_year, t_month, t_day = map(int, today.split('.'))
    
    for idx, pri in enumerate(privacies):
        d, t = map(str, pri.split())
        p_year, p_month, p_day = map(int, d.split('.'))
        term = dict1[t]
    
        if p_month+term > 12:
            p_year += (p_month + term) // 12
            p_month = (p_month + term) % 12

        else:
            p_month += term
        
        p_day -= 1
        if p_day == 0:
            p_month -= 1
            p_day = 28
        if p_month == 0:
            p_year -= 1
            p_month = 12
        
        if p_year < t_year:
            result.append(idx+1)
        elif p_year == t_year and p_month < t_month:
            result.append(idx+1)
        elif p_year == t_year and p_month == t_month and p_day < t_day:
            result.append(idx+1)
        
    return result