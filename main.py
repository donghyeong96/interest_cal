product=[]
interest1y=[]
interest2y=[]

choice = 0
while choice !='3':
    choice = input("[관리자 : 1, 고객 : 2, 종료 : 3] 중 선택해주세요 / 선택 : ")
    if choice == '1' :
        adminpw = input('관리자 비밀번호를 입력하세요 : ')

        if adminpw == 'admin' :
            select = 0
            while select !='4':
                select = input('[1 : 상품등록, 2 : 상품수정, 3 : 상품삭제, 4 : 종료] 중 선택해주세요 / 선택 : ')

                if select == '1':
                    x=1
                    while x != 2:
                        product.append(input('신규 생성하는 상품명을 입력하세요 : '))
                        interest1y.append(float(input('해당 상품의 예치기간 1년 기준 이자율을 입력하세요 : ')))
                        interest2y.append(float(input('해당 상품의 예치기간 2년 기준 이자율을 입력하세요 : ')))
                        x = input('계속 등록하시려면 1, 종료하시려면 2를 입력하세요. / 선택 : ')
                        if x == '1' : continue
                        elif x == '2' : 
                            print(product)
                            print('위와 같이 상품이 등록되었습니다.')
                            break
                        else:
                            print('1, 2번 중 선택해주세요.')
                            break
                elif select == '2':
                    update_asispd = input('수정할 상품명을 입력하세요 : ')
                    update_tobepd = input('수정 후의 상품명을 입력하세요 : ')
                    update_tobe1y = float(input('수정 후의 1년 기준 이자율을 입력하세요 : '))
                    update_tobe2y = float(input('수정 후의 2년 기준 이자율을 입력하세요 : '))
                    interest1y[product.index(update_asispd)] = update_tobe1y
                    interest2y[product.index(update_asispd)] = update_tobe2y
                    product[product.index(update_asispd)] = update_tobepd
                    print('상품명 :',update_tobepd,', 1년 이자율 :', update_tobe1y, ', 2년 이자율 :',update_tobe2y)
                    print('위와 같이 상품이 수정되었습니다.')
                elif select == '3':
                    delete = input('삭제할 상품명을 입력하세요: ')
                    del interest1y[product.index(delete)]
                    del interest2y[product.index(delete)]
                    product.remove(delete)
                    print(product)
                    print('상품이 삭제되고 위와 같이 상품목록이 유지됩니다.')
                elif select == '4': break
                else:
                    print('1, 2, 3, 4번 중 선택해주세요.')

        else:
            print('비밀번호가 틀렸습니다!')

    elif choice == '2' :
        custsel = 0
        while custsel !='3':
            custsel = input("[1 : 상품조회, 2 : 이자계산기 실행, 3 : 종료] 중 선택해주세요. / 선택 : ")
            if custsel == '1':
                for i in product:
                    print(product.index(i),'번 - 상품명 : ',(i),', 1년 이자율 : ',interest1y[product.index(i)],', 2년 이자율 : ',interest2y[product.index(i)])
            elif custsel == '2':
                cost = float(input("월 납입금을 입력하세요. / 월 납입금 : "))
                cal_pd = input("이자계산을 원하시는 상품명을 입력하세요. / 상품명 : ")
                cal_int1 = float(interest1y[product.index(cal_pd)])
                cal_int2 = float(interest2y[product.index(cal_pd)])
                print('''1년 예치 기준
                - 원금합계 : ''',round(cost*12),'''원
                - 이자금액 : ''',round(cost*(cal_int1*0.01/12)*(12*(12+1)/2)),'''원
                - 세후 수령액 : ''',round((cost*12)+((cost*(cal_int1*0.01/12)*(12*(12+1)/2))-(cost*(cal_int1*0.01/12)*(12*(12+1)/2))*0.154)),'원'
                )
                print('''2년 예치 기준
                - 원금합계 : ''',round(cost*24),'''원
                - 이자금액 : ''',round(cost*(cal_int1*0.01/24)*(24*(24+1)/2)),'''원
                - 세후 수령액 : ''',round((cost*24)+((cost*(cal_int1*0.01/24)*(24*(24+1)/2))-(cost*(cal_int1*0.01/24)*(24*(24+1)/2))*0.154)),'원'
                )
            elif custsel == '3': break
            else:
                print ('1, 2번 중 선택해주세요.')
    elif choice=='3' : break
    else: print('1, 2번 중 선택해주세요.')


