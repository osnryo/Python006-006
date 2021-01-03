import sys
import os
import time

'''
手动编写一个daemon程序
'''

def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:
        pid = os.fork()

        if pid > 0:
            # 父进程先于子进程exit,会使子进程变成孤儿进程
            # 这样子进程成功被init这个守护进程收养
            sys.exit(0)

    except OSError as err:
        sys.stderr.write('_Fork #1 failed: {0}\n'.format(err))
        sys.exit(1)

    # 从父进程环境脱离
    # decouple from parent environment
    # chdir确认进程不占用任何目录，否则不能umont
    os.chdir('/') 
    # umask
    os.umask()


def test():

if __name__ == "__main__"
    daemon
