
import datetime
import csv
import locale




distance=input('距離は?')
time=input('タイムは？')
timeline=input('走った時間帯は？')
pace=input('ペースは？')
span=input('前回と何日あけた?')
condition=input('コンディションは？')
wheather=input('天気は？')
comment=input('感想は？')


dt_now=datetime.datetime.now()
dt=dt_now.strftime('%Y年%m月%d日')
weekday=dt_now.strftime('%A')



with open('rundiary.csv','a') as f:
    writer = csv.writer(f)
    #次の行は初回登録のみ。２回目以降の登録時はコメントアウト！！
    writer.writerow(['日付','曜日','距離','タイム','ペース','スパン','コンディション','感想'])
    writer.writerow([str(dt),str(weekday),str(distance),str(time),str(pace),str(span),str(condition),str(comment)])
    f.close()