import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import sys
import re
import struct
import argparse
from ping3 import ping

def pingFun(ip_address):
    #ping operation
    try:
        print('ip address in ping function',ip_address)
        presult = subprocess.run(["ping",ip_address, "-t", "5"])
        #presult = ping(ip_address,timeout=1)
        print('result',presult)
        print(savefile)
        if presult.returncode == 0:
            if savefile:
                with open(savefile,'a',encoding='gbk') as File:
                    File.write(ip_address+'\n')

    except Exception as e:
        print('exception in pingFun',e)
        #print("Something went wrong with your ping function!")


def tcpFun(ip_port):
    #tcp operation
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    print('certain ip port',ip_port)
    # connect to remote host
    try:
        print('try')
        return_code = s.connect_ex(ip_port)
        #print('tcp connect.',return_code)
    except OSError as e:
        print('OS Error:', e)
    except SocketError as e:  #??
        print('Socket Error:', e)
        
    if return_code == 0:
        #print("Connected.")
        #success_list.append(ip_port[1])
        if savefile:
            with open(savefile,'a',encoding='gbk') as File:
                File.write(ip_port[0]+':'+ip_port[1]+'\n')
    else:
        print('Unable to connect.')

def ping_range(ipaddress_start,ipaddress_end):
    #get the all ip addresses
    try:
        start_num = ipaddress_start.split('.')[-1]
        end_num = ipaddress_end.split('.')[-1]
        start_head = ipaddress_start.rstrip(start_num).rstrip('.')
        ping_list = [start_head + '.' + str(num) for num in range(int(start_num), int(end_num)+1)]
        #print(ping_list)
    except Exception as e:
        print('exception in ping_range',e)
        #print("Something went wrong when you get ip range!")
    return ping_list

def ip2int(addr):
  return struct.unpack("!I", socket.inet_aton(addr))[0]

def validation_ip_range(ipaddr):
    #check the format of ip
    #用正则检查ip地址的正确性
    #print('find::',ipaddr.find('-'))
    if ipaddr.find('-') >=0:
        matchIprange = re.match( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\-'r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ipaddr)

        if matchIprange is None:
            raise ValueError('bad format of ip range')

        Iprange = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(\-)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",ipaddr)
        print('i',Iprange)
        ips = Iprange.groups()
        print('g',ips)
        ip_from = ip2int(ips[0])
        ip_to = ip2int(ips[2])
        if ip_from > ip_to:
            raise ValueError('bad ip range')
        return True

    else:
        #print('ipaddr in validation',ipaddr)
        matchIp = re.match( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ipaddr)
        #print(matchIp)
        if matchIp is None:
            raise ValueError('bad format of ip')
        else:
            return False

def main():
    # global关键字(内部作用域想要对外部作用域的变量进行修改)
    global savefile
    global ip_range_flag
    #print(len(sys.argv[1:]))
    #判断是否有接收到外部传参
    ip_range_flag = False
    if not len(sys.argv[1:]):
        usage()
    '''
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hn:f:i:wv:',
                                   ["help", "nprocess=", "function=", "ipadress=", "writefile="])
    except getopt.GetoptError as a:
        usage()

    print(opts)
    for o, a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-n','--nprocess'):
            processn = int(a)
        elif o in ('-f','--function'):
            operate = a
        elif o in ('-i','--ipadress'):
            ipaddr = a
        elif o in ('-w','--writefile'):
            savefile = a
        elif o in ('-v', '--types'):
            types = a
        else:
            assert ls
        False, "Unhandled Options"
    '''
    try:
        parser = argparse.ArgumentParser(description='opening port probe')
        parser.add_argument('-n', type=int, default=4, help='number of concurrent')
        parser.add_argument('-f', choices=['ping', 'tcp'], default='tcp', help='protocol, ping or tcp')
        parser.add_argument('-ip', type=str, required=True, help='ip range, e.g. 192.168.1.1-192.168.1.128')
        parser.add_argument('-w', type=str, help='write to file')
        parser.add_argument('-m', choices=['proc', 'thread'], default='proc', help='multiprocess or threading', required=False)
        #parser.add_argument('-v', action='count', default=0, help='show elapsed time')
    except Exception as e:
        print(e)

    #get arguments
    args = parser.parse_args()
    print(args)
    processn = args.n
    operate = args.f
    ipaddr = args.ip
    savefile = args.w
    types = args.m

    ping_list = []
    #check ip address format
    ip_range_flag = validation_ip_range(ipaddr)
    if ip_range_flag:
        ipr = ipaddr.split('-')
        ipaddr_from=ipr[0]
        ipaddr_to=ipr[1]
        ping_list = ping_range(ipaddr_from, ipaddr_to)
    else:
        ping_list.append(ipaddr)

    #choose to process type
    if types:
        PoolExecutor = globals()['ThreadPoolExecutor']
    else:
        PoolExecutor = globals()['ProcessPoolExecutor']

    #print('ping_list:',ping_list)
    #choose to operation type
    if operate == 'tcp':

        #tcp_list = [(ipaddr, port) for port in range(0, 65536)]
        tcp_list = [(ipaddr, port) for port in range(0, 100)]
        #print('tcp_list:', tcp_list)
        with PoolExecutor(max_workers=processn) as executor:
            executor.map(tcpFun, tcp_list)

    elif operate == 'ping':
        #print('process number:',processn)
        with PoolExecutor(max_workers=processn) as executor:
            executor.map(pingFun, ping_list)

    else:
        raise Exception('请在-f后输入tcp/ping')    

def usage():
    print("Usage: pmap.py -n [nprocess] -f [function] -v [process] -i [ipaddress] -w [writefile]")
    #print("-n, --nprocess ")
    #print("-f, --function ")
    #print("-i, --ipaddress ")
    #print("-w, --writefile ")
    print("Examples: ")
    print("pmap.py -n 4 -f ping -i 192.168.0.1-192.168.0.100")
    print("pmap.py -n 10 -f tcp -i 192.168.0.1 -w result.json")
    sys.exit(0)

    '''
    命令行参数举例如下：
    pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100

    pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json

    说明：

        因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
        -n：指定并发数量。
        -f ping：进行 ping 测试
        -f tcp：进行 tcp 端口开放、关闭测试。
        -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
        -w：扫描结果进行保存。
    '''

if __name__ == "__main__":
    main()
