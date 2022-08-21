import sys
import build

if sys.argv[1] == 'build':
	build.build()
elif sys.argv[1] == 'serve':
	build.build()
	build.serve()
else:
	print("Please either build or serve")