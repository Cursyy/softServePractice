import subprocess
import datetime

red :str = "\033[91m"
green :str = "\033[92m" 
cyan :str = "\033[96m"

try:
    mysql_user :str = input(cyan + "Write mysql user: ").strip()
    mysql_host :str = input("Write mysql host: ").strip()
    mysql_password :str = input("Write mysql password: ").strip()
    mysql_database :str = input("Write mysql database: ").strip()
except KeyError:
    print(red + "Invalid data")
    exit()

date :str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name :str = f'{mysql_database}_{date}.sql'
command :str = f'mysqldump -u {mysql_user} -p{mysql_password} -h{mysql_host} --no-tablespaces {mysql_database} > {file_name}'

try:
    subprocess.run(command, shell=True)
    print(green + "Dump was created successfuly")
except Exception as e:
    print(red + e)
    print(red + "Dump was not created")
    exit()