import time
from datetime import datetime


def block(start_time,end_time, blocked_sites):
    redirect_url = '127.0.0.1'
    hosts = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    while True:
        if start_time < datetime.now() < end_time:
            print('Доступ ограничен')
            with open(hosts, 'r+') as file:
                src = file.read()
                for site in blocked_sites:
                    if site in src:
                        pass
                    else:
                        file.write(f'{redirect_url} {site}\n')
        else:
            with open(hosts, 'r+') as file:
                src = file.readlines()
                file.seek(0)
                for line in src:
                    if not any(site in line for site in blocked_sites):
                        file.write(line)
                file.truncate()
                print('Доступ открыт')
        time.sleep(5)

def main():
    time1 = int(input('Начало '))
    time2 = int(input('Конец '))
    blocked_sites = ['www.twitch.tv', 'twitch.tv'] 
    start_time = datetime(datetime.now().year,datetime.now().month,datetime.now().day, time1)
    end_time = datetime(datetime.now().year,datetime.now().month,datetime.now().day, time2)
    block(start_time, end_time,blocked_sites)


if __name__ == '__main__':
    main()