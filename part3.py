# Part 3 - Daniel
# independent variable
p_list = [0.01, 0.02, 0.03, 0.04, 0.05]
# results from our algorithm 
triangle_nums = []
# expected number of triangles
comparison_nums = []
n = 1024

for p in p_list:
    tri_avg = 0
    # find the avg of 10 trials for every value of p
    for _ in range(10):
        a = np.zeros(n,n)
        for i in range(n):
            for j in range(n):
                if i >= j:
                    a[i][j] = np.binomial(p)
                else:
                    a[i][j] = a[j][i]   
                    
        a2 = strassens(a,a)
        a3 = strassens(a2,a)
        trisum = 0
        for j in range(n):
            trisum += a[j][j]
        trisum = trisum / 6
        tri_avg += trisum
    tri_avg = tri_avg / 10
    triangle_nums.append(tri_avg)
    comparison = 1024*1023*1022/6
    comparison = comparison * (p**3)
    comparison_nums.append()
# TODO: plot