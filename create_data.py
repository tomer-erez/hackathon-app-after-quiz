import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE5NjQ5NCwidWlkIjozMDQyNTUzNywiaWFkIjoiMjAyMi0wNS0xMlQxMToyNzo1My4zODBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIxMzM4NDUsInJnbiI6InVzZTEifQ.GBFH52N9sRG8XKPpf5zD6ifpBG8upY5CkrFcsvCuKTo"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}


## create item when a students has 3 weeks issues
def Create_3_weeks_notification(name):
    query3 = 'mutation ($text: String!, $group_id: String!){ create_item (board_id:2664241570, item_name:$text, group_id:$group_id ) { id } }'
    vars = {'text' : name +' will need your attention as he is struggeling with the course', 'group_id' : 'new_group' }

    data = {'query' : query3, 'variables' : vars}
    r = requests.post(url=apiUrl, json=data, headers=headers) # make request

## create item when only X percent or less of students passed in a specific question
def Create_Percentage_issue(percent, name_of_ques):
    query3 = 'mutation ($text: String!, $group_id: String!) { create_item (board_id:2664241570, item_name:$text , group_id:$group_id) { id } }'
    vars = {'text' : str(100 - percent) +' percent of students are having issues with ' +name_of_ques , 'group_id': 'new_group17729'}
    data = {'query' : query3, 'variables' : vars}
    r = requests.post(url=apiUrl, json=data, headers=headers) # make request
    #print(r.json())