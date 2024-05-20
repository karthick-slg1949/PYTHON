def printnumber(N, original, k, flag):
    print(N, end = "")
    if (N <=0):
        if(flag==0):
            flag = 1
        else:
            flag = 0
    if (N == original and (not(flag))):
        return
            
    if (flag == True):
        printnumber(N - k, original, k, flag)
        return
    if (not(flag)):
        printnumber(N + k, original, k, flag);
        return
N = 20
k = 6
printnumber(N, N, k, True)
            