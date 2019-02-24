# coding: utf8

import paramiko
import os
import sys
import time
import lib.kmtz_func as f
import colorama

class KMTZ:
    host   = "192.168.1.2" # kmtz
    user   = "root"
    secret = "root"
    port   = 22

    current_img_dir = ""
    left_pic_local  = ""
    right_pic_local = ""

    current_lidar_dir = ""
    lidar_file_local  = ""

    def rotateHeadSlow(self, deg_start, deg_stop, deg_step):

        print("DEG_START:", deg_start)
        print("DEG_STOP:",  deg_stop)
        print("DEG_STEP:",  deg_step)

        deg_start = int(f.SRV_MOTOR_0_DEG + deg_start * f.SRV_MOTOR_1_DEG_STEP)
        deg_stop  = int(f.SRV_MOTOR_0_DEG + deg_stop * f.SRV_MOTOR_1_DEG_STEP)
        deg_step  = int(deg_step * f.SRV_MOTOR_1_DEG_STEP)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.secret, port=self.port)

        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.settimeout(600)

        channel.exec_command('source /etc/profile && cd /media/scripts && ./servo_set_pos.sh ' + str(deg_start) + " " + str(deg_stop) + " " + str(deg_step))

        while(1):
            cout = str(channel.recv(1024), "utf-8")
            if(cout.find("finish") != -1):
                #sys.stdout.write("Rotate pos: %d deg \n" % int(deg_stop))
                break
            else:
                current_pos = filter(str.isdigit, cout)
                if(current_pos):
                    sys.stdout.write("Rotate pos: %d    \r" % (int((int(current_pos) - f.SRV_MOTOR_0_DEG)/f.SRV_MOTOR_1_DEG_STEP)))


        channel.close()
        client.close()


    def srvMotorPwrEn(self, pwr_en=1):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.secret, port=self.port)

        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.settimeout(5)

        pwr_en = pwr_en << 3
        channel.exec_command('source /etc/profile && /media/scripts/gpio.sh ' + str(pwr_en))
        channel.recv(1024)

        channel.close()
        client.close()

    def rotateHead(self, deg_val):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.secret, port=self.port)

        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.settimeout(5)

        deg_val = deg_val*f.SRV_MOTOR_1_DEG_STEP + f.SRV_MOTOR_0_DEG
        channel.exec_command('source /etc/profile && /media/scripts/start_pwm0.sh ' + str(int(deg_val)))
        channel.recv(1024)

        channel.close()
        client.close()

    def getLidarData(self, debug):

        colorama.init()

        lidar_file_remote = '/media/app/cloud.ply'
        self.current_lidar_dir = os.getcwd() + "\\LIDAR\\" + time.strftime("%d.%m.%Y-%H.%M.%S")

        self.lidar_file_local  = self.current_lidar_dir + '/cloud.ply'

        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.user, password=self.secret)
        sftp = paramiko.SFTPClient.from_transport(transport)

        os.makedirs(self.current_lidar_dir)

        if(debug):
            sftp.get(lidar_file_remote, self.lidar_file_local, callback=f.printTotals)
            print("\ncopy lidar file ... done")
            print("lidar file:", colorama.Fore.GREEN + self.lidar_file_local, colorama.Style.RESET_ALL)
        else:
            sftp.get(lidar_file_remote, self.lidar_file_local)

        sftp.close()
        transport.close()

    def lidarScan(self, step_deg, points_count):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.secret, port=self.port)

        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.settimeout(600)
        channel.exec_command('source /etc/profile && cd /media/app && ./lidar.elf')

        while(1):
            cout = str(channel.recv(1024), "utf-8")
            print(cout)
            if(cout.find("command") != -1):
                break

        channel.send("DS\n")
        print(channel.recv(1024))

        while(1):
            cout = str(channel.recv(1024), "utf-8")
            print(cout)
            if(cout.find("set rotate step") != -1):
                break

        channel.send(str(step_deg) + " " + str(points_count) + "\n")

        while(1):
            cout = str(channel.recv(1024), "utf-8")
            print(cout)
            if(cout.find("Read") != -1):
                break

        collisions = 0
        while(1):
            cout = str(channel.recv(1024), "utf-8")

            if(cout.find("COLLISION") != -1):
                collisions += 1

            if(cout.find("start_pwm0.sh") != -1):
                #print cout,
                str_pos = cout.find("start_pwm0.sh") + len("start_pwm0.sh") + 1
                digit_str = cout[str_pos:str_pos + 4]
                current_pos = filter(str.isdigit, digit_str)
                if(current_pos):
                    sys.stdout.write("Rotate pos: %d deg Collisions: %d\r" % (int((int(current_pos) - 560)/4.8333), collisions))

            if(cout.find("Read") != -1):
                #print
                break

        channel.send("Exit\n")

        while(1):
            cout = str(channel.recv(1024), "utf-8")
            print(cout)
            if(str(cout).find("Power disabled") != -1):
                print
                break

        channel.close()
        client.close()


    def takePhoto(self):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.secret, port=self.port)

        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.settimeout(5)
        channel.exec_command('source /etc/profile && cd /media/scripts && ./get_2pics.sh 0')

        while(1):
            cout = str(channel.recv(1024), "utf-8")
            print(cout)
            if(cout.find("finish") != -1):
                print
                break

        channel.close()
        client.close()

    def getCamImage(self, debug):

        left_pic_remote = '/media/outputData/left_0.png'
        right_pic_remote = '/media/outputData/right_0.png'

        self.left_pic_local  = self.current_img_dir + '/cam_left.png'
        self.right_pic_local = self.current_img_dir + '/cam_right.png'

        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.user, password=self.secret)
        sftp = paramiko.SFTPClient.from_transport(transport)

        os.makedirs(self.current_img_dir)

        if(debug):
            sftp.get(left_pic_remote, self.left_pic_local, callback=f.printTotals)
            print("copy cam0 image ... done                     ")
            sftp.get(right_pic_remote, self.right_pic_local, callback=f.printTotals)
            print("copy cam1 image ... done                     ")
        else:
            sftp.get(left_pic_remote, self.left_pic_local)
            sftp.get(right_pic_remote, self.right_pic_local)

        sftp.close()
        transport.close()
