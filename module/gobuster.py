import subprocess

class gobuster():

    def dns(target_name, dir_path='/home/ray/work/webscan/SecLists/Discovery/DNS/subdomains-top1million-5000.txt'):
        with subprocess.Popen(['/bin/gobuster', 'dns', '-w', dir_path,
                               '-d', target_name, '-o', f'/home/ray/work/webscan/module/goscan/{target_name}_dns.txt', '-q' ], stdout=subprocess.PIPE) as proc:
            if b'finshed' in proc.stdout.read():
                return 'finshed'
    
    def dir(target_name, dir_path, ext):
        with subprocess.Popen(['/bin/gobuster', 'dir', '-w', dir_path,
                               '-u', target_name, '-o', f'/home/ray/work/webscan/module/goscan/{target_name}_dir.txt', '-q'], stdout=subprocess.PIPE) as proc:
            if b'finshed' in proc.stdout.read():
                proc.kill()
        
#gobuster.dns('test', '/home/ray/work/webscan/SecLists/Discovery/DNS/namelist.txt')