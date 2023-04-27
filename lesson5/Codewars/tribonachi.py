# Трібоначі
def tribonacci(signature, n):
    if n == 0: return []
    
    else:
        if n == 1: return [signature[0]]
        if n == 2: return [signature[0], signature[1]]
        if n == 3: return [signature[0], signature[1], signature[2]]
        a1 = signature[0]
        a2 = signature[1]
        a3 = signature[2]
        result = signature
        for i in range(4, n + 1):
            s = a1 + a2 + a3
            result.append(s)
            if i < n:
                a1 = a2
                a2 = a3
                a3 = s
        return result
'''
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
'''

'''
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]
'''

'''
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
'''