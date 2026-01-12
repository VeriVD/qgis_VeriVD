from qgis.core import Qgis, QgsMessageLog

DEBUG = True
DEBUG_KEEP_LAYER = False


def info(msg, level=Qgis.MessageLevel.Info):
    QgsMessageLog.logMessage(str(msg), "VeriVD", level)


def dbg_info(msg: str):
    if DEBUG:
        info(msg)
