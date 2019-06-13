turn = 1
while turn <4:	
	password = input('請輸入密碼: ')
	if password == 'a12345':
		print('登入成功!')
		break
	else:
		print('密碼錯誤，還有', 3-turn, '次機會。 ')
		turn = turn + 1