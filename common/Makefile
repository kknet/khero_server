
all:
	protoc -I=./ --python_out=../src/msg message.proto
	protoc -I=./ --java_out=./ message.proto

clean:
	rm -rf com/
	rm ../src/msg/message_pb2.py
