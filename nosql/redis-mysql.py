import time
import MySQLdb as mdb
import redis

print 'Initialising...'
N = 10000
users = [(int(i), i) for i in range(0, N)]

r = redis.StrictRedis(host='localhost')

# Assumes that a test database exists
con = mdb.connect('localhost', 'root', '', 'test')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS `users` (`id` varchar(255) NOT NULL, `val` int(11) NOT NULL, PRIMARY KEY (`id`))')
cur.execute('TRUNCATE TABLE `users`')
con.commit()


print 'Redis: %5d inserts' % N,
t0 = time.time()
for id, val in users:
    r.zadd('users', id, val)
print '%6.3fs' % (time.time() - t0)


print 'Mysql: %5d inserts' % N,
t0 = time.time()
for id, val in users:
    cur.execute("INSERT IGNORE INTO users(id, val) VALUES('%s', '%s')" % (id, val))
    con.commit()
print '%6.3fs' % (time.time() - t0)


print 'Redis: %5d selects' % N,
t0 = time.time()
for id, val in users:
    r.zcount('users', val, N)
print '%6.3fs' % (time.time() - t0)


print 'MySQL: %5d selects' % N,
t0 = time.time()
for id, val in users:
    cur.execute("SELECT COUNT(*) FROM users WHERE `val`>%d" % val)
    con.commit()
print '%6.3fs' % (time.time() - t0)


print 'Redis: %5d deletes' % N,
t0 = time.time()
for id, val in users:
    r.zrem('users', id)
print '%6.3fs' % (time.time() - t0)


print 'MySQL: %5d deletes' % N,
t0 = time.time()
for id, val in users:
    cur.execute("DELETE FROM users WHERE `id`='%s'" % id)
    con.commit()
print '%6.3fs' % (time.time() - t0)

