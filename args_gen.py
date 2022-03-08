# create bord_dic <value = bord_name , key = bord_id>
import json
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
#
# vars = {
#     "bord_ids": args.bord_ids,
#     "myItemName": args.item_name,
#     "columnVals": json.dumps({
#         "status": {"label": "Working on it"},
#         "date4": {"date": args.date},
#         "phone": {"phone": args.phone},
#         "location1": args.location,
#         # {"email" : { <email name> => "email" : "dipro.b@monday.com", <what will be desply in column><user name> "text" : "email"}} update email column
#         "email": {"email": args.Email, "text": "email"},
#         # text colum is in this formt  <item_id : <string> >
#         "text99": args.pub_name,
#         "long_text": args.discreption,
#         "long_text_1": args.notes,
#         "hour": {"hour": args.time.hour, "minute": args.time.minute}
#     })
# }
#
