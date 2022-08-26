from flask import Flask, request, send_from_directory, redirect, url_for, abort
import base64
import os
import asyncio
import datetime
import tbapi

parser = tbapi.TBAParser(api_key=os.environ.get('TBAKEY'), cache=False)
app = Flask(__name__)


async def sleepcheck():
    while True:
        files = os.listdir(avatars)
        for i in files:
            filedate = datetime.datetime.fromtimestamp(os.stat(i).st_ctime)
            today = datetime.datetime.today()
            if filedate.hour == today.hour and filedate.day != today.day:
                os.remove('avatars/{}'.format(i))
        asyncio.sleep(3600)


@app.route('/get_image')
def get_image():
    team = request.args.get('team')
    try:
        int(team)
    except:
        return "Please specify a valid team!"
    type = request.args.get('type')
    files = os.listdir('avatars')
    if '{}.png'.format(team) not in files:
        try:
            media = parser.get_team_media(team, 2023)
        except:
            return redirect('first.png')
        img_data = None
        for i in media:
            if i.type == 'avatar':
                img_data = i.details['base64Image']
                img_data = img_data.encode()
        if img_data is None:
            return redirect('first.png')
        with open("avatars/{}.png".format(team), "wb") as fh:
            print(len(img_data))
            fh.write(base64.decodebytes(img_data))
    if type == 'image':
        return send_from_directory('avatars', '{}.png'.format(team))
    elif type == 'url':
        return url_for('avatars/{}.png'.format(team))
    else:
        return redirect('/avatars/{}.png'.format(team), code=302)


@app.route('/first.png')
def first():
    return send_from_directory('', 'first.png')


@app.route('/avatars/<path:path>')
def avatars(path):
    return send_from_directory('avatars', path)


@app.route('/')
def home():
    return app.send_static_file('index.html')
