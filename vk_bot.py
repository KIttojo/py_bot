import vk_api
import time
import random
# C:\Users\denis\Desktop\archive

# def function():
# 	pass для оптимизации в будущем
# ca0e63f5c20c05de00361a153f535ae6264f4f0dfd1164134792566b3eb415cd3313eb2444b00013dff5b 

def main():
	VK = vk_api.VkApi(token = '057e5a581e64ca454f9f5e3518e0832d8ae48dfebace6f58418e8faac5ec4c7929a6f042e1ce6a9ed3a07')

	try:
		get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
		get_id_1 = get_chat['items'][0]['last_message']['from_id']
		first_mes_1 = random.randint(100000, 10000000)
		print(VK.method("messages.send", {"random_id": first_mes_1,"user_id": get_id_1, "message": "Для начала работы с ботом напишите в чат !start .В дальнейшем следуйте инструкциям, которые будут даны вам при правильном прохождении этапов мини-квеста"}))

	except:
		print("Imput is empty")
	
	while True:
		get_chat = VK.method("messages.getConversations", { "count": 1, "filter":'unanswered'})
		
		
		try:
			get_id = get_chat['items'][0]['last_message']['from_id']
			now_text = get_chat['items'][0]['last_message']['text']
			first_mes = random.randint(100000, 10000000)
			#тут первое и единственное сообщение со статическим рандом_айди
			# print(VK.method("messages.send", {"random_id": first_mes,"user_id": get_id, "message": "Для начала работы с ботом напишите в чат !start .В дальнейшем следуйте инструкциям, которые будут даны вам при правильном прохождении этапов мини-квеста"}))
			
			if now_text == '!stop': #stopping the code
				return False 

			if now_text == '!start':
				print(VK.method("messages.send", {"random_id": random.randint(100000, 10000000),"user_id": get_id, "message": "Доброго времени суток, путник. Наверное, ты слышал о Cicada 3301, и хотел бы попробовать принять участие в чем-то подобном. У нас есть кое-что простенькое для тебя."}))
				print(VK.method("messages.send", {"random_id": random.randint(100000, 10000000),"user_id": get_id, "message": "Итак, мы начинаем. Первым делом тебе стоит найти в одной из соц. сетей автора подсказку к следующему шагу. Это будет ну очень просто, уверяю."}))
				
			if now_text == 'Zg4rSD':
				print(VK.method("messages.send", {"random_id": random.randint(100000, 10000000),"user_id": get_id, "message": "Поздравленяю, ты победил. Приз - нихуя"}))
			
			time.sleep(5)
			print(mes)
			
		except :
			print("...")

if __name__ == '__main__':
	main()