import cv2
import time

# 准备好识别方法
recognizer = cv2.face.LBPHFaceRecognizer_create()

# 使用之前训练好的模型
recognizer.read('lib/trainer.yml')

# 再次调用人脸分类器
cascade_path = "lib/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

id_num = 0
# 设置好与ID号码对应的用户名，如下，如0对应的就是初始
names = ['Person1', 'Person2']

Status = False
Wrong = False
count = 1


def Identify():
	# 调用摄像头
	cam = cv2.VideoCapture(0)
	minW = 0.1 * cam.get(3)
	minH = 0.1 * cam.get(4)
	
	while True:
		ret, img = cam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# 识别人脸
		faces = face_cascade.detectMultiScale(
			gray,
			scaleFactor=1.2,
			minNeighbors=5,
			minSize=(int(minW), int(minH))
		)
		# 进行校验
		
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
			id_num, confidence = recognizer.predict(gray[y:y + h, x:x + w])
			
			# 计算出一个检验结果
			if confidence < 100:
				id_name = names[id_num]
				confidence = "{0}%", format(round(100 - confidence))
				global Status, Wrong, count
				if int(confidence[1]) >= 78:
					print("第"+str(count)+"次认证成功！")
					Status = True
					break
				else:
					print("第"+str(count)+"次认证失败！")
					if not Wrong:
						count += 1
					if count == 6:
						Wrong = True
						break
			else:
				print("识别错误！")
				Wrong = True
				break
		if Status or Wrong:
			break
	# 释放资源
	cam.release()
	cv2.destroyAllWindows()
	return Status

