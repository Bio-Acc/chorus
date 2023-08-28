# chorus运行的所有序列并且获得两个轴
import subprocess
import json
import datetime
Y = []
X = []


def get(d: str):
    sum = 0
    with open(d, "r") as f:
        cnt = 0
        for i in f:
            cnt += 1
            if cnt % 2 == 0:
                sum += len(i.strip())
    return sum


for i in range(10, 501, 10):
    subprocess.run(
        f"sh ../Tool/cache.sh".split(" "))
    QUERY = f"../queryForCrossoverPoint/Q_{i}.fa"
    cmd = f"sh /home/wangziyuan/fxw/work/TASK03/chorus/chorus.sh {i}"
    bg = datetime.datetime.now()
    res = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
    ed = datetime.datetime.now()
    X.append(get(QUERY))
    t = (ed - bg).total_seconds()
    Y.append(t)
    print(f"Q_{i}.fa", t)


f2 = open("/home/wangziyuan/fxw/work/TASK03/temp/chorus.log", "w")
f2.write(json.dumps(X))
f2.write("\n")
f2.write(json.dumps(Y))
