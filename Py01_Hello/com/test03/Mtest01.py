# -*- coding:utf-8 -*-

def func01():
    print('함수 1 입니다')
    
def func02():
   return '함수 2입니다.'

def func03():
   return {1:'a', 2:'b'}
if __name__ == "__main__":
    #프로그램의 주 진입점
    print('프로그램이 시작되면 가장먼저..')
    func01()
    print(func02())
    print(func03().keys())