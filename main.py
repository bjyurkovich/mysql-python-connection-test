import MySQLdb

# Create two connections
db=MySQLdb.connect(user='root', passwd="coleslaw",db="TestConnections")
db1=MySQLdb.connect(user='root', passwd="coleslaw",db="TestConnections")
db2=MySQLdb.connect(user='root', passwd="coleslaw",db="TestConnections")

#Reset DB

c=db.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS TestConnections;")
c.execute("USE TestConnections;")
c.execute("DROP TABLE IF EXISTS Test;")  
c.execute("CREATE TABLE `Test` (`id` BIGINT NOT NULL AUTO_INCREMENT, `data` VARCHAR(255) NOT NULL, PRIMARY KEY (`id`));") 


#  Get cursors for both
c1=db1.cursor()
c2=db2.cursor()

# Start transactions on both
c1.execute("START TRANSACTION;")
c1.execute("INSERT INTO Test SET `data`='Hello on connection 1';")

c2.execute("START TRANSACTION;")
c2.execute("INSERT INTO Test SET `data`='Hello on connection 2';")

# Rollback on 1, commit on 2.  Hope that only 2 survives in the DB
c1.execute("ROLLBACK")
c2.execute("COMMIT")

c2.execute('SELECT * FROM Test;')
print c2.fetchall()