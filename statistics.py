from math import sqrt

def calc_mean(values):
    """calculate the mean of an iterable object (values)"""
    if len(values) == 0 : return 0
    return sum(values) / len(values)


def calc_stdv(values):
    """calculate the std of an iterable object (values)"""
    if len(values) <= 1 : return 0
    mean = calc_mean(values)
    sum_val = sum([(x - mean)**2 for x in values])
    return sqrt(sum_val / (len(values) - 1))


def calc_covariance(values1, values2):
    """ calculates a covariance of two features
     :argument values1 -- feature 1 values
     :argument values2 -- feature 2 values
     :return the covariance of two features
     """
    if len(values1) <= 1 : return 0
    mean1,mean2 = calc_mean(values1), calc_mean(values2)
    sum_val = sum([(x - mean1)*(y - mean2) for x,y in zip(values1,values2)])
    return sum_val / (len(values1)-1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above,statistic_functions):
    """prints the population statistics according to the arguments values
    :argument feature_description -- The printed description of the statistic calculation
    :argument data -- The dictionary of the data
    :argument treatment -- The feature used to filter the data
    :argument target -- The feature which used to calculate it's statistics
    :argument threshold -- The limit value of the treatment
    :argument is_above -- A boolean variable which determines if threhold is minimum / maximum value
    :argument statistic_functions -- A list of statistics functions
    """
    values = [data[target][i] for i,value in enumerate(data[treatment]) if is_above is (value > threshold)]
    print(f"{feature_description}\n{target}: {str([round(func(values),2) for func in statistic_functions])[1:-1]}")





