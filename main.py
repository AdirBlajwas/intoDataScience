import sys
import data
import random
import numpy as np
import statistics

SUMMER, FALL, WINTER, SPRING = 1,2,3,0
HOLIDAY, WEEKDAY = 1,0
HUM = 'hum'
CNT = 'cnt'
T1 = 't1'
SEASON = 'season'
IS_HOLIDAY = "is_holiday"
COV = "Cov"
SEASONS_VAL = [range(4)]


def question1(main_data, statistic_functions):
    print("Question 1:")
    loc_dict = {'Summer' : [SEASON,SUMMER], 'Holiday' : [IS_HOLIDAY, HOLIDAY], 'All': SEASONS_VAL}
    for key in loc_dict.keys():
        print(f"{key}:")
        if key != 'All' :
            data_filtered,other_data = data.filter_by_feature(main_data,loc_dict[key][0], [loc_dict[key][1]])
        else: data_filtered = main_data
        data.print_details(data_filtered, (HUM, T1, CNT), statistic_functions[0:2])
        data.print_joint_details(data_filtered, (T1, CNT), [statistic_functions[2]], [COV])

def question2(main_data, statistic_functions):
    print("\nQuestion 2:")
    local_dict  = {'thres_signs' : ["<=", ">"],'is_above_vals': [True, False], IS_HOLIDAY : ['holiday','weekday'],
                   'feature_descriptions' : [f"Winter {word} records:" for word in ['holiday', 'weekday']],
                   'data': list(data.filter_by_feature(main_data,IS_HOLIDAY,[HOLIDAY]))}
    thres_val = 13.0
    for i,thres_sign in enumerate(local_dict['thres_signs']) :
        print(f"if {T1}{thres_sign}{round(thres_val,1)} then:")
        for cur_data, description in zip(local_dict['data'],local_dict['feature_descriptions']):
            statistics.population_statistics(description, cur_data, T1, CNT, thres_val, i==0,
                                             statistic_functions[0:2])






def main(argv):
    main_data = data.load_data(argv[1],argv[0])
    random.seed(42)
    statistic_functions = [statistics.calc_mean, statistics.calc_stdv,statistics.calc_covariance]
    # main_data = {
    #     'season': [np.random.randint(0, 4) for i in range(10)],
    #     't1': [np.random.randint(0, 35) for i in range(10)],
    #     'cnt': [np.random.randint(0, 100) for i in range(10)],
    #     'is_holiday': [np.random.randint(0, 2) for i in range(10)],
    #     'hum': [100 * np.random.random() for i in range(10)],
    # }
    # print(main_data['is_holiday'])
    question1(main_data,statistic_functions)
    question2(main_data,statistic_functions)
    # statistics.population_statistics('hi it\'s what:', main_data,'t1','cnt',13.0, False, statistic_functions[0:2])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
