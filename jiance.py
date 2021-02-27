from multiprocessing import Process
from send_email import send_email
import socket
import time
def jiesuo():
    print("监听来自手机的socker通信模块启动成功！")
    s = socket.socket()
    host = "192.168.31.95"
    port = 25565
    s.bind((host, port))
    s.listen(5)  # 等待客户端连接
    while True:
        c, addr = s.accept()
        # 有客户端接入了，需要记录接入时间
        print('连接地址：', addr)
        txt_path = "timer.txt"
        with open(txt_path,"w+") as f:
            f.write(str(time.time()))
            f.close()
        c.close()  # 关闭连接

def jiance():
    print ("检测手机两次解锁时间模块运行成功！")
    em = send_email("config/senderinfo.txt","config/tixinginfo.txt")
    er = send_email("config/senderinfo.txt","config/receiverinfo.txt")
    status = 0
    while True:
        txt_path = "timer.txt"
        with open(txt_path,"r+") as f:
            time_data = f.read()
            f.close()
            # 判断是否是第一次运行该程序
        if time_data != "":
            now_time = time.time()
            # 开始判断多久没收到消息了，时间单位是小时
            shijiancha = ((float(now_time) - float(time_data))/60)/60
            # shijiancha = (float(now_time) - float(time_data))
            if shijiancha < 20 and status != 0:
                status = 0
            if shijiancha >= 20 and shijiancha < 22 and status == 0:
                em.send("这是紧急救援系统的提醒消息","config/tixing1.txt")
                print("发送提醒邮件")
                status = 1
            if shijiancha >= 32 and shijiancha < 34 and status == 1:
                em.send("这是紧急救援系统的提醒消息", "config/tixing2.txt")
                print("发送提醒邮件")
                status = 2
            if shijiancha >= 24 and shijiancha < 25.5 and status == 2:
                er.send("您的好友生命正在受到威胁！！！","config/jiuyuan.txt")
                print("发送紧急救援邮件")
                status = 3
            if shijiancha >= 25.5 and shijiancha < 24 * 7 and status == 3:
                er.send("您的好友生命正在受到威胁！！！","config/tixingjiuyuan.txt")
                print("发送提醒救援邮件")
                status = 4
            if shijiancha / 24 == 7 and status == 4:
                er.send("来自您好友的告别邮件","config/end.txt")
                print("发送最后的邮件")
                break

def chushihua():
    # 先将之前运行所产生的时间记录归零
    txt_path = "timer.txt"
    with open(txt_path,"w+") as f:
        f.write("")

def log():
    for n in range(3):
        print ("程序正在启动，请等待",3-n,"秒")
        time.sleep(1)

def run():
    # p1 = Process(target=run,args=("hi",))
    p = Process(target=chushihua)
    plog = Process(target=log)
    p1 = Process(target=jiesuo)
    p2 = Process(target=jiance)
    p.start()
    plog.start()
    time.sleep(5)
    p1.start()
    p2.start()

if __name__ == '__main__':
    run()