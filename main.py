bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
let Avalue = 0
let position = 0
basic.showIcon(IconNames.Square)
bluetooth.startUartService()
basic.forever(function () {
    if (bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)).includes("S")) {
        position = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)).indexOf("T")
        basic.showString(convertToText(position))
        basic.showString(bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)).charAt(position + 5))
        Avalue = parseFloat(bluetooth.uartReadUntil(serial.delimiters(Delimiters.Colon)).charAt(position + 5))
        if (Avalue == 1) {
            bluetooth.uartWriteString("ACC:T0R0A1")
        } else {
            bluetooth.uartWriteString("ACC:T0R0A0")
        }
    }
})
