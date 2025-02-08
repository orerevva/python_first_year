def string(s):
  
  result = []
  c = 1

  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      c += 1
    else:
      result.append(s[i-1])
      if c > 1:
        result.append(str(c))
        c = 1
  result.append(s[-1])
  if c > 1:
    result.append(str(c))
    
  return "".join(result)
  
n = input()
print(string(n))

