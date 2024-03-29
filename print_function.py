import json
from itertools import islice

# this page is for special print function
list_names_tools = ["item name","status","inventory","inventory know","comments"]
list_names_events = ["location","date","time","descripton","nots","status","publisher name","publisher Phone","publisher Email"]

def print_board(bord_id,commend,client):
    if commend == "tools":
        list_ = list_names_tools.copy()
        size = 8

    if commend == "events":
        list_ = list_names_events.copy()
        size = 11

    res = list()
    data_bord = get_data_from_bord_to_list(bord_id,client)
    res.append([data_bord[i:i+8] for i in range(0,len(data_bord),size)])
    res = res[0]
    for item in res:
        for name,data in zip(list_,item):
             print(str(name) + ":" + str(data[0]))
        print()


# function will fetch data from monday using monday api (see description bellow )
# she convert data from jason to => python object and print it to the screen
def get_data_from_bord_to_list(bord_id,client):
    res = client.boards.fetch_items_by_board_id(bord_id)
    # convert from json => dic
    item_list = list()
    res_list = list()
    #convert the bord json data to list of list each index contine the fileds of one item
    # item[0] = > list of dic => the id and value of each field
    for item in res["data"]["boards"]:
        for data_item in item["items"]:
            item_list.append(data_item["column_values"])
    # get the value of the fileds
    for item_object in item_list:
        for item_data in item_object:
            tup = (str(item_data["text"]),str(item_data["id"]))
            res_list.append(tup)
    print(res_list)
    return res_list,len(item_list)

#(Utility)# print json with indent
def print_json(json_):
    print(json.dumps(json_, indent=2, sort_keys=True))
