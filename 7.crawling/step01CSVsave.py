# 데이터를ㄹ  csv로 저장하기
# 실습단게1 - Do you remember JOIN() function?
    
# 실습단계2 - csv 모듈 사용

# Step01
print('no', 'name', 'age')

# list의 데이터로 csv 구조로 변환
['1', '허준', '60']               
['2', '신사임당', '80']

# 1, 허준, 60으로 나오게 하려면?
print(",".join(['1','허준','60']))
print(",".join(['2','신사임당','80']))

'''
join() function handling every element in table



    history.csv라는 파일에 쓰기
    csv 포맷 작성 후에 new line에 반영
    한글 데이터 들어갔는지 고려해야 함

    한번에 하나의 row만 출력? => 1차원 list
    한번에 다수의 row를 출력? => 2차원 list로 구성 

'''

# step02 - csv 모듈 사용

import csv
with open("history.csv", 'w', newline = '', encoding = 'utf-8 sig') as f:
    #history.csv 파일로 csv작성 가능한 객체화
    #writer 변수로 호출하는 함수는 csv파일로 작성 가능
    writer = csv.writer(f)

    # csv파일의 header 작성
    writer.writerow(['no', 'name', 'age'])
    writer.writerows([
                    ['1', '허준', '60'],
                    ['2', '율곡', '600'],
                    ['3', '이산', '10']
                    ])



























