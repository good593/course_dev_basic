import pymysql

def get_con():
  con = pymysql.connect(host='mysql-container', user='root', password='pass', charset='utf8') # 한글처리 (charset = 'utf8')

  return con

def show_databases():
  con = None
  cur = None
  try:
    con = get_con();
    cur = con.cursor(pymysql.cursors.DictCursor)
    sql = "show databases"
    cur.execute(sql)

    rows = cur.fetchall()
    print("show databases is >> ")
    print(rows)
  except Exception as e:
    print("Exception > "+str(e))
  finally:
    if cur:
      cur.close()
    if con:
      con.close()

if __name__== "__main__":
  print("[main] Start!!")
  show_databases()
  print("[main] End!!")

