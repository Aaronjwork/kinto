#!/usr/bin/env python3
import json, time, os, sys, subprocess, shlex, platform, argparse
from shutil import copyfile
from subprocess import PIPE, Popen
from prekinto import *


log = print


def cmdline(command):
    """执行传入的命令并返回命令的输出"""
    process = Popen(args=command, stdout=PIPE, universal_newlines=True, shell=True)
    return process.communicate()[0]


def check_x11():
    check_x11 = cmdline(
        "(env | grep -i x11 || loginctl show-session \"$XDG_SESSION_ID\" -p Type) | awk -F= '{print $2}'"
    ).strip()

    if len(check_x11) == 0:
        if os.name != "nt":
            print("You are not using x11, please logout and back in using x11/Xorg")
            sys.exit()
        else:
            print("\nYou are detected as running Windows.")
            # windows_setup()
            sys.exit()


def distro_dename():
    distro = (
        cmdline("awk -F= '$1==\"NAME\" { print $2 ;}' /etc/os-release")
        .replace('"', "")
        .strip()
        .split(" ")[0]
    )
    dename = (
        cmdline("./linux/system-config/dename.sh")
        .replace('"', "")
        .strip()
        .split(" ")[0]
        .lower()
    )


def create_kinto_config():
    homedir = os.path.expanduser("~")
    if os.path.isdir(homedir + "/.config/kinto") == False:
        os.mkdir(homedir + "/.config/kinto")
        time.sleep(0.5)


def show_git_info():
    cmdline("git fetch")

    kintover = cmdline(
        'echo "$(git describe --tag --abbrev=0 | head -n 1)" "build" "$(git rev-parse --short HEAD)"'
    )

    print("\nKinto " + kintover + "Type in Linux like it's a Mac.\n")


def call_xkeysnail_service(args):
    if args.uninstall:
        subprocess.check_call(shlex.split("./xkeysnail_service.sh uninstall"))
        exit()
    else:
        subprocess.check_call(shlex.split("./xkeysnail_service.sh"))


def parse_args():
    parser = argparse.ArgumentParser()

    # -r --remove
    parser.add_argument(
        "-r", "--remove", dest="uninstall", 
        action="store_true", help="uninstall kinto"
    )
    
    return parser.parse_args()


def main():
    args = parse_args()
    log("args:", args)
    
    check_x11()
    distro_dename()
    create_kinto_config()
    show_git_info()
    call_xkeysnail_service(args)
    
    
if __name__ == '__main__':
    main()
