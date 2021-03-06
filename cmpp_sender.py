

'''
	cmppSender:发送处理对象，以及接受消息
'''

class cmppSender(object):

	def __init__(self, socketfd, message):
		self.sockFd = socketfd
		self.message = message


	def senderSevice():
		if self.sockFd != 0 and self.message != "":
			cmppNet.sendMsg(sockFd, message)
		else:
			print('socket or message error, sockfd=' + sockFd + 'messsage:' + message)
			return -1
		#接收消息头
		msglen = cmppNet.recvMsg(sockFd, heademsg, 12)
		if msglen == 12:
			bodylen = struct.upack('!I', heademsg[0:4]) - 12
		else:
			print('recv msg header error: headlen = ' + msglen)
			return -1


		bodylen = cmppNet.recvMsg(sockFd, bodymsg, bodylen)
		if bodylen > 0:
			RecvMessage = heademsg + bodymsg
			if len(RecvMessage) > 8:
				recvHeader = cmppHeader(RecvMessage)
				if( recvHeader.getCommandId() == CMPP_CONNECT_RESP):
					connectResp = cmppConnectResp(RecvMessage)
					return connectResp.getStatus()

				elif(recvHeader.getCommandId() == CMPP_SUBMIT_RESP):
					submitResp = cmppSubmitResp(RecvMessage)
					return submitResp.getResult()
					pass
				elif(recvHeader.getCommandId() == CMPP_ACTIVE_TEST):
					activeResp = cmppActiveTestResp(RecvMessage)
					pass
				elif(recvHeader.getCommandId() == CMPP_ACTIVE_TEST_RESP):
					print('the active test resp')
					return 0
				else:
					print('unknow the msg command:' + recvHeader.getCommandId())
					return -1
		else:
			print('recv the message error' + RecvMessage)
			return -1
		

			
