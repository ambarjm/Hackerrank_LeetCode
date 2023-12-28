def dynamicArray(n, queries):
     lastAnswer=0
     seq=[[] for _ in range (n)]
     result=[]
     for q,x,y in queries:
         if q==1:
             idx =(x ^ lastAnswer) % n
             seq[idx].append(y)
         else:
             idx= (x^lastAnswer) % n
             v = y% len (seq[idx])
             lastAnswer= seq[idx][v]
             result.append(lastAnswer)
     return result
