from flask import Flask
import requests
import json

app = Flask(__name__)

#pull data from reddit
def get_aww():
    #r = requests.get('http://reddit.com/r/aww/new.json', timeout = 1)
    #return(r.json())
    with open('datasets/reddit_aww.json') as aww_file:
        aww = json.load(aww_file)
    return aww

def get_cars():
    r = requests.get('http://reddit.com/r/autos.json', timeout = 1)
    j = r.json()
    return(j)
    #with open('datasets/reddit_aww.json') as aww_file:
    #    aww = json.load(aww_file)
    #return aww


#route for cars
@app.route('/cars/')
def hello_world():
    a = get_cars()
    linksList = []
    htmlStart = """<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
"""

    htmlEnd = """
</body>

</html>"""
    jpgList = ""
    gifvList = ""

    for link in a['data']['children']:
        eachUrl = link['data']['url']
        if not ".gifv" in eachUrl:
            embedJPG = "<img src=" + '"' + eachUrl + '"' + ' alt="HTML5 Icon" ' +' style="width: 50%; height: 50%"/>'
            jpgList+=embedJPG
        else:
            embedGIF = '<iframe class="imgur-embed" width="25%" height="25%" frameborder="0" src=" '+ eachUrl+ '"></iframe>'
            gifvList +=embedGIF
        
    #return str(linksList)
    return(htmlStart + gifvList + jpgList + htmlEnd)

#get the posts from reddit
@app.route('/aww/')
def get_posts():
    a = get_aww()
    linksList = []
    htmlStart = """<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
"""

    htmlEnd = """
</body>

</html>"""
    jpgList = ""
    gifvList = ""

    for link in a['data']['children']:
        eachUrl = link['data']['url']
        if not ".gifv" in eachUrl:
            #linksList.append(eachUrl)
            embedJPG = "<br><br><img src=" + '"' + eachUrl + '"' + ' alt="gg" ' +' style="width: 50%; height: 50%"/>'
            jpgList+=embedJPG
        else:
            #eachUrl.replace('.gifv','.webm')
            embedGIF = '<br><br><iframe class="imgur-embed" width="25%" height="25%" frameborder="0" src=" '+ eachUrl+ '"></iframe>'
            #embedGIF = '<video width="320" height="240" controls> <source src="' + eachUrl + '" type="video/mp4"> </video>'
            gifvList +=embedGIF
        
    #return str(linksList)
    return(htmlStart + gifvList + jpgList + htmlEnd)

#main
if __name__ == '__main__':
    app.run()
    #print(get_posts())
