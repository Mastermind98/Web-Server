# Import socket module
from socket import * 
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
#Fill in start
serverSocket.bind(('localhost',56006))
serverSocket.listen(1)
#Fill in end

while True:
	print('The server is ready to receive')

	connectionSocket, addr = serverSocket.accept() #Fill in start             #Fill in end

	try:
		# Recieve the request
		message = connectionSocket.recv(1024).decode() #Fill in start             #Fill in end

		# Extract the path to the requested file
		filename = message.split()[1]
		
		# read the path from the second character 
		f = open(filename[1:])

		# Read the file "f" and store in a temporary buffer
		outputdata = f.read() #Fill in start             #Fill in end
		
		# send one http header line in to the socket
		#Fill in start
		connectionSocket.send("HTTP/1.0 200 OK".encode())
		#Fill in end
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# close connection
		connectionSocket.close()

	except IOError:
			# Send HTTP response code and message for file not found
			#Fill in start
			connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
			#Fill in end

			# Close the client connection socket
			#Fill in start
			connectionSocket.close()
			#Fill in end
	serverSocket.close()  
	sys.exit() #Terminate the program after sending the corresponding data