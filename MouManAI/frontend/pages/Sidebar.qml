import QtQuick
import QtQuick.Controls

Rectangle {

    width: 220

    color: "#1a1a1a"

    signal pageSelected(int index)

    Column {

        anchors.fill: parent

        anchors.margins: 15

        spacing: 12

        Text {

            text: "MouMan AI"

            color: "white"

            font.pixelSize: 24

            font.bold: true
        }

        Rectangle {
            width: parent.width
            height: 1
            color: "#333333"
        }

        Button {
            text: "Dashboard"
            onClicked: pageSelected(0)
        }

        Button {
            text: "Activity"
            onClicked: pageSelected(1)
        }

        Button {
            text: "System Health"
            onClicked: pageSelected(2)
        }

        Button {
            text: "Reports"
            onClicked: pageSelected(3)
        }
    }
}