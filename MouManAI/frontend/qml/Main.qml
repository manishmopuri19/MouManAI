import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "../components"
import "../pages"

ApplicationWindow {

    visible: true

    width: 1400
    height: 900

    title: "MouMan AI"

    color: "#121212"

    RowLayout {

        anchors.fill: parent

        spacing: 0

        Sidebar {

            Layout.preferredWidth: 220

            onPageSelected: {
                stack.currentIndex = index
            }
        }

        StackLayout {

            id: stack

            Layout.fillWidth: true
            Layout.fillHeight: true

            Dashboard {}
            Activity {}
            SystemHealth {}
            Reports {}
        }
    }
}