bluetooth.onUartDataReceived(serial.delimiters(Delimiters.Colon), function () {
    basic.showString(bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)))
    if (bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)).includes(":")) {
        position = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)).indexOf("S")
        basic.showString("" + (position))
        basic.showString("this".charAt(position - 1))
        Avalue = "this".charAt(position - 1)
        basic.showString(Avalue)
        if (Avalue == 1) {
            bluetooth.uartWriteString(":T0R0A1")
        } else {
            bluetooth.uartWriteString(":T0R0A0")
        }
    }
})
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
let Avalue = ""
let position = 0
basic.showIcon(IconNames.Square)
