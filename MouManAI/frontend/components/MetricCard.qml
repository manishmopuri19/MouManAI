import QtQuick
import QtQuick.Controls

Rectangle{
    width:220
    height:120
    radius:12
    color:"#1e1e1e"
    border.color:"#333333"
    property string title:""
    property string value:""

    Column{
        anchors.centerIn:parent
        spacing:8
        Text{
            text:title
            color:"#888888"
            font.pixelSize:16
        }
        Text{
            text:value
            color:"white"
            font.pixelSize:28
            font.bold:true
        }
    }
}