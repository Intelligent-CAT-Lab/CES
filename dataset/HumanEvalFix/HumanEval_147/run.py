def get_max_triples(n):
    A = [i*i for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)

output = get_max_triples(5)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_147/output.txt", 'w')
file.write(str(output))
file.close()
    