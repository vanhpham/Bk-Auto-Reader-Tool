import serial.tools.list_ports


def findcom(device):
    devices = {'CAN1': '207138944D4D', 
               'CAN2': '206E38774D4D', 
               'CAN3': '207138664D4D', 
               'CAN4': '206F38854D4D',
               'CAN5': '207038724D4D',
               'esp': "29987",
               'OBD': "A78FQOF5A"}
    ports = serial.tools.list_ports.comports()  
    portnum = None
    for port in ports:
        print(f"Port: {port.device} // {port.hwid} // {port.pid} ")
        if device in devices.keys():  
            if port.serial_number == devices[device] or port.pid == devices[device]:
                portnum = port.device
                break
    return portnum