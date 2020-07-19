import re
s = 1
def pr(i_n):
    a = i_n.split('("', 1)[1]
    b = a.split('")', 1)[0]
    print(b)
def pv (i_n):
    a = i_n.split('(', 1)[1]
    b = a.split(')', 1)[0]
    print(b)
def var(i_n):
    a = i_n.split('(', 1)[1]
    b = a.split(')', 1)[0]
    p = re.compile(r'^['+'.*]')
    ss = re.compile(r'$[' + '.*]')
    sss = ss.findall(b)
    pp = p.findall(b)
    pp = sss
def main_wile(s):
    while True:
        in_put = input("[%d]>" % s)
        in_put_s = list(in_put)
        print(in_put_s)
        s += 1
        in_put_s[0] + in_put_s[1] = in_put_in
        if in_put_in == "pr":
            pr(in_put)
        elif in_put_in == "pv":
            pv(in_put)
        elif in_put_in == "va":
            var(in_put)
main_wile(s)