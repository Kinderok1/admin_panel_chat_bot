

def get_flag(flag:dict):
    import shelve
    FILENAME = r"C:\Users\павел\PycharmProjects\huita\ololo\bot\bot_api\misc\states2.db"#hardCode
    with shelve.open(FILENAME) as states:
        states["date"] = flag['date']
        states['caption'] = flag['caption']
        states['status'] = flag['status']
        states['pk'] = flag['pk']
        states['descrip'] = flag['descrip']
        states['image'] = flag['image']

def get_flag_msg(flag:dict):
    import shelve
    FILENAME = r"C:\Users\павел\PycharmProjects\huita\ololo\bot\bot_api\misc\states3.db"#hardCode
    with shelve.open(FILENAME) as states:
        states["msg"] = flag['msg']
        states['owner'] = flag['owner']

if __name__ == "__main__":
    get_flag(dict())