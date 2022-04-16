import time

# da-keo-giay
time.sleep(1)
print("Trò chơi Oẳn Tù Tì", "v1.0.0")
time.sleep(0.2)
print("nhấn ENTER để tiếp tục")
input(">")
print("nhập /da/ /keo/ /giay/ để chọn Đá,Kéo,Giấy")
input(">")
print("nhập /exit/ để Thoát")
input(">")
print("-"*10+"B-ắ-t-"+"-Đ-ầ-u"+"-"*10)

mayluonthang = 0
while True:
	human = input(">")
	if mayluonthang==7:
		print("bạn bị lừa rồi! máy sẽ luôn thắng ahihi! :)")
		time.sleep(2)
		input("oantutiv1.0.1 comming soon!, nhấn ENTER chơi tiếp")
		for i in range(30): print("error 404!~@#$");time.sleep(0.1)
		for x in range(3,0,-1): print(f"tắt trò chơi sau {x}s", end="\r");time.sleep(1)
		print("bai bai!")
		time.sleep(0.2)
		break
	if mayluonthang%3==1: time.sleep(0.2); print("! "+"try "*(mayluonthang%5)+"!")
	if human=="da":
		mayluonthang += 1
		print("bạn chọn: Đá")
		bot = "giay"
		time.sleep(2)
		print("máy chọn: Giấy")
		time.sleep(1)
		print("--> máy win")
	elif human=="keo":
		mayluonthang += 1
		print("bạn chọn: Kéo")
		bot = "da"
		time.sleep(2)
		print("máy chọn: Đá")
		time.sleep(1)
		print("--> máy win")
	elif human=="giay":
		mayluonthang += 1
		print("bạn chọn: Giấy")
		bot = "keo"
		time.sleep(2)
		print("máy chọn: Kéo")
		time.sleep(1)
		print("--> máy win")
	elif human=="exit":
		print("bai bai!")
		time.sleep(0.2)
		break
	else: continue



