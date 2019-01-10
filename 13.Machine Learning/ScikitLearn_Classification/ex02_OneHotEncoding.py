# r, b, y 데이터를 one-hot endcoding하는 프로그램 직접 만들기


from sklearn.preprocessing import OneHotEncoder
# 주소값을 넘겨주고 동일한 객체 참조해 데이터 수정 :  call by reference 

def ordList(charlist):
    for  i, c in enumerate(charlist):     # 자동으로 인덱스 값을 주는 enumerate 함수
        charlist[i] = ord(c)

def main():
    enc = OneHotEncoder() 

    data =[
        ['r'],   # [ord['r]] 로 해도 되긴 한다. 근데 비효율적
        ['b'], 
        ['y']
    ]
    print(data)

    for cc in data:
        ordList(cc)
    enc.fit(data)     # enc.fit(ord(data) )는 리스트를 받아와서 안됨!!
    print(enc.transform(data).toarray())
    '''
    [[114], [98], [121]]
    [[0. 1. 0.]
    [1. 0. 0.]
    [0. 0. 1.]]
    '''

    data2 = [
        ['r'],
        ['b'],
        ['b'],
        ['a'],
        ['y']
    ]
    for cc in data2:
        ordList(cc)
    enc.fit(data2)

    print(enc.transform(data2).toarray())
    '''
    [[0. 0. 1. 0.]
    [0. 1. 0. 0.]
    [0. 1. 0. 0.]
    [1. 0. 0. 0.]
    [0. 0. 0. 1.]]
    '''


    '''
    1. 에러 메세지
        ValueError: could not convert string to float: 'r'
    2. 에러 발생된 사유?
    3. 처리로직
    4. 힌트 : ord(0)
    '''

if __name__ == '__main__' :
    main()