from qgis.core import Qgis, QgsMessageLog

DEBUG = True


def info(msg, level=Qgis.Info):
    QgsMessageLog.logMessage(str(msg), "VeriVD", level)


def dbg_info(msg: str):
    if DEBUG:
        info(msg)
