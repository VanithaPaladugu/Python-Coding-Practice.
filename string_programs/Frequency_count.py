s=input()
for i in range(len(s)):
  count=0
  for j in range(len(s)):
    if s[i]==s[j]:
      count+=1
  if s.index(s[i])==i:
    print(s[i],count)
