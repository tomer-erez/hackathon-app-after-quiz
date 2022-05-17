from functions import *
from create_data import *
from read_data import *

print('\n\n\n')

week_1_id = 2664040130
week_2_id = 2664041413
week_3_id = 2665389890

# retrieve all data from boards
dict_week1, dict_answers_1 = retrieve_dicts(week_1_id)
dict_week2, dict_answers_2 = retrieve_dicts(week_2_id)
dict_week3, dict_answers_3 = retrieve_dicts(week_3_id)

# creating week 1 stats
dict_binary_ans_week1 = counter_right_answers(dict_week1, dict_answers_1)
dict_sum_right_ans_week1 = week_right_ans_counter(dict_binary_ans_week1)

# creating week 2 stats
dict_binary_ans_week2 = counter_right_answers(dict_week2, dict_answers_2)
dict_sum_right_ans_week2 =week_right_ans_counter(dict_binary_ans_week2)

# creating week 3 stats
dict_binary_ans_week3 = counter_right_answers(dict_week3, dict_answers_3)
dict_sum_right_ans_week3 = week_right_ans_counter(dict_binary_ans_week3)

# get a list of strugling students
united = unite_right_ans(dict_sum_right_ans_week1, dict_sum_right_ans_week2, dict_sum_right_ans_week3)
list_strugle = less_than_4_ans_in_total(united)

# create items for each struggeling student
for i in list_strugle:
    Create_3_weeks_notification(i)

questions_list_1 = retrieve_questions(week_1_id)
questions_list_2 = retrieve_questions(week_2_id)
questions_list_3 = retrieve_questions(week_3_id)
success_rate_week_1 = success_rate_per_question_this_week(dict_binary_ans_week1)
success_rate_week_2 = success_rate_per_question_this_week(dict_binary_ans_week2)
success_rate_week_3 = success_rate_per_question_this_week(dict_binary_ans_week3)



dict_of_tough_topics( success_rate_week_1,questions_list_1)
dict_of_tough_topics( success_rate_week_2,questions_list_2)
dict_of_tough_topics( success_rate_week_3,questions_list_3)