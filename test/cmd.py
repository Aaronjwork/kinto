import argparse
from subprocess import PIPE, Popen


log = print

def parse_args():
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-r", dest="uninstall", 
        action="store_true", help="uninstall kinto"
    )
    parser.add_argument(
        "--remove", dest="uninstall", 
        action="store_true", help="uninstall kinto"
    )

    args = parser.parse_args()
    return args


def cmdline(command):
    """"""
    process = Popen(args=command, stdout=PIPE, universal_newlines=True, shell=True)
    # communicate 用于获取命令的输出
    # 返回个元组，第一个元素是stdout，第二个元素是stderr
    return process.communicate()[0]

def cmdline_test():
    cmd = "ls -al"
    cmd = "echo 'sb'"

    log(f"执行命令: {cmd}")
    r = cmdline(cmd)
    log(r, type(r))



def main():
    args = parse_args()
    log("args:", args)


if __name__ == '__main__':
    main()
