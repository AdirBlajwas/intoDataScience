from math import sqrt


def calc_mean(values):
    if len(values) == 0 : return 0
    return sum(values) / len(values)


def calc_stdv(values):
    if len(values) <= 1 : return 0
    mean = calc_mean(values)
    sum_val = sum([(x - mean)**2 for x in values])
    return sqrt(sum_val / (len(values) - 1))


def calc_covariance(values1, values2):
    if len(values1) <= 1 : return 0
    mean1,mean2 = calc_mean(values1), calc_mean(values2)
    sum_val = sum([(x - mean1)*(y - mean2) for x,y in zip(values1,values2)])
    return sum_val / (len(values1)-1)

def population_statistics(feature_description, data, treatment, target, threshold, is_above,statistic_functions):
    # print(feature_description)
    if(is_above): values = [data[target][i] for i,value in enumerate(data[treatment]) if value > threshold]
    else: values = [data[target][i] for i,value in enumerate(data[treatment]) if value <= threshold]
    print(f"{feature_description}\n{target}: {(str)([round(func(values),2) for func in statistic_functions])[1:-1]}")
