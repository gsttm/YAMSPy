from yamspy import MSPy

serial_port = '/dev/tty.usbmodem0x80000001' 
with MSPy(device=serial_port, baudrate=115200,loglevel="DEBUG") as board:
    board.send_MSP_SET_SERVO_CONFIGURATION()
