# ML/DL에선 수치 데이터 사용
# 학습시키는 훈련 데이터 수 만큼 one-hot encoding기술 적용
# one-hot : 0과 1로 구성된 표현

from sklearn.preprocessing import OneHotEncoder

# test데이터로 library를 활용해서  one-hot으로 변경
def main():
    enc = OneHotEncoder() # 변환가능 객체(학습기)
    
    # 훈련 데이터
    sourcedata = [
        [65], 
        [66], 
        [67], 
        [68]
    ]
    #학습 : fit
    enc.fit(sourcedata)

    # onehotEncoder 객체의 현 상태는 65~68까지의 one-hot encoding 정보 보유

    # 다음에 진행해야할 코드 로직?
    # 1단계 - fit 학습된 내용 확인
    print(enc.transform(sourcedata).toarray())
    '''
    [[1. 0. 0. 0.]
    [0. 1. 0. 0.]
    [0. 0. 1. 0.]
    [0. 0. 0. 1.]]
    '''
    # 2단계 - 새로운 데이터로 Test 진행
    data = [[65], [66], [67], [65], [68]]
    print(enc.transform(data).toarray())
    '''
    ValueError: unknown categorical feature present [69] during transform.
    '''


if __name__ == '__main__' :
    main()