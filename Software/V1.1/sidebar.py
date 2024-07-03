from final import *
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog, QFileDialog
from PySide6.QtCore import QThread, Signal, Slot, QMetaObject, Qt, Q_ARG
import threading
import time
import can
from findcom import findcom
from datetime import datetime
import pandas as pd
import os
import can.interfaces.slcan

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BK-Auto Reader Tool")
        self.start_times = {}
        self.onlyicon.setHidden(True)
        self.StatusBar.setCurrentIndex(3)
        self.mainMenu.setCurrentIndex(0)    
        self.connectbut.clicked.connect(self.switch_to_connectionPage)
        self.sendbut.clicked.connect(self.switch_to_sendPage)
        self.snifferbut.clicked.connect(self.switch_to_snifferPage)
        self.diagbut.clicked.connect(self.switch_to_diagPage)
        self.settingbut.clicked.connect(self.switch_to_settingPage)
        self.connectbut_1.clicked.connect(self.switch_to_connectionPage)
        self.sendbut_1.clicked.connect(self.switch_to_sendPage)
        self.snifferbut_1.clicked.connect(self.switch_to_snifferPage)
        self.diagbut_1.clicked.connect(self.switch_to_diagPage)
        self.settingbut_1.clicked.connect(self.switch_to_settingPage)
        self.Stream.clicked.connect(self.stream)
        self.Stream.clicked.connect(self.loaddatatoTable)
        self.Save_seting.clicked.connect(self.Cont_channel_clicked)
        self.Stream_2.clicked.connect(self.send)
        self.Pause.clicked.connect(self.pause_stream)
        self.Save_to_CSV.clicked.connect(self.prepare_save_to_csv)
        self.Stop_Save.clicked.connect(self.stop_save_to_csv)
        self.comboBox.currentIndexChanged.connect(self.loaddatatoTable) 
        
        self.df = {}
        self.df_lock = {}
        self.thread_pool = {}  # Store threads for each channel
        for channel in ["CAN1", "CAN2", "CAN3", "CAN4", "CAN5", "OBD"]:
            self.df[channel] = pd.DataFrame(columns=["timestamp", "dlc", "arbitration_id", "data"])
            self.df_lock[channel] = threading.Lock()
        self.save_threads = []
        self.save_info = {}
        self.stop_saving_event = threading.Event()

    def switch_to_connectionPage(self):
        self.mainMenu.setCurrentIndex(0)
        self.StatusBar.setCurrentIndex(3)

    def switch_to_sendPage(self):
        self.mainMenu.setCurrentIndex(1)
        self.StatusBar.setCurrentIndex(0)

    def switch_to_snifferPage(self):
        self.mainMenu.setCurrentIndex(2)
        self.StatusBar.setCurrentIndex(1)

    def switch_to_diagPage(self):
        self.mainMenu.setCurrentIndex(3)
        self.StatusBar.setCurrentIndex(4)

    def switch_to_settingPage(self):
        self.mainMenu.setCurrentIndex(4)
        self.StatusBar.setCurrentIndex(2)

    def Cont_channel_clicked(self):
        global wait_connect
        wait_connect = {}
        if self.CAN1_tick.isChecked():
            wait_connect["CAN1"] = self.Speed_1.currentText()
        if self.CAN2_tick.isChecked():
            wait_connect["CAN2"] = self.Speed_2.currentText()
        if self.CAN3_tick.isChecked():
            wait_connect["CAN3"] = self.Speed_3.currentText()
        if self.CAN4_tick.isChecked():
            wait_connect["CAN4"] = self.Speed_4.currentText()
        if self.CAN5_tick.isChecked():
            wait_connect["CAN5"] = self.Speed_5.currentText()
        if self.OBD.isChecked():
            wait_connect["OBD"] = None
        comlocation = self.auto_connect()
        print(comlocation)
        print(wait_connect)
        self.OBD.setChecked(False)
        self.CAN1_tick.setChecked(False)
        self.CAN2_tick.setChecked(False)
        self.CAN3_tick.setChecked(False)
        self.CAN4_tick.setChecked(False)
        self.CAN5_tick.setChecked(False)

    def auto_connect(self):
        com_location = {}
        errordevice = []
        for key in wait_connect:
            a = findcom(key)
            if a is not None:
                com_location[key] = a
            else:
                errordevice.append(key)
        if errordevice:
            self.error_message(errordevice)
        return com_location



    def error_message(self, error_device):
        error_devices_str = ', '.join(error_device)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Error")
        msg.setInformativeText(f"Device {error_devices_str} not found")
        msg.setWindowTitle("Error")
        msg.exec()

    def stream(self):
        for channel, rate in wait_connect.items():
            if channel not in self.thread_pool or not self.thread_pool[channel].isRunning():
                with self.df_lock[channel]:
                    self.df[channel] = pd.DataFrame(columns=["timestamp", "dlc", "arbitration_id", "data"])  # Clear the DataFrame
                self.stream_channel(channel, rate)

    def stream_channel(self, channel, rate):
        if channel not in self.thread_pool:
            self.thread_pool[channel] = CanBusThread(channel, rate, self.df, self.df_lock)  # Pass the whole df dictionary
            self.thread_pool[channel].data_received.connect(self.update_table_from_thread) 

        if not self.thread_pool[channel].isRunning(): 
            self.thread_pool[channel].start()
    def update_table_from_thread(self, channel):
        """Slot connected to the data_received signal."""
        # print(f"Updating table from thread, channel: {channel}")
        # with self.df_lock[channel]:
            # print(f"DataFrame for {channel} in update_table_from_thread: \n{self.df[channel]}")
        self.loaddatatoTable() 
    def stream_CAN1(self):
        rate = wait_connect["CAN1"]
        self.thread_CAN1 = CanBusThread("CAN1", rate, self.df["CAN1"], self.df_lock["CAN1"])  
        self.thread_CAN1.data_received.connect(self.loaddatatoTable)
    
        self.thread_CAN1.start()

    def stream_CAN2(self):
        rate = wait_connect["CAN2"]
        self.thread_CAN2 = CanBusThread("CAN2", rate, self.df["CAN2"], self.df_lock["CAN2"])   
        self.thread_CAN2.data_received.connect(self.loaddatatoTable)
        self.thread_CAN2.start()

    def stream_CAN3(self):
        rate = wait_connect["CAN3"]
        self.thread_CAN3 = CanBusThread("CAN3", rate, self.df["CAN3"], self.df_lock["CAN3"])   
        self.thread_CAN3.data_received.connect(self.loaddatatoTable)
        self.thread_CAN3.start()

    def stream_CAN4(self):
        rate = wait_connect["CAN4"]
        self.thread_CAN4 = CanBusThread("CAN4", rate, self.df["CAN4"], self.df_lock["CAN4"])
        self.thread_CAN4.data_received.connect(self.loaddatatoTable)
        self.thread_CAN4.start()

    def stream_CAN5(self):
        rate = wait_connect["CAN5"]
        self.thread_CAN5 = CanBusThread("CAN5", rate, self.df["CAN5"], self.df_lock["CAN5"])
        self.thread_CAN5.data_received.connect(self.loaddatatoTable)
        self.thread_CAN5.start()

    def closeEvent(self, event):
        self.pause_stream()
        self.stop_save_to_csv()
        super().closeEvent(event)

    def send(self):
        if "CAN1" in wait_connect:
            self.send_CAN1()
        if "CAN2" in wait_connect:
            self.send_CAN2()
        if "CAN3" in wait_connect:
            self.send_CAN3()
        if "CAN4" in wait_connect:
            self.send_CAN4()
        if "CAN5" in wait_connect:
            self.send_CAN5()

    def send_CAN1(self):
        rate = wait_connect["CAN1"]
        port = findcom("CAN1")
        if port:
            self.send_thread_CAN1 = SendMsgThread(port, rate, 0.5)
            self.send_thread_CAN1.start()

    def send_CAN2(self):
        rate = wait_connect["CAN2"]
        port = findcom("CAN2")
        if port:
            self.send_thread_CAN2 = SendMsgThread(port, rate, 0.5)
            self.send_thread_CAN2.start()

    def send_CAN3(self):
        rate = wait_connect["CAN3"]
        port = findcom("CAN3")
        if port:
            self.send_thread_CAN3 = SendMsgThread(port, rate, 0.5)
            self.send_thread_CAN3.start()

    def send_CAN4(self):
        rate = wait_connect["CAN4"]
        port = findcom("CAN4")
        if port:
            self.send_thread_CAN4 = SendMsgThread(port, rate, 0.5)
            self.send_thread_CAN4.start()

    def send_CAN5(self):
        rate = wait_connect["CAN5"]
        port = findcom("CAN5")
        if port:
            self.send_thread_CAN5 = SendMsgThread(port, rate, 0.5)
            self.send_thread_CAN5.start()

    def pause_stream(self):
        for channel in self.thread_pool:
            if self.thread_pool[channel].isRunning():
                self.thread_pool[channel].stop()

    def prepare_save_to_csv(self):
        self.save_info.clear()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder to Save Data")
        if not folder_path:
            print("No folder selected for saving CSV.")
            return  

        for channel in wait_connect.keys():
            channel_name, ok = QInputDialog.getText(
                self,
                f"Enter Name for {channel}",
                f"Enter custom name for channel {channel}:",
            )
            if not ok or not channel_name:
                print(f"No name entered for {channel}.")
                return 
            col = list(self.df.keys()).index(channel)
            file_path = os.path.join(folder_path, f"{channel_name}.csv")
            self.save_info[channel] = file_path
            self.tableWidget_3.setItem(0, col, QTableWidgetItem(channel_name))
        self.stop_saving_event.clear()
        # print(f"Starting to save CSV for channels: {self.save_info}")
        self.start_save_to_csv()

    def start_save_to_csv(self):
        self.save_threads = []
        for channel in self.save_info:
            with self.df_lock[channel]:
                self.df[channel] = pd.DataFrame(columns=self.df[channel].columns)
                self.df[channel].reset_index(drop=True, inplace=True)
                self.start_times[channel] = datetime.now()
        for channel, file_path in self.save_info.items():
            save_thread = threading.Thread(target=self.save_to_csv, args=(channel, file_path))
            save_thread.start()
            self.save_threads.append(save_thread)
        # print(f"Save threads started: {self.save_threads}")

    def save_to_csv(self, channel, file_path):
        last_saved_index = 0 # Keep track of the last saved index

        with open(file_path, "w") as f:
            f.write("timestamp,dlc,arbitration_id,data\n")
        # print(f"Saving to CSV at {file_path} for channel: {channel}")

        while not self.stop_saving_event.is_set():
            with self.df_lock[channel]:
                if not self.df[channel].empty:
                    new_rows = self.df[channel].iloc[last_saved_index:] # Get only the new rows
                    # print(f"Writing to CSV for channel: {channel}")
                    new_rows.to_csv(file_path, mode="a", header=False, index=False)
                    last_saved_index = len(self.df[channel]) # Update last saved index
                    self.update_csv_info(channel)
    def update_csv_info(self, channel):
        """Updates the CSV file information table."""
        file_path = self.save_info.get(channel)

        if file_path:
            try:
                # Check if the file exists before accessing attributes
                if os.path.exists(file_path):
                    file_size = os.path.getsize(file_path)
                    file_size_str = f"{file_size} bytes"
                    last_update = datetime.fromtimestamp(os.path.getmtime(file_path))
                    last_update_str = last_update.strftime('%H:%M:%S')

                    # Retrieve the start time
                    start_time = self.start_times.get(channel, None)
                    if start_time:
                        time_elapsed = datetime.now() - start_time
                        time_elapsed_str = str(time_elapsed)
                    else:
                        time_elapsed_str = "Unknown"

                    col = list(self.df.keys()).index(channel)

                    # Use QMetaObject.invokeMethod for thread-safe execution
                    QMetaObject.invokeMethod(
                        self,
                        "_update_csv_table_items",
                        Qt.QueuedConnection,
                        Q_ARG(int, col),
                        Q_ARG(str, file_size_str),
                        Q_ARG(str, file_path),
                        Q_ARG(str, last_update_str),
                        Q_ARG(str, time_elapsed_str)
                    )
                else:
                    print(f"CSV file for {channel} not found: {file_path}")
            except Exception as e:
                print(f"Error updating CSV info: {e}")

    @Slot(int, str, str, str, str)
    def _update_csv_table_items(self, col, file_size_str, file_path, last_update_str, time_elapsed_str):
        """Helper function to update table items (called on the main GUI thread)."""
        if self.tableWidget_3.rowCount() > col:
            self.tableWidget_3.setItem(1, col, QTableWidgetItem(file_size_str))
            self.tableWidget_3.setItem(2, col, QTableWidgetItem(file_path))
            self.tableWidget_3.setItem(3, col, QTableWidgetItem(last_update_str))
            self.tableWidget_3.setItem(4, col, QTableWidgetItem(time_elapsed_str))
        else:
            print(f"Error: Row index {col} out of bounds for tableWidget_3")

    def stop_save_to_csv(self):
        self.stop_saving_event.set()
        for thread in self.save_threads:
            thread.join()
        self.save_threads = []

        # Clear the DataFrames after stopping the save threads




    def loaddatatoTable(self):
        selected_index = self.comboBox.currentIndex()
        selected_channel = self.comboBox.currentText()

        if selected_index == 0: 
            self.tableWidget.setRowCount(0)
            return
        if selected_channel == "All":
            combined_df = pd.DataFrame(columns=["timestamp", "dlc", "arbitration_id", "data", "channel"])
            for channel in self.df:
                with self.df_lock[channel]:
                    temp_df = self.df[channel].copy()
                    temp_df["channel"] = channel
                    combined_df = pd.concat([combined_df, temp_df], ignore_index=True)
            filtered_df = combined_df.sort_values(by="timestamp", ascending=False)
            self._load_df_to_table(filtered_df)
        else:
            with self.df_lock[selected_channel]:
                filtered_df = self.df[selected_channel].copy()
                filtered_df = filtered_df.sort_values(by="timestamp", ascending=False)
                self._load_df_to_table(filtered_df)

    def _load_df_to_table(self, df):
        # print("Loading data to table:")
        # print(df)
        self.tableWidget.setRowCount(0)  # Clear existing rows
        for index, row in df.iterrows():
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            for i, value in enumerate(row):
                self.tableWidget.setItem(rowPosition, i, QTableWidgetItem(str(value)))
            if self.tableWidget.rowCount() > 50:
                self.tableWidget.removeRow(0)
        self.tableWidget.scrollToTop()

class CanBusThread(QThread):
    data_received = Signal(str)   

    def __init__(self, channel, rate, df_dict, df_lock_dict):
        QThread.__init__(self)
        self.stop_event = threading.Event()
        self.channel = channel
        self.rate = rate
        self.df_dict = df_dict
        self.df_lock_dict = df_lock_dict

    def run(self):
        # print(f"Starting CanBusThread for {self.channel} at {self.rate} bps")
        Po = findcom(self.channel)
        start_time = time.time()
        try:
            with can.Bus(interface="slcan", channel=Po, bitrate=int(self.rate)) as server:
                # Directly call receive here
                self.receive(server, start_time)  
        except Exception as e:
            print(f"Exception in CanBusThread for {self.channel}: {e}")

    def receive(self, bus, start_time):
        # print("Start receiving messages")
        while not self.stop_event.is_set():
            try:
                rx_msg = bus.recv(1)
                if rx_msg is not None:
                    timestamp = time.time()
                    timestamp_datetime = datetime.fromtimestamp(timestamp)
                    timestamp_str = timestamp_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')

                    new_row = {
                        "timestamp": timestamp_str,
                        "dlc": rx_msg.dlc,
                        "arbitration_id": rx_msg.arbitration_id,
                        "data": rx_msg.data
                    }

                    # Update the DataFrame using the channel as the key
                    with self.df_lock_dict[self.channel]:
                        self.df_dict[self.channel] = pd.concat([self.df_dict[self.channel], pd.DataFrame([new_row])], ignore_index=True)

                    # print(f"Received message on {self.channel}: {new_row}")
                    # print("Current DataFrame content:")
                    # print(self.df_dict[self.channel]) # Print the specific DataFrame
                    
                    self.data_received.emit(self.channel)  
            except Exception as e:
                print(f"Exception in receive method: {e}")
        # print("Stopped receiving messages")

    @Slot(dict)
    def update_dataframe(self, new_row):
        """Updates the DataFrame on the main thread."""
        new_row_df = pd.DataFrame([new_row])
        with self.df_lock_dict[self.channel]:
            self.df_dict[self.channel] = pd.concat([self.df_dict[self.channel], new_row_df], ignore_index=True)

    def stop(self):
        self.stop_event.set()

class SendMsgThread(QThread):
    def __init__(self, channel, bitrate, freq):
        QThread.__init__(self)
        self.channel = channel
        self.bitrate = bitrate
        self.freq = freq

    def run(self):
        # print(f"Starting SendMsgThread for {self.channel} at {self.bitrate} bps")
        try:
            with can.interface.Bus(channel=self.channel, interface='slcan', bitrate=500000) as bus:
                while True:
                    msg = can.Message(arbitration_id=0x123, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False)
                    try:
                        bus.send(msg)
                        # print("Message sent on {}".format(bus.channel_info))
                        time.sleep(0.000001)
                    except can.CanError:
                        print("Message NOT sent")
        except Exception as e:
            print(f"Exception in SendMsgThread for {self.channel}: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()
