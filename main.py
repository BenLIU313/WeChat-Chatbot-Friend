from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading
from respond import respond

logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


def on_message(message):
    queue_recved_message.put(message)

INIT=0
MARKET_SUMMARY=1
PROFILE_SYMBOL=2
HOLDERS_SYMBOL=3
FINANCIALS_SYMBOL=4

def thread_handle_message(wx_inst):
    next_state=INIT
    while True:
        message = queue_recved_message.get()
        print(message)
        state =next_state
        if 'msg' in message.get('type'):
            #Analysis information type
            msg_content = message.get('data', {}).get('msg', '')
            send_or_recv = message.get('data', {}).get('send_or_recv', '')
            wxid=message.get('data', {}).get('from_wxid', '')

            if send_or_recv[0] == '0':
                next_state, response = respond(state,msg_content)
                wx_inst.send_text(wxid, response)




def main():
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    wx_inst.start_wechat(block=True)

    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    print(wx_inst.get_myself())
    threading.Thread(target=thread_handle_message, args=(wx_inst,)).start()

    time.sleep(2)
    wx_inst.send_text(to_user='your wx_id', msg='start')
    time.sleep(2)

if __name__ == '__main__':
    main()
