# customer의 1명의 정보를 저장
customer1 = {'id' : 1, 'name' : '홍길동', 'email' : 'gildong@aa.com', 'phone' : '01012345678'}
customer2 = dict()
customer2['id'] = 2
customer2['name'] = '둘리'
customer2['email'] = 'dooly@aa.com'
customer2['phone'] = '01056781234'
print(customer1['name'])
print(customer2.get('name1'))
result = customer2.get('name1')
if result:
    print(result)
else:
    print('dict key not found')

customer3 = {'id' : 3, 'name' : '마이콜', 'email' : 'micahale@aa.com', 'phone' : '01012342222'}

customer_list = [customer1, customer2, customer3]

customer_list2 = []
customer_list2.append(customer1)
customer_list2.append(customer2)
print(customer_list2)

for cust in customer_list:
    # print(type(cust), cust)
    for key in cust.keys():
        print(f'{key} = {cust[key]}')

for cust in customer_list:
    for k, v in cust.items():
        print(f'{k} = {v}')