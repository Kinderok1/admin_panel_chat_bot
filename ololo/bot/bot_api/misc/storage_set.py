

def get_flag(flag:dict):
    import shelve
    FILENAME = r"C:\Users\павел\PycharmProjects\huita\ololo\bot\bot_api\misc\states2.db"
    with shelve.open(FILENAME) as states:
        states["date"] = flag['date']
        states['caption'] = flag['caption']
        states['status'] = flag['status']
        states['pk'] = flag['pk']

def get_flag_msg(flag:dict):
    import shelve
    FILENAME = r"C:\Users\павел\PycharmProjects\huita\ololo\bot\bot_api\misc\states3.db"
    with shelve.open(FILENAME) as states:
        states["msg"] = flag['msg']
        states['owner'] = flag['owner']

if __name__ == "__main__":
    get_flag(dict())