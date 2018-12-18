'''
서로 다른 기종간 호환되는 포맷인  JSON타입으로 변환하는 작업
JSON 사용하는 이유
    : 값 구분이 명확
    : 기기에 종속적이지 않음
    : 모든 언어가 호환되는 포맷
    :  csv보다 더 효율적인 사유는??
        => 고유한 key로 데이터 구분
    : 서버로부터 대량의 데이터를 client가  JASON 포맷으로 많이 사용
    : MongoDB의 데이터 저장 포맷 => json형태
API
    1. python의 list를 JSON형태(객체)로 변환 : dumps()
    2. JSON의 데이터를 python의 데이터로 변환 : loads()

실습단계
    1. 모듈 import
    2. test 데이터 구성
    3. json객체로 변환

고려사항
    1. 한글 데이터 보호(인코딩)
'''

import json

friends = [
            {'f1' : 1, 'name' : '박성백'},
            {'f2' : 2, 'name' : '이이'},
            {'f3' : 3, 'name' : '허준'}
            ]
print(friends[2].values)

with open("friends.json", 'w', encoding='utf-8 sig') as f:
    json.dump(friends, fp=f, ensure_ascii=False) # dump f returns values

# json 확장자 파일로 생성
with open("friends.json", 'w', encoding='utf-8 sig') as f:
    json.dump(friends, fp=f, ensure_ascii=False) # dump f returns values


# list를 json객체로 변환해 보기
jsonData = json.dumps(friends, ensure_ascii=False)
print(jsonData)

jsonData = json.dumps(friends, ensure_ascii=False, indent=10) # one indent parameter applying four spaces
print(jsonData)

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))







