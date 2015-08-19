from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.structs import ProtocolTreeNode
import cleverbot
import logging
import threading
import json
import traceback

logger = logging.getLogger(__name__)

class YowCleverBotLayer(YowInterfaceLayer):
    def __init__(self):
        super(YowCleverBotLayer, self).__init__()
        self.cb = cleverbot.Cleverbot()

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        self.toLower(messageProtocolEntity.ack())
        if messageProtocolEntity.getType() == TextMessageProtocolEntity.MESSAGE_TYPE_TEXT:
            messageContent = messageProtocolEntity.getBody()
            response = self.cb.ask(messageContent)
            self.toLower(TextMessageProtocolEntity(response, to=messageProtocolEntity.getFrom()))
