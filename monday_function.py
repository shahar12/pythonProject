from monday import MondayClient
import json
import requests
from print_function import print_board,get_data_from_bord_to_list


# global monday user api data, include  = > api_key (use for accesses to your account on monday)
# dict_bords = > continue a dictionary => create bord_dic <value = bord_name , key = bord_id>
apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0NzQ2NzA5NywidWlkIjoyNzYwMTUwOCwiaWFkIjoiMjAyMi0wMi0yM1QwOTo0MjoyMS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTEwNzYyOTYsInJnbiI6InVzZTEifQ.uDWh-PSBMqlqQgeGdgVMdelBn08Oip1_yYhq6JIwpGQ"
client = MondayClient(apiKey)
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}
# create bord_dic <value = bord_name , key = bord_id>
zip_iter = zip(["tools", "request", "events","test"],["2326678952", "2326731714", "2348440107","2348954454"])
dict_bords = dict(zip_iter)

vars_tool_request = {
    "bord_ids": int(dict_bords["request"]),
    "myItemName": "רוני דוד" ,
    "columnVals": json.dumps({
        "status": {"label": "Working on it"},
        "timeline0": {"from": "2022-03-07","to": "2022-03-14"},
        "phone": {"phone": "0545311349"},
        # {"email" : { <email name> => "email" : "dipro.b@monday.com", <what will be desply in column><user name> "text" : "email"}} update email column
        "email": {"email": "shshar.amshili@gmail.com", "text": "email"},
        "text3": "סיר פויקה",
        # text colum is in this formt  <item_id : <string> >
    })
}

vars_tool_request_test = {
    "bord_ids": int(dict_bords["request"]),
    "myItemName": "בדיקה בדיקה" ,
    "columnVals": json.dumps({
        "timeline0": {"from": "2022-03-07","to": "2022-03-14"},
        "phone": {"phone": "0545311349"},
        # {"email" : { <email name> => "email" : "dipro.b@monday.com", <what will be desply in column><user name> "text" : "email"}} update email column
        "email": {"email": "shshar.amshili@gmail.com", "text": "email"},
        "text3": "סיר פויקה",
        # text colum is in this formt  <item_id : <string> >
    })
}



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

#crate the query struct to send to monday api
def int_args(args):
    vars = {
        "bord_ids": args.bord_ids,
        "myItemName": args.item_name,
        "columnVals": json.dumps({
            "status": {"label": "Working on it"},
            "date4": {"date": args.date},
            "phone": {"phone": args.phone},
            "location1": args.location,
            # {"email" : { <email name> => "email" : "dipro.b@monday.com", <what will be desply in column><user name> "text" : "email"}} update email column
            "email": {"email": args.Email, "text": "email"},
            # text colum is in this formt  <item_id : <string> >
            "text99": args.pub_name,
            "long_text": args.discreption,
            "long_text_1": args.notes,
            "hour": {"hour": args.time.hour, "minute": args.time.minute}
        })
    }
    return args


def add_new_event_to_bord(args):
    query_chngae_colmun_value = "mutation ($bord_ids : Int! ,$myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_ids, item_name:$myItemName, column_values:$columnVals) { id } }"
    data = {"query": query_chngae_colmun_value, "variables": args}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    print(r.json())


#(Utility)# print json with indent
def print_json(json_):
    print(json.dumps(json_, indent=2, sort_keys=True))





def main():
    # =============================================================================
    # create all the bords info in dict
    # =============================================================================
    
    # # =============================================================================
    # fatch all the bords and items from monday.com
    # =============================================================================
    res = client.boards.fetch_items_by_board_id(dict_bords["request"])
    # print_json(res)
    add_new_event_to_bord(vars_tool_request)
    # # =============================================================================
    # create a new item in equipment bord on monday.com
    # =============================================================================
    #chngae_colmun_value()
    print_board(dict_bords["tools"],"tools",client)
if __name__ == "__main__":
    main()
