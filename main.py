product=[]
interest1y=[]
interest2y=[]

adminpw = input('관리자 비밀번호를 입력하세요: ')

if adminpw == 'admin' :
    x=1
    while x != 2:
        product.append(input('상품명을 입력하세요 : '))
        interest1y.append(float(input('예치기간 1년 기준 이자율을 입력하세요 : ')))
        interest2y.append(float(input('예치기간 2년 기준 이자율을 입력하세요 : ')))
        x = input('계속 등록하시려면 1, 종료하시려면 2를 입력하세요.')
        if x == '2' : 
            print(product)
            print('위와 같이 상품이 등록되었습니다.')
            break
else:
    print('비밀번호가 틀렸습니다!')