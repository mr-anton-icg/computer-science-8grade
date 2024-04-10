def min_n_variables(elements):
    min_v = elements[0]
    for x in elements:
        if x < min_v:
            min_v = x
    return min_v

# # elements = [6**6, 7**5, 5**7]
# elements = [5,1,9,0,7]
# assert min_n_variables(elements) == 0
# print('min value of elements=', min_n_variables(elements))

def second_min_n_variables(elements):
    min_v = elements[0]
    for x in elements:
        if x < min_v:
            min_v = x

    second_min_v = elements[0]
    for x in elements:
        if x < second_min_v:
            if x > min_v:
                second_min_v = x
                
    return second_min_v

# elements = [6**6, 7**5, 5**7]
elements = [5,1,9,0,7]
assert second_min_n_variables(elements) == 1
print('second min value of elements=', second_min_n_variables(elements))

