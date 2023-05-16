from pyparrot.Minidrone import Mambo

mamboAddr = 'e0:14:ba:60:3d:c6'

mambo = Mambo(address = mamboAddr, use_wifi = False)
mambo.smart_sleep(2)
print('Trying to connect mambo')
success = mambo.connect(num_retries = 3)
print(f'Connected: {success}')

mambo.disconnect()

