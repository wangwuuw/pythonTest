import pymysql
import sys
from en_decryption import decrypts
sys.path.append("/Users/dfg/PycharmProjects/pythonTest")
from db_config import db_config
def get_conn_to_db(db_name, query_sql):
    global cur
    # db_name_config = config_init(db_name)
    conn = pymysql.connect(**db_config)
    try:
        cur = conn.cursor()
        cur.execute(query_sql)
        row = cur.fetchall()
    except Exception as e:
        print("error" + str(e))
        raise e
    finally:
        cur.close()
    conn.close()
    # print(row)
    return row


def get_conn_to_db2(db_name, query_sql):
    global cur
    db_name_config = config_init(db_name)
    conn = pymysql.connect(**db_name_config)
    try:
        cur = conn.cursor()
        cur.execute(query_sql)
        # row = cur.fetchall()
        conn.commit()
    except Exception as e:
        print("error" + str(e))
        raise e
    finally:
        cur.close()
    conn.close()


sal = 'select user_id,country_of_registered from kyc_institution_infos where use_type="CURRENT"'
a = get_conn_to_db('ui', sal)

for i in range(len(a)):
    if 'AES:' in a[i]['country_of_registered'] :
        ss = decrypts(a[i]['country_of_registered'])
    else:
        ss=a[i]['country_of_registered']
    print(a[i]['country_of_registered'])
    print(ss)
    # insert = "INSERT INTO `ui`.`Statistical country`(`user_Id`, `registerType`, `nationality_list`, `country_of_registered`) VALUES (%i, 'LEGAL_ENTITY', '', '%s')" % (
    # a[i]['user_id'], escape_string(ss))
    #
    # c = get_conn_to_db2('ui', insert)


sql = 'select user_id,nationality_list from kyc_retail_infos where use_type="CURRENT"'
retail = get_conn_to_db('ui', sql)

for i in range(len(retail)):
    if 'AES:' in retail[i]['nationality_list']:

        ss = decrypts(retail[i]['nationality_list'])
    else:
        ss=retail[i]['nationality_list']
    print(retail[i]['nationality_list'])
    print(ss)
    # insert = "INSERT INTO `ui`.`Statistical country`(`user_Id`, `registerType`, `nationality_list`, `country_of_registered`) VALUES (%i, 'INDIVIDUAL', '%s', '')"%(retail[i]['user_id'],escape_string(ss))
    # c = get_conn_to_db2('ui', insert)