import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE5ODY2MCwidWlkIjozMDQyNTg2MSwiaWFkIjoiMjAyMi0wNS0xMlQxMTo0MTozOC45MjdaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIxMzM4NDUsInJnbiI6InVzZTEifQ.CP0p_wI4Lp4On-BBC6pwTeLsmpsiJbzdXnUbY3FsKjM"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}


def retrieve_dicts(board_id):
    query2 = '{boards (ids: ' + str(board_id) + ') {  items { name column_values{ text  } } } }'
    data = {'query': query2}

    r = requests.post(url=apiUrl, json=data, headers=headers).json()  # make request
    num_of_students = len(r['data']['boards'][0]['items'])

    dict = {}
    admin_dict = {}
    for i in range(0, num_of_students):
        name = (r['data']['boards'][0]['items'][i]['name'])
        if name.lower() == "admin":
            admin_dict["admin"] = []
            for j in range(0, 3):
                ans = r['data']['boards'][0]['items'][i]['column_values'][j]['text']
                admin_dict[name].append(ans)

        else:
            dict[name] = []
            for j in range(0, 3):
                ans = r['data']['boards'][0]['items'][i]['column_values'][j]['text']
                dict[name].append(ans)
    return dict, admin_dict


# get question names
def retrieve_questions(board_id):
    query2 = '{boards (ids: ' + str(board_id) + ') {  items { name column_values{title text  } } } }'
    data = {'query': query2}

    r = requests.post(url=apiUrl, json=data, headers=headers).json()  # make request

    question_list = []
    for i in range(0, 3):
        name = (r['data']['boards'][0]['items'][0]['column_values'][i]['title'])
        question_list.append(name)
    return question_list