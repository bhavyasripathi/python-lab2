class DatabaseConnection:
  def __init__(self,port,hostname,username, password):
    self.port = port
    self.hostname = hostname
    self.username = username
    self.password = password

   def show_connection(self):
      print("port:",self.port)
      print("Hostname:",self.hostname)
      print("Username:",self.username)
      print("Password: [hidden]")

  db = DatabaseConnection(5432, "localhost", "admin", "demo")
  db.show_connection()
