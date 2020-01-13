import json
from flask import Flask
from flask import request, make_response

app = Flask(__name__)

fruits = ("banana", "apple", "orange", "strawberry")
vegetables = ("beetroot", "lettuce", "cucumber", "carrot", "celery")

with open('people.json', 'r') as pdata:
    people = json.loads(pdata.read())

with open('companies.json', 'r') as cdata:
    companies = json.loads(cdata.read())


# return all their employees
@app.route("/emp", methods=["GET"])
def getemployees():
    company = request.args.get('company')
    comp = [i for i in companies if i["company"] == company]

    if len(comp) == 0:
        return make_response({'error': "No company name - %s exists." % company})
    else:
        employees = [i for i in people if i['company_id'] == comp[0]['index']]
        if len(employees) == 0:
            return make_response({'error': "No employees for company %s" % company})
        else:
            return make_response(json.dumps(employees))


# friends data and common friends
@app.route("/people", methods=["GET"])
def getfriends():
    """Method for people info and common friend"""
    friend1 = request.args.get('frnd1')
    friend2 = request.args.get('frnd2')
    if friend1 and friend2:
        frnd1_info = [i for i in people if str(i['index']) == friend1]
        frnd2_info = [i for i in people if str(i['index']) == friend2]
        common_friends = [i for i in frnd1_info[0]['friends'] if i in frnd2_info[0]['friends']]

        friends_info = []
        for friend in common_friends:
            friend_info = [people[i] for i in range(len(people)) if people[i]['index'] == friend['index']]
            friends_info.append(friend_info)

        # brown eyes and alive
        filtered_friend = [friends_info[i][0] for i in range(len(friends_info)) if friends_info[i][0]['eyeColor'] == 'brown'
                           and friends_info[i][0]['has_died'] is False]

        data = {
            "friend1": frnd1_info,
            "friend2": frnd2_info,
            "common_friend": filtered_friend
        }
        return make_response(json.dumps(data))


# return food info for person
@app.route("/food/<emp>", methods=["GET"])
def getfood(emp):
    employee = [i for i in people if str(i['index']) == emp]
    if len(employee) == 0:
        return make_response({'error': "No results for company %s" % emp})
    else:
        food_lst = employee[0]['favouriteFood']
        fruits_lst =[]
        vegetables_lst = []
        for food in food_lst:
            if food in fruits:
                fruits_lst.append(food)
            elif food in vegetables:
                vegetables_lst.append(food)

        data = {
            "username": employee['name'],
            "age": employee['age'],
            "fruits": fruits_lst,
            "vegetables": vegetables_lst
        }
        return make_response(json.dumps(data))


if __name__ == "__main__":
    app.run(debug=True)
