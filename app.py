import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('ping', 'ping')
print(r.get('ping')) # pong




