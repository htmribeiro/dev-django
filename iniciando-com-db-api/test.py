from MySQLdb import connect

user = ('USER_NAME')
passwd = ('USER_PASSWORD')
db = ('TARGET_DB')

connect(
  user=user, passwd=passwd, db=db
)
print('Conexão bem sucedida.')
