FROM redis:2.8.17

#/data is the volume that came from redis add to it the config file
ADD redis.conf /redis.conf

CMD ["redis-server", "/redis.conf"]
