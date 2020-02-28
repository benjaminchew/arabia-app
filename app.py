from flask import Flask, request, jsonify, render_template
from external.amadeus import get_pois, get_profile_pic
from external.wikipedia import get_summary, get_wikipedia_page_data
from external.microsoft import msft_tts
# from external.couchbase import get_or_create_user, save_user_data

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    category = request.args['c']
    return render_template('index.html', category=category)


@app.route('/find_pois')
def find_pois():
    

    # parse params
    lat = float(request.args['lat'])
    lon = float(request.args['lon'])
    radius = float(request.args['r'])
    category = request.args['c']
    
    # get pois
    pois = get_pois(lat=lat, lon=lon, radius=radius, category=category)

    # get image for each POI
    for poi in pois:
        poi['wiki_data'] = get_wikipedia_page_data(poi['name'])

    # return as JSON
    return jsonify({
        'pois': pois
    })

@app.route('/get_audio')
def get_audio_file():
    text = str(request.args['text'])

    audio_file_url = msft_tts(text)

    return jsonify({
        'audio_url': audio_file_url
    })


# @app.route('/sign_up')
# def sign_up():
#
#     # parse params
#     username = request.args['username']
#     password = request.args['password']
#
#     # lookup username (and verify password)
#     user_data, created = get_or_create_user(username=username, password=password)
#
#     # if username, then return user deets
#     if not created:
#         return user_data
#
#     # else, create a new profile pic
#     profile_pic = get_profile_pic()
#     user_data = save_user_data(username=username, data={
#         'profile_pic': profile_pic
#     })
#
#     return jsonify(user_data)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)