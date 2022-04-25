import sys
import data
import statistics
import pandas as pd
import matplotlib.pyplot as plt
# pandas and matplotlib are used only(!) in the dry_part function


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
    """For all of the days, summer days and holidays separately, the function
    prints the mean and std of several features, and the covariance of t1 and cnt"""
    print("Question 1:")
    # a dictionary used to iterate the summer,holiday and all of the days for printing
    loc_dict = {'Summer' : [SEASON,SUMMER], 'Holiday' : [IS_HOLIDAY, HOLIDAY], 'All': SEASONS_VAL}
    for key in loc_dict.keys():
        print(f"{key}:")
        if key != 'All' :
            data_filtered,other_data = data.filter_by_feature(main_data,loc_dict[key][0], [loc_dict[key][1]])
        else: data_filtered = main_data
        data.print_details(data_filtered, (HUM, T1, CNT), statistic_functions[0:2])
        data.print_joint_details(data_filtered, (T1, CNT), [statistic_functions[2]], [COV])

def question2(main_data, statistic_functions):
    """For the winter days, the function calculates the mean and std of cnt for holidays and weekdays , separatly
    for days with temperature above 13.0 deg and below/equal"""
    # Filtering only th winter days
    winter_data, other_data = data.filter_by_feature(main_data,SEASON,[WINTER])
    print("\nQuestion 2:")
    #A dictionary used to iterate the different threshold limits, the holidays, for each calculation and print.
    local_dict  = {'thres_signs' : ["<=", ">"],'is_above_vals': [True, False], IS_HOLIDAY : ['holiday','weekday'],
                   'feature_descriptions' : [f"Winter {word} records:" for word in ['holiday', 'weekday']],
                   'data': list(data.filter_by_feature(winter_data,IS_HOLIDAY,[HOLIDAY]))}
    thres_val = 13.0
    for i,thres_sign in enumerate(local_dict['thres_signs']) :
        print(f"if {T1}{thres_sign}{round(thres_val,1)} then:")
        for cur_data, description in zip(local_dict['data'],local_dict['feature_descriptions']):
            statistics.population_statistics(description, cur_data, T1, CNT, thres_val, i==1,
                                             statistic_functions[0:2])



def dry_part(main_data):
    """The function creates a graph for the avg cnt according to days with the same temperature"""
    winter_data,other_data = data.filter_by_feature(main_data,SEASON,[WINTER])
    holiday_data, weekday_data = data.filter_by_feature(winter_data,IS_HOLIDAY,[HOLIDAY])
    df_index = [f'day_{i + 1}' for i in range(len(weekday_data[SEASON]))]
    df = pd.DataFrame(weekday_data, index=df_index)
    new_df = df.groupby('t1').mean().sort_values('t1')['cnt']
    cnt_lst = new_df.tolist()
    t1_lst = new_df.index.tolist()
    print(cnt_lst)
    print(t1_lst)
    plt.plot(t1_lst, cnt_lst)
    plt.xlabel('t1')
    plt.ylabel('cnt avg')
    plt.title('winter weekday cnt by t1')
    plt.show()


def main(argv):
    main_data = data.load_data(argv[1],argv[0])
    statistic_functions = [statistics.calc_mean, statistics.calc_stdv,statistics.calc_covariance]
    question1(main_data,statistic_functions)
    question2(main_data,statistic_functions)
    #dry_part(main_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
