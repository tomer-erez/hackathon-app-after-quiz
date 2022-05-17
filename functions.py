from create_data import Create_Percentage_issue


def precent_of_wrong_answers (num_of_students, precent, question):
    precent = num_of_students*precent/100
    counter = 0
    for answer in question:
        if answer != 1:
            counter += 1
    if counter >= precent:
        print("There are more than ", str(precent), "of wrong answers in this question")
        return True
    else:
        print("There are less than ", str(precent), "of wrong answers in this question")
        return False

def counter_right_answers(dic_of_answers, correct_answer):
    count_right_ans = 0
    students_count = len(dic_of_answers.keys())
    for ans in dic_of_answers.items:
        if ans == correct_answer:
            count_right_ans+=1
    return count_right_ans/students_count

#return name dic and number of right ans per week!
def week_right_ans_counter(dic_of_answers, ans1, ans2, ans3):
    new_dic = {}
    count = 0
    for key in dic_of_answers.keys():
        if dic_of_answers[key][0] == ans1:
            count+=1;
        if dic_of_answers[key][1] == ans2:
            count += 1;
        if dic_of_answers[key][2] == ans3:
            count+=1;
        new_dic[key] = count;
        count = 0
    return new_dic

#return name and the num of right ans of all three weeks
def unite_right_ans(week1, week2, week3):
    unite_dic = {}
    for key in week1.keys():
        unite_dic[key] = week1[key]+week2[key]+week3[key]
    return unite_dic

#return list of students' names with least than 4 correct ans in total
def less_than_4_ans_in_total(dic):
    stupid_student = []
    for key in dic:
        if dic[key] <= 4:
            stupid_student.append(key)
    return stupid_student


# gets student and admin dics and return student dic whith list of 1 or 0, 1 for correct ans and 0 for wrong ans
def counter_right_answers(dic_of_student,dic_admin):
    new_dic_of_student = {}
    for student in dic_of_student.keys():
        new_dic_of_student[student] = []
        for i in range(3):
            if dic_admin['admin'][i] != dic_of_student[student][i]:
                new_dic_of_student[student].append(0)
            else:
                new_dic_of_student[student].append(1)
    return new_dic_of_student

#return name dic and number of right ans per week!
def week_right_ans_counter(dic_of_student):
    new_dic = {}
    for key in dic_of_student.keys():
        new_dic[key]=sum(dic_of_student[key])
    return new_dic

#gets binary dict of ans and return list with the success rates
def success_rate_per_question_this_week(binary_dict):
    rate = [0, 0, 0]
    for name in binary_dict.keys():
        i = 0
        for ans in binary_dict[name]:
            rate[i]+=ans
            i+=1
    for i in range(len(rate)):
        rate[i] = rate[i]/len(binary_dict)*100
    return rate

# create every question that has success rates less than 50%

def dict_of_tough_topics(success_rate_list,topics_list):
    tough_topics={}
    for i in range(len(topics_list)):
        if success_rate_list[i]<=50:
            tough_topics[topics_list[i]]=success_rate_list[i]
    if len(tough_topics)>0:
        for dic in tough_topics.keys():
            Create_Percentage_issue(tough_topics[dic], dic)