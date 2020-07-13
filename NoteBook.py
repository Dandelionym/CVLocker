import src.open as op

status = op.Identify()

if status:
	print("Access!")
else:
	exit(9)

