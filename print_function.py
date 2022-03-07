
# this page is for special print function
list_names_tools = ["item name","status","inventory","inventory know","comments"]
list_names_events = ["location","date","time","descripton","nots","status","publisher name","publisher Phone","publisher Email"]

def print_board(bord_id,commend,client):
    if commend == "tools":
        list_ = list_names_tools.copy()
    if commend == "events":
        list_ = list_names_events.copy()

    data_bord = get_data_from_bord_to_list(bord_id,client)
    res = ""
    for data in data_bord:
        for sub_data in data:
            print(type(sub_data),list(sub_data.split(":")))
    # for data in data_bord:
    #     for name in list_:
    #          print( str(name) + ":" + str(data))
    #     print()


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
            id = item_data["id"]
            text = item_data["text"]
            res_list.append({id,text})
    print(res_list)
    return res_list
