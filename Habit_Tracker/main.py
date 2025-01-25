import datetime as dt
import requests


USERNAME = ""
TOKEN = ""
#Creating an account
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)

#Creating a graph
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_config = {
    "id":"graph365",
    "name":"Coding Journey",
    "unit":"minutes",
    "type":"int",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# Input a value
today = dt.datetime.now()
print(today.strftime("%Y%m%d"))
graph_value_post_endpoint = "https://pixe.la/v1/users/kevinjames005/graphs/graph365"
graph_value_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many minutes did you learn:")
}
response = requests.post(url=graph_value_post_endpoint,json=graph_value_config,headers=headers)
print(response.text)

# Update a pixel
update_graph_pixel = f"https://pixe.la/v1/users/kevinjames005/graphs/graph365/{today.strftime("%Y%m%d")}"
parameters_quantity = {
    "quantity":"45"
}
# response = requests.put(url=update_graph_pixel,json=parameters_quantity,headers=headers)
# print(response.text)

# Delete a pixel
delete_a_pixel = f"https://pixe.la/v1/users/kevinjames005/graphs/graph365/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=update_graph_pixel,headers=headers)
# print(response.text)