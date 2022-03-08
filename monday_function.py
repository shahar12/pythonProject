from monday import MondayClient
import requests
from print_function import print_board,print_json
from args_gen import *

# global monday user api data, include  = > api_key (use for accesses to your account on monday)
# dict_bords = > continue a dictionary => create bord_dic <value = bord_name , key = bord_id>
apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0NzQ2NzA5NywidWlkIjoyNzYwMTUwOCwiaWFkIjoiMjAyMi0wMi0yM1QwOTo0MjoyMS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTEwNzYyOTYsInJnbiI6InVzZTEifQ.uDWh-PSBMqlqQgeGdgVMdelBn08Oip1_yYhq6JIwpGQ"
client = MondayClient(apiKey)
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}

# create new item for bord id = > test check if its ok to replace bord id with static var
def create_new_item(item_name):
    create_item_query = "mutation ($bord_ids : Int! , $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_ids, item_name:$myItemName, column_values:$columnVals) { id } }"
    vars = {"myItemName": item_name}
    data = {"query": create_item_query, "variables": vars}
    r = requests.post(url=apiUrl, json=data, headers=headers) # make request
    if r.status_code != 200:  # throw exception
        print('Status:', r.status_code)
        raise Exception("Add to board failed.")
    else:
        print(json.loads(r))

# {"id": "phone", "text": "", "type": "phone", "value": None}
# function create a new item and update field with the right value
# get = > <item name,string> , <args,class of the uniq bord type filed > , <bord_id , int >
def add_to_bord(item_name,args,bord_id):
    query_chngae_colmun_value = "mutation ($bord_id : Int!,$myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_id, item_name:$myItemName, column_values:$columnVals) { id } }"
    data = {"query": query_chngae_colmun_value, "variables": vars}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    if r.status_code != 200:  # if error throw exception
        print('Status:', r.status_code)
        raise Exception("Add to board failed.")
    else :
        print(json.loads(r))



def add_new_event_to_bord(args):
    query_chngae_colmun_value = "mutation ($bord_ids : Int! ,$myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_ids, item_name:$myItemName, column_values:$columnVals) { id } }"
    data = {"query": query_chngae_colmun_value, "variables": args}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    print(r.json())



def main():
    # # =============================================================================
    # create a new item in equipment bord and event bord on monday.com
    # =============================================================================
    add_new_event_to_bord(vars_tool_request)
    add_new_event_to_bord(vars_tool_request_test)
    # # =============================================================================
    # print the bords tools and events from monday.com
    # =============================================================================
    print_board(dict_bords["tools"],"tools",client)
    print_board(dict_bords["events"],"events",client)

if __name__ == "__main__":
    main()
