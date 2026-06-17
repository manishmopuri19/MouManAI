import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

app = QApplication(sys.argv)

engine = QQmlApplicationEngine()

qml_file = Path(__file__).parent / "qml" / "Main.qml"

engine.load(str(qml_file))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())