from flask import Flask, render_template, redirect, request, jsonify, url_for
from flask_socketio import SocketIO, emit, join_room
import requests
import random
import html
import time

app = Flask(__name__)
SECRET_KEY = "51"
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app, cors_allowed_origins="*")
socketio.init_app(app)

rooms = {}

@app.route("/")
def home():
    #print('ON HOME PAGE')
    global next_que
    global question_list
    global correct_answers
    global final_answers
    global amount
    global score
    global database_list
    global played_solo
    global nickname
    global all_names
    global question_dict
    global score_dict
    played_solo = False
    next_que = 0
    amount = 0
    score = 0
    question_dict = {}
    score_dict = {}
    all_names = []
    question_list = []
    final_answers = []
    correct_answers = []
    database_list = []
    return render_template("index.html")

@app.route("/solo/game", methods=["POST"])
def user_input():
    global amount
    global nickname
    global played_solo
    played_solo = True
    categories_list = ['food_and_drink', 'art_and_literature', 'movies', 'music', 'society_and_culture', 'sport_and_leisure', 'geography']
    amount = request.form.get("amount")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    nickname = request.form.get("nickname")
    #print(nickname)


    # if the category is food and drink, art and literature, movies, music, science, society and culture or sport and leisure use second api
    if (category in categories_list):
        url = getNewUrl(amount,category)
        Json = getNewJson(url)
        correct_answers, final_answers, question_list = newToDict(Json)

    else:
        url = getUrl(amount, category,difficulty)
        Json = getJson(url)
        correct_answers, final_answers, question_list = toDict(Json)
    

    return quiz_page(correct_answers, final_answers, question_list)

#global question_list
@app.route('/next/question', methods=["POST"])
def next_question():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    global amount
    global score

    
    if played_solo:

        answer = request.form.get("answers")


    if(final_answers[next_que][int(answer)] == correct_answers[next_que]):
        print(final_answers[next_que][int(answer)])
        print(correct_answers[next_que])
        score += 1

    print('NEXT QUE: ', next_que)
    print('AMOUNT ', amount)
    if int(next_que + 1) == int(amount):
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount)
        return redirect(link)
        # print(score)

    next_que += 1
    print('SHOULD START AT 1', next_que)
    print('final answers: ')
    print(final_answers)
    question_name = question_list[next_que]

    return render_template(
        'solo_quiz.html',
        question=str(
        next_que + 1) + ") " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[next_que][0]),
        answer2=html.unescape(
        final_answers[next_que][1]),
        answer3=html.unescape(
        final_answers[next_que][2]),
        answer4=html.unescape(
        final_answers[next_que][3]))


@app.route('/next/question/2', methods=["POST"])
def next_question_2():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")
  

    if(final_answers[1][int(answer)] == correct_answers[1]):
        print(final_answers[1][int(answer)])
        print(correct_answers[1])
        score += 1
    
    if int(amount_2) == 1:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[1]

    return render_template(
        'quiz2.html',
        question="2) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[1][0]),
        answer2=html.unescape(
        final_answers[1][1]),
        answer3=html.unescape(
        final_answers[1][2]),
        answer4=html.unescape(
        final_answers[1][3]))

        
@app.route('/next/question/3', methods=["POST"])
def next_question_3():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[2][int(answer)] == correct_answers[2]):
        print(final_answers[2][int(answer)])
        print(correct_answers[2])
        score += 1
    
    if int(amount_2) == 2:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[2]

    return render_template(
        'quiz3.html',
        question="3) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[2][0]),
        answer2=html.unescape(
        final_answers[2][1]),
        answer3=html.unescape(
        final_answers[2][2]),
        answer4=html.unescape(
        final_answers[2][3]))


@app.route('/next/question/4', methods=["POST"])
def next_question_4():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[3][int(answer)] == correct_answers[3]):
        print(final_answers[3][int(answer)])
        print(correct_answers[3])
        score += 1
    
    if int(amount_2) == 3:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[3]

    return render_template(
        'quiz4.html',
        question="4) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[3][0]),
        answer2=html.unescape(
        final_answers[3][1]),
        answer3=html.unescape(
        final_answers[3][2]),
        answer4=html.unescape(
        final_answers[3][3]))

@app.route('/next/question/5', methods=["POST"])
def next_question_5():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[4][int(answer)] == correct_answers[4]):
        print(final_answers[4][int(answer)])
        print(correct_answers[4])
        score += 1

    if int(amount_2) == 4:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[4]

    return render_template(
        'quiz5.html',
        question="5) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[4][0]),
        answer2=html.unescape(
        final_answers[4][1]),
        answer3=html.unescape(
        final_answers[4][2]),
        answer4=html.unescape(
        final_answers[4][3]))

@app.route('/next/question/6', methods=["POST"])
def next_question_6():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[5][int(answer)] == correct_answers[5]):
        print(final_answers[5][int(answer)])
        print(correct_answers[5])
        score += 1
    
    if int(amount_2) == 5:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[5]

    return render_template(
        'quiz6.html',
        question="6) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[5][0]),
        answer2=html.unescape(
        final_answers[5][1]),
        answer3=html.unescape(
        final_answers[5][2]),
        answer4=html.unescape(
        final_answers[5][3]))

@app.route('/next/question/7', methods=["POST"])
def next_question_7():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[6][int(answer)] == correct_answers[6]):
        print(final_answers[6][int(answer)])
        print(correct_answers[6])
        score += 1
    
    if int(amount_2) == 6:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[6]

    return render_template(
        'quiz7.html',
        question="7) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[6][0]),
        answer2=html.unescape(
        final_answers[6][1]),
        answer3=html.unescape(
        final_answers[6][2]),
        answer4=html.unescape(
        final_answers[6][3]))

@app.route('/next/question/8', methods=["POST"])
def next_question_8():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[7][int(answer)] == correct_answers[7]):
        print(final_answers[7][int(answer)])
        print(correct_answers[7])
        score += 1
    
    if int(amount_2) == 7:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[7]

    return render_template(
        'quiz8.html',
        question="8) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[7][0]),
        answer2=html.unescape(
        final_answers[7][1]),
        answer3=html.unescape(
        final_answers[7][2]),
        answer4=html.unescape(
        final_answers[7][3]))

@app.route('/next/question/9', methods=["POST"])
def next_question_9():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[8][int(answer)] == correct_answers[8]):
        print(final_answers[8][int(answer)])
        print(correct_answers[8])
        score += 1
    
    if int(amount_2) == 8:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[8]

    return render_template(
        'quiz9.html',
        question="9) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[8][0]),
        answer2=html.unescape(
        final_answers[8][1]),
        answer3=html.unescape(
        final_answers[8][2]),
        answer4=html.unescape(
        final_answers[8][3]))

@app.route('/next/question/10', methods=["POST"])
def next_question_10():
    global next_que
    global question_list
    global correct_answers
    global final_answers
    #global amount
    global score
    global new_name
    global question_dict

    answer = request.form.get("answers")

    if(final_answers[9][int(answer)] == correct_answers[9]):
        print(final_answers[9][int(answer)])
        print(correct_answers[9])
        score += 1
    
    if int(amount) == 9:
        print('NEXT QUE: in if ', next_que)
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount_2)
        return redirect(link)
        # print(score)
        
    print(final_answers)
    question_name = question_list[9]

    return render_template(
        'quiz10.html',
        question="10) " + html.unescape(question_name),
        answer1=html.unescape(
        final_answers[9][0]),
        answer2=html.unescape(
        final_answers[9][1]),
        answer3=html.unescape(
        final_answers[9][2]),
        answer4=html.unescape(
        final_answers[9][3]))

@app.route("/display_score/<score><amount>")
def display_score(score, amount):
    global nickname
    #time = stop stopwatch
    #addToDB(nickname,score,time)
    try:
        return render_template(
            "score.html",
            Nickname=nickname,
            score=score,
            amount=amount)
    except BaseException:
        return render_template(
            "score.html",
            Nickname="User",
            score=score,
            amount=amount)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/leaderboard")
def leaderboard():

    return render_template('leaderboard.html')

# @app.route("/quiz_2<room>", methods=["POST"])
# def quiz_2(room):
#     global join_nickname
#     join_nickname = request.form.get("nickname")
#     return jsonify({'redirect': url_for("example_2", nickname=nickname)})

# @app.route('/example_2/<nickname>')
# def example_2(nickname):
#     return render_template("quiz.html")
# @app.route("/quiz_2")
# def quiz_2():
#     return render_template("quiz.html")

@app.route("/quiz<room>", methods=["POST"])
def quiz(room):
    global amount_2
    global nickname_2

    categories_list = ['food_and_drink', 'art_and_literature', 'movies', 'music', 'society_and_culture', 'sport_and_leisure', 'geography']
    amount_2 = request.form.get("amount")
    category_2 = request.form.get("category")
    difficulty_2 = request.form.get("difficulty")
    nickname_2 = request.form.get("nickname")
    #print(nickname_2)


    # if the category is food and drink, art and literature, movies, music, science, society and culture or sport and leisure use second api
    if (category_2 in categories_list):
        url = getNewUrl(amount_2,category_2)
        Json = getNewJson(url)
        correct_answers, final_answers, question_list = newToDict(Json)

    else:
        url = getUrl(amount_2, category_2,difficulty_2)
        Json = getJson(url)
        correct_answers, final_answers, question_list = toDict(Json)
    

    return quiz_page(correct_answers, final_answers, question_list)



def getNewUrl(amount,category):
    print('MADE IT TO GET NEW URL')
    base_url = 'https://trivia.willfry.co.uk/api/questions?'
    final_url = base_url + 'limit=' + str(amount)
    if category != 'default_c':
        final_url = base_url + 'categories=' + category + '&limit=' + str(amount)
    return final_url


def getNewJson(url):
    response = requests.get(url)
    data = response.json()
    return data


def newToDict(json):
    correct = []
    answers = []
    temp_list = []
    for value in json:
        question_list.append(value['question'])
        correct_answers.append(value['correctAnswer'])
        correct = value['correctAnswer']
        # Grabs only 3 incorrect answers to make sure corect answer will always be on screen
        answers = value['incorrectAnswers'][:3]
        answers.append(correct)
        random.shuffle(answers)
        final_answers.append(answers)
    return correct_answers, final_answers, question_list


def getUrl(amount, category, difficulty):
    Base_url = 'https://opentdb.com/api.php?amount=' + str(amount)
    final_url = Base_url
   
    if category != 'default_c':
        final_url = final_url + '&category=' + str(category)
    
    final_url = final_url + '&type=multiple'

    return final_url


def getJson(final_url):
    response = requests.get(final_url)
    data = response.json()
    return data


def toDict(json_data):
    correct = []
    answers = []
    for value in json_data['results']:
        # print(value)
        # questions.append(value['question'])
        question_list.append(value['question'])
        correct_answers.append(value['correct_answer'])
        correct = value['correct_answer']
        answers = value['incorrect_answers']
        answers.append(correct)
        random.shuffle(answers)
        final_answers.append(answers)
    #print('q list ', question_list)

    return correct_answers, final_answers, question_list


def quiz_page(correct_answers, final_answers, question_list):
    #print("camehere")
    #start stopwatch
    #print(played_solo)
    global question_name
    global start_time
    start_time = time.time()
    question_name = question_list[0]

    if played_solo == True:
        print("solo")
        return render_template(
        'solo_quiz.html',
        question='1) ' +
        html.unescape(question_name),
        answer1=html.unescape(
            final_answers[0][0]),
        answer2=html.unescape(
            final_answers[0][1]),
        answer3=html.unescape(
            final_answers[0][2]),
        answer4=html.unescape(
            final_answers[0][3]))
    else:
        print("notsolo")
        return jsonify({'redirect': url_for("example", question_name=question_name)})

@app.route('/example/<question_name>')
def example(question_name):
    question_name = question_name
    return render_template(
        'quiz.html',
        question='1) ' +
        html.unescape(question_name),
        answer1=html.unescape(
            final_answers[0][0]),
        answer2=html.unescape(
            final_answers[0][1]),
        answer3=html.unescape(
            final_answers[0][2]),
        answer4=html.unescape(
            final_answers[0][3]))

@app.route("/quiz_2")
def quiz_2():
    return quiz_page(correct_answers, final_answers, question_list)
#     # return render_template(
#     #     'quiz.html',
#     #     question='1) ' +
#     #     html.unescape(question_name),
#     #     answer1=html.unescape(
#     #         final_answers[0][0]),
#     #     answer2=html.unescape(
#     #         final_answers[0][1]),
#     #     answer3=html.unescape(
#     #         final_answers[0][2]),
#     #     answer4=html.unescape(
#     #         final_answers[0][3]))

def is_admin(id, room):
    return rooms[room] == id

@socketio.on('connection')
def on_connect(socket):
    print('user connected')

@socketio.on('disconnect')
def on_admin_disconnect():
    print('user disconnected')
    print(rooms)
    for room in rooms:
        if is_admin(request.sid, room):
            print(room)
            del rooms[room]
    emit('leave')

# only emitted by players

@socketio.on('join')
def on_join(data):
    #global all_names
    global question_dict
    global new_name
    new_name = data['name']
    #all_names.append(new_name)
    question_dict[new_name] = 0
    print('question_dict: ', question_dict)
    room = data['room']
    join_room(room)
    emit('join', data, room=room)
    print(f'{new_name} joined {room}')

@socketio.on('buzz')
def on_buzz(data):
    name = data['name']
    room = data['room']
    emit('buzz', { 'name': name } , room=room)

@socketio.on('exists')
def exists(data):
    room = data['room']
    emit('exists', room in rooms)

# only emitted by admin

@socketio.on('create')
def on_create(data):
    room = data['room']
    if (room in rooms or len(room) < 3):
        emit('create', False)
    else:
        join_room(room)
        rooms[room] = request.sid
        emit('create', True)
        #print(f'created room: {room}')

@socketio.on('reset')
def on_reset(data):
    room = data['room']
    #res = data['res']
    if is_admin(request.sid, room):
        emit('reset', room=room)

@socketio.on('begin')
def on_begin(data):
    room = data['room']
    if is_admin(request.sid, room):
        emit('begin', room=room)

@socketio.on('score')
def on_score(data):
    leaderboard = data['leaderboard']
    room = data['room']
    if is_admin(request.sid, room):
        emit('score', { 'leaderboard' : leaderboard }, room=room)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')