from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "sql@2019"
app.config["MYSQL_DATABASE_DB"] = "hybrid"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config['MYSQL_DATABASE_SOCKET'] = None

mysql.init_app(app)