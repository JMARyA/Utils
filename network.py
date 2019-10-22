import subprocess
network = "192.168.1.0/24"
p = subprocess.Popen(["sudo", "nmap", "-v", "-sP", network], stdout=subprocess.PIPE)

def run(cmd):
    cmd = cmd.split(" ")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return p

def getIPS(cmd):
    ips = []
    currentIP = ""
    for l in cmd:
        if ": " in l[1:]:
            print("Interface \"{}\" found".format(l.split(" ")[1][:-1]))
            currentIP = l.split(" ")[1][:-1]
        if "inet" in l:
            try:
                ip = l.split("inet ")[1].split("/")[0]
            except:
                continue
            print("     with IP \"{}\"".format(ip))
            ips.append((currentIP, ip))
    return ips

def choice(choices, default):
    print("")
    for i, e in enumerate(choices):
        print("[{}] {}".format(i, e))
    ch = input("Select one of the options ({}): ".format(default))
    if ch == "":
        return default
    return int(ch)

def scanNetwork():
    p = run("ip addr show eth0")
    p = subprocess.Popen(["ip", "addr"], stdout=subprocess.PIPE)
    array = []
    for l in p.stdout:
        array.append(str(l, encoding="utf-8"))
    array = getIPS(array)
    ch = array[choice(array, 1)]
    ip = ".".join(ch[1].split(".")[:-1])+".1/24"
    print("")
    r = run("sudo nmap -sP {}".format(ip))
    devices = []
    currentDev = ""
    for line in r.stdout:
        line = str(line, encoding="utf-8")
        if "Nmap scan report for " in line:
            hostname = line.split("Nmap scan report for ")[1].split(" ")[0].replace("\n", "")
            try:
                devip = line.split("Nmap scan report for ")[1].split(" (")[1][:-2].replace("\n", "")
            except:
                if len(hostname.split(".")) == 4:
                    devip = hostname
                else:
                    devip = "Error"
        if "MAC Address: " in line:
            macaddr = line.split("MAC Address: ")[1].split(" ")[0].replace("\n", "")
            macvend = line.split("MAC Address: ")[1].split(" (")[1][:-2].replace("\n", "")
            devices.append((hostname, devip, macaddr, macvend))

    for d in devices:
        print("{} ({}) / {} ({})".format(d[0], d[1], d[2], d[3]))


scanNetwork()
