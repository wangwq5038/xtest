import json

host = "http://192.168.9.87:8880/api/v1.0"
with open ('read_json.json','r',encoding='utf8') as fp:
    json_data = json.load(fp)
    test_data = json_data['paths']
    # print(test_data)
    # print(type(test_data))
    print(test_data["/admin/login"]["post"]["produces"])
    # for k,v in test_data.items():
        # print(k)
        # print(type(v))
        # url = host + "{}".format(k)
        # print(url)
                
        