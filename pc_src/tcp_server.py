import socket
import requests
import json

def get_position():
	
	r = requests.get('http://127.0.0.1:5000/pozycja_zadana')
	data = json.loads(r.content)
	array = json.loads(data)
	position = int(array['pozycja'])
	#print(position) 
	return position

def post_position(data):
	url = 'http://127.0.0.1:5000/pozycja_aktualna'
	payload = {'pozycja': str(data)}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	return 0

def main():
	

	TCP_IP = '192.168.0.102'
	TCP_PORT = 5005
	BUFFER_SIZE = 20 

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	while 1:
		s.listen(1)

		conn, addr = s.accept()
		print('Connection address:', addr)
		while 1:
			try:
				data = conn.recv(BUFFER_SIZE)
			except:
				break
			if data:
				print("received data:", data)
				#71 = kod ascii litery G
				if data[0] == 71:
					pos = get_position()
					st = str(pos).zfill(3)
					conn.send(st.encode('utf-8')) 
					print("sent data:", st)
				else:
					pos_post = int(data[0:3])
					post_position(pos_post)
		conn.close()
		print('Connection closed')

if __name__ == '__main__':
	main()