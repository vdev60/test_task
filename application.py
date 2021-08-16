import requests

greeting = "Hello, World!"
access_key = "keyFsBiFJBAWFvy4o"
base_id = "app22SoQ4enC0rByb"
table_name = "MainTable"
headers={"Authorization": "Bearer {}".format(access_key)}
url = "https://api.airtable.com/v0/" + base_id + "/" + table_name
list_titles = []

def get_data():
    r  = requests.get(url, headers = headers)
    data = r.json()
    if r:
        pass
    else:
        return "An error has occurred."


    for record in data["records"]:
        list_titles.append(record["fields"]["title"])
    
    return list_titles


def circular_buffer(arr):
    new_arr= [];
    if len(arr) < 3:
        new_arr.append(arr)
        return new_arr 
    new_arr.append(arr)
    new_arr.append([arr[1]] + [arr[2]] + [arr[0]])
    new_arr.append([arr[2]] + [arr[0]] + [arr[1]])
    return new_arr

def return_current_element(list_titles):
    i = 0
    yield "Start of cycle"
    while(True):
        three_title = circular_buffer(list_titles[i:i+3])
        for j in three_title:
            yield j
        i = i+3
        if i > len(list_titles):
            yield "End of cycle"
            i = 0






