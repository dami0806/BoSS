import pymysql

# Mysql과 연결을 설정하거나 해제합니다.
class ConnectDB:
    
    # conn= pymysql.connect(host='db', user='boss', password='password', db='Boss', charset='utf8', autocommit=True) # docker-compose DB 연결
    # conn= pymysql.connect(host='localhost', user='root', password='password', db='Boss', charset='utf8', autocommit=True) # local DB 연결
    # curs= conn.cursor(pymysql.cursors.DictCursor) # sql문 수행을 위해 cursor 객체를 생성합니다.
    
    # 인스턴스 초기화 
    def __init__(self, sql):
        self.sql= sql # 인스턴스 변수 sql값을 설정합니다.
        self.data = None 
        self.conn= pymysql.connect(host='db', user='boss', password='password', db='Boss', charset='utf8', autocommit=True) # DB와 연결합니다.
        # self.conn= pymysql.connect(host='localhost', user='root', password='password', db='Boss', charset='utf8', autocommit=True) # DB와 연결합니다.
        self.curs= self.conn.cursor(pymysql.cursors.DictCursor) # sql문 수행을 위해 cursor 객체를 생성합니다.
    
    # sql문 실행  
    def execute(self):
        self.curs.execute(self.sql) # sql문 수행합니다.

    # 결과 반환    
    def fetch(self):
        self.data = self.curs.fetchall() # sql결과를 반환합니다.
        # self.data = json.dumps(self.data, ensure_ascii=False, indent=4) # 딕셔너리형 데이터를 json 형식으로 변환합니다.
        return self.data # 결과값을 저장합니다.

    # 인스턴스 삭제 
    def __del__(self):
        self.curs.close # cursor 객체를 닫습니다.
        self.conn.close # DB연결을 해제합니다.
        
        
        
