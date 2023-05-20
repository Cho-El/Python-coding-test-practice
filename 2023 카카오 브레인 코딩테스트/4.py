import requests
url = 'https://jsonmock.hackerrank.com/api/tvseries?page='
genre = "Animation"
result = []
# page 수는 20까지
for i in range(1, 21):
    url = f'https://jsonmock.hackerrank.com/api/tvseries?page={i}'
    response = requests.get(url= url)
    responseDict = response.json()
    for data in responseDict['data']:
        if genre in data['genre']:
            result.append((data['name'], data['imdb_rating']))

result.sort(key = lambda x : [-x[1],x[0]])
print(result[0])