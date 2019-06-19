import sys
import os
from tinydb import TinyDB, Query
from pathlib import Path
import datetime

DB_PATH = os.path.join(str(Path.home()),'rememberDB.json')

def main():
    command = sys.argv[1]
    if command == 'this':
        data = ''.join(sys.argv[2::])
        result = insert(data)
    elif command == 'all':
        result = retrieve()
    elif command == 'help':
        result = str(['this','all', 'help'])
    else:
        result = 'wrong command'
    print(result)    

def insert(data):
    current_date = datetime.datetime.now()
    try:
        db = TinyDB(DB_PATH)
        db.insert({'date':str(current_date),'text':data})
        result = f'saved: {data} at {current_date}'
        return result
    except EnvironmentError as error:
        return str(error)
    
def retrieve(criteria=None):
    result = None
    if criteria is not None:
        pass
    else:
        db = TinyDB(DB_PATH)
        result = db.all() 
    return result


if __name__ == "__main__":
    main()