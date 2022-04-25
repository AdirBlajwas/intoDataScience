import pandas


def load_data(path, features):
    """Reads the data of London.csv and returns it as a dictionary"""
    df = pandas.read_csv(path)
    data = df.to_dict(orient= "list")
    return data


def filter_by_feature(data, feature, values):
    """Filter a dictonary type of data into 2 dictionaties according to the arguments
    :argument data -- The original dictionary
    :argument feature -- The feature used to filter the data by
    :argument values -- The values which the feature can get
    :return 2 data dictionaries (tuple) after filtering
    """
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key], data2[key] = [],[]
        for index,feature_value  in enumerate(data[feature]):
            if feature_value in values:
                data1[key]  = data1[key] + [data[key][index]]
            else:
                data2[key]  = data2[key] + [data[key][index]]
    return data1, data2


def print_details(data, features, statistic_functions):
    """Prints the statistics of the feature argument"""
    for feature in features:
        func_lst = [round(function(data[feature]),2) for function in statistic_functions]
        func_string = str(func_lst)[1:-1]
        print(f"{feature}: {func_string}")


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    """Prints A complex statistics of joint features"""
    for func_name, func in zip(statistic_functions_names,statistic_functions):
        cov_val = round(func(data[features[0]],data[features[1]]),2)
        print(f"{func_name}({', '.join(features)}): {cov_val}")




