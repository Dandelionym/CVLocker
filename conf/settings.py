import json


class UserInfo(object):
	Info = {}
	Item = []
	PATH = 'license.txt'

	def Write(self, Info):
		with open(self.PATH, mode='w') as f:
			if self.Info is not {}:
				self.Item.append(Info)
			json.dump(self.Item, f)
			f.write('\n')

	def Read(self):
		with open(self.PATH, mode='r') as f:
			result = json.load(f)
			self.Item = [] if result is None else result

	def add_user(self):
		while True:
			name = input("[English] Name: ")
			pwd  = input("[English] PIN : ")
			cfm = input("Sure? (y/n)   : ")
			if cfm in ['y', 'n']:
				if cfm == 'y':
					if (not name.isalpha()) or (not pwd.isascii()):
						print("[Warning] Please check again!")
						continue
					else:
						self.Info[name] = pwd
						print(self.Info)
						break
				if cfm == 'n':
					continue
		self.Write(self.Info)

user = UserInfo()

try:
	user.Read()
except:
	user.add_user()






