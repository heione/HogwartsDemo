from study.study_sql.sqldb import SQL
import time
import json

#
# a = SQL.get_instance().run_sql('select * from student')
# time.sleep(10)
# print(a)


def load_json():
    with open('user_info_forserver.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def insert_user():
    data = load_json()
    for type_key in data.keys():
        for user_key in data[type_key].keys():
            user = data[type_key][user_key]
            username = user.get('username')
            pwd = user.get('pwd')
            user_id = user.get('user_id')
            nickname = user.get('nickname')
            birthday = user.get('birthday')
            cert = user.get('cert')
            coin = user.get('coin')
            gold = user.get('gold')
            qiucard = user.get('qiucard')
            realInfo = user.get('realInfo')
            is_bind_mobile = user.get('is_bind_mobile')
            total_master_score = user.get('total_master_score')
            total_score = user.get('total_score')
            vipLevel = user.get('vipLevel')

            sql = f'insert into users ' \
                f'(username, pwd, user_id, nickname, birthday, cert, ' \
                f'coin, gold, qiucard, realInfo, is_bind_mobile, total_master_score, total_score, vipLevel)' \
                f'values ' \
                f'("{username}","{pwd}",{user_id},"{nickname}",{birthday},{cert},{coin},{gold},{qiucard},{realInfo},' \
                f'{is_bind_mobile},{total_master_score},{total_score},{vipLevel})'
            SQL.get_instance().update_sql(sql)


if __name__ == '__main__':
    insert_user()
