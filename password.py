turn = 3
while turn >0:	
	turn = turn-1
	password = input('請輸入密碼: ')
	if password == 'a12345':
		print('登入成功!')
		break
	else:
		if turn >0:
			print('密碼錯誤，還有', turn, '次機會。 ')
		else:
			print('三次輸入錯誤，帳號被鎖。')
		