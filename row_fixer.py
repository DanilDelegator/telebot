from pprint import pprint as pp

# חותמת זמן	כבר טיפל בפנייה	שם מלא	טלפון	מייל	איזור מגורים	עיר מגורים	ניידות? רכב/אופנוע	תחומי התנדבות	האם יש תחום נוסף שהיית רוצה לעזור בו?	ניקוד
MONGO_TO_LOCAL_CSV = {
    # מייל??
    # עיר מגורים??
    '_id': 'טלפון',
    # 'uid': '',
    # 'is_male': '',
    # 'user_type': '',
    'full_name': 'שם מלא',
    'living_area': 'איזור מגורים',
    'mobility': 'ניידות? רכב/אופנוע',
    'volunteer_categories': 'תחומי התנדבות',
    'is_frozen': 'כבר טיפל בפנייה',
    'volunteer_requests': 'האם יש תחום נוסף שהיית רוצה לעזור בו?',
    # 'done_registration': '',
    'first_message_timestamp': 'זמן',
    # 'done_registration_timestamp': '',
    # 'deleted': '',
    # 'current_flow_id': '',
    # 'current_flow_step': '',
    # 'last_message_timestamp': '',
    # 'last_message_retries': '',
    # 'last_message_sent': '',
    # 'last_message': '',
    # 'last_frozen_reminder': '',
    # 'onetime_messages': '',
}


def fix_row(row):
    # print(row)
    res = {}
    for key, value in row.items():
        if key not in MONGO_TO_LOCAL_CSV: continue

        new_key = MONGO_TO_LOCAL_CSV[key]

        if key == '_id':
            res[new_key] = '0' + str(value)[3:]
        elif key == :
            res[new_key] = value

    pp(res)
    print('----')
    return res
