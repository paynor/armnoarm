def on_uart_data_received():
    global position, Avalue
    basic.show_string(bluetooth.uart_read_until(serial.delimiters(Delimiters.COLON)))
    if bluetooth.uart_read_until(serial.delimiters(Delimiters.COLON)).includes(":"):
        position = bluetooth.uart_read_until(serial.delimiters(Delimiters.COLON)).index_of("S")
        basic.show_string("" + str(position))
        basic.show_string(bluetooth.uart_read_until(serial.delimiters(Delimiters.COLON)).char_at(position - 1))
        Avalue = parse_float(bluetooth.uart_read_until(serial.delimiters(Delimiters.COLON)).char_at(position - 1))
        if Avalue == 1:
            bluetooth.uart_write_string(":T0T0A1")
        else:
            bluetooth.uart_write_string(":T0R0A0")
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.COLON), on_uart_data_received)

def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

Avalue = 0
position = 0
basic.show_icon(IconNames.SQUARE)
bluetooth.start_uart_service()

def on_forever():
    pass
basic.forever(on_forever)
