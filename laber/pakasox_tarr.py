def pakasox_tarr(my_list):
    n = my_list[-1]
    n_sum = (n*(n+1))/2
    res = n_sum - sum(my_list)
    return int(res)