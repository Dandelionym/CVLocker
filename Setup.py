if __name__ == '__main__':
	import src.get as get
	# 获取面部信息
	get.Get()
	import src.train as train
	# 训练模型
	train.Train()
	import src.identify as ident
	# 识别
	ident.Identify()
