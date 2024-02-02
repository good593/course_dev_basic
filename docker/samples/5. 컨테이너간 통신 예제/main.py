import pymysql

con = pymysql.connect(host='localhost', user='root', password='pass', charset='utf8') # 한글처리 (charset = 'utf8')

if __name__== "__main__":
  print("Hello World")


