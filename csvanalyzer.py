import csv
import os
with open('students.csv','r') as f:
    reader =csv.DictReader(f)
    data=list(reader)
average={}
for row in data:
    if row['subject'] not in average:
        average[row['subject']]=[int(row['score'])]
    else:
        average[row['subject']].append(int(row['score']))
average_score={}
for keys in average:
    average_score[keys]=sum(average[keys])/len(average[keys])

print(f'Average subject scores: {average_score}' )

top_scorer= {}
for row in data:
    if row['name'] not in top_scorer:
        top_scorer[row['name']]=int(row['score'])
    else:
        top_scorer[row['name']] += int(row['score'])
        
maxi=0       
for i,j in top_scorer.items():
    if j>maxi:
        maxi=j
        name=i
print(f'Topper:{name}:{maxi}')
summaryx=f'This is the summary the topper was {name} with score of {maxi}. the average subject scores are {average_score}'
with open('summary.txt','w') as f:
    f.write(summaryx)
