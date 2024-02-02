import time
import pymysql

def get_con():
  con = pymysql.connect(host='compose-mysql-db', user='root', password='root1234', charset='utf8') # 한글처리 (charset = 'utf8')
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
  print ("Sleep 5 seconds from now on...")
  time.sleep(5) # mysqldb가 생성될 시간동안 대기.....
  
  print("[Docker Compose][main] Start!!")
  show_databases()
  print("[Docker Compose][main] End!!")

