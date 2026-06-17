import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "../components"

Rectangle {

    color: "#121212"

    GridLayout {

        anchors.fill: parent

        anchors.margins: 20

        columns: 3

        rowSpacing: 15

        columnSpacing: 15

        MetricCard {
            title: "CPU"
            value: "24%"
        }

        MetricCard {
            title: "RAM"
            value: "68%"
        }

        MetricCard {
            title: "Battery"
            value: "81%"
        }

        MetricCard {
            title: "Temperature"
            value: "65°C"
        }

        MetricCard {
            title: "Focus Score"
            value: "82"
        }

        MetricCard {
            title: "Top App"
            value: "VS Code"
        }
    }
}