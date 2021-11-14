import subprocess

class nmap():
    def allport(target):
        with subprocess.Popen(['/bin/nmap','-sS','-p-',target,'-o',f'nscan/{target}_port.txt'] , stdout=subprocess.PIPE) as proc:
            pass
        return 'finished'