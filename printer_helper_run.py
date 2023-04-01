import os
import time

for i in range(1, 9):
	os.system('rundll32 printui.dll,PrintUIEntry /k /n "HP LaserJet Professional P1102" ')
	time.sleep(3480)  # время задержки выполнения команды os.system() в секундах

	t = time.localtime()
	current_time = time.strftime("%H:%M:%S (%d.%m)", t)
	print(f'Печать тестовой страницы №{i} выполнено в {current_time}')

