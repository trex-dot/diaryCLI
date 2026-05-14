from collections import Counter
with open('server.log','r') as f:
    lines=f.readlines()
errorlist=[] 
commonip=[]
bussiesthour=[]   
for i in lines:
    parts=i.split()
    if parts[2]=="ERROR":
        errorlist.append(parts[4])
    commonip.append(parts[3])
    hours=parts[1].split(":")
    bussiesthour.append(hours[0])

mostfreqip=Counter(commonip)
commonhour=Counter(bussiesthour)
errors = Counter(errorlist)
most_common_ip = mostfreqip.most_common(1)[0]
print(most_common_ip)
busiest_hour = commonhour.most_common(1)[0]

report = f"""LOG ANALYSIS REPORT
===================
Most Common Errors:
{errors.most_common()}

Most Frequent IP: {most_common_ip[0]} ({most_common_ip[1]} times)

Busiest Hour: {busiest_hour[0]}:00 ({busiest_hour[1]} requests)
"""

print(report)
with open('reporrt.txt', 'w') as f:
    f.write(report)