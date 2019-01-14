import tensorflow as tf
import numpy as np


# Step03 - 숫자가 3개, 연산식은 +와 *
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

calc1 = a+b*c
calc2 = (a+b)*c

sess = tf.Session()
data1 =  sess.run(calc1)
data2 =  sess.run(calc2)

print(data1, data2)


# Step02 - 숫자 연산
a = tf.constant(123)
b = tf.constant(567)

add_op = a+b

sess = tf.Session()

data = sess.run(add_op)   # session에 있는 run함수 실행
print(data)


# Step01 - API 정상실행하는지 확인

# 문자열로 상수 정의
hello = tf.constant('Hello')

# 세션 시작
sess = tf.Session()

# 실제 실행
print(sess.run(hello))
