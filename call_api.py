api1='http://127.0.0.1:8080/ip'
api2='http://127.0.0.1:8080/emp'
import requests
api1_res=requests.get(api1)
api1_res=api1_res.json()
print('api1_res=',api1_res)
api2_res=requests.post(api2,params={'user':'abc','passwd':'xyz'})
api2_res=api2_res.json()
print('api2_res=',api2_res)
api3='http://127.0.0.1:8080/json'
api3_res=requests.get(api3)
api3_res=api3_res.json()
print('api3_res=',api3_res)