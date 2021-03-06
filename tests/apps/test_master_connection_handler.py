from ATE.apps.masterApp.master_connection_handler import MasterConnectionHandler
from ATE.apps.common.connection_handler import ConnectionHandler

PORT = 1883
HOST = '10.9.1.6'
SITE = 0
DEVICEID = "sct01"

SITES = [0, 1, 2]


class Msg:
    def __init__(self):
        self.topic = ""
        self.payload = ""

    def decode(self, dummy):
        return self.payload


class TestApplication:

    def on_control_status_changed(self, siteid, msg):
        self.controlsite = siteid
        self.controlmsg = msg

    def on_testapp_status_changed(self, siteid, msg):
        self.testappsite = siteid
        self.testappmsg = msg

    def on_testapp_testresult_changed(self, siteid, msg):
        pass

    def setup_method(self):
        self.connection_handler = MasterConnectionHandler(HOST,
                                                          PORT,
                                                          SITES,
                                                          DEVICEID,
                                                          self)
        self.controlsite = None
        self.controlmsg = None
        self.testappsite = None
        self.testappmsg = None

    def teardown_method(self):
        self.connection_handler = None
        self.controlsite = None
        self.controlmsg = None
        self.testappsite = None
        self.testappmsg = None

    def test_masterconnhandler_control_status_event_is_dispatched(self):
        msg = Msg()

        msg.topic = "ate/sct01/Control/status/site1"
        msg.payload = "{\"state\" : \"busy\"}"
        self.connection_handler._on_message_handler(None, None, msg)
        assert(self.controlsite == "1")

    def test_masterconnhandler_testapp_Status_event_is_dispatched(self):
        msg = Msg()

        msg.topic = "ate/sct01/TestApp/status/site1"
        msg.payload = "{\"state\" : \"busy\"}"
        self.connection_handler._on_message_handler(None, None, msg)
        assert(self.testappsite == "1")

# ToDo: Implement me!

    # def test_masterconnhandler_sendnext_sends_correct_data(self, mocker):
    #     # spy = mocker.spy(Cls, "method")
    #     # ToDo: Check if the correctly formed message is sent
    #     assert False

    def test_masterconnhandler_sendload_sends_correct_data(self, mocker):
        mocker.patch.object(ConnectionHandler, "publish")
        self.connection_handler.send_load_test_to_all_sites("placeholder_string___this_should_be_a_dict_with_certain_keys_for_a_valid_cmd_payload")
        ConnectionHandler.publish.assert_called_once_with("ate/sct01/Control/cmd", "{\"type\": \"cmd\", \"command\": \"loadTest\", \"testapp_params\": \"placeholder_string___this_should_be_a_dict_with_certain_keys_for_a_valid_cmd_payload\", \"sites\": [0, 1, 2]}", 0, False)

    def test_masterconnhandler_sendterminate_sends_correct_data(self, mocker):
        mocker.patch.object(ConnectionHandler, "publish")
        self.connection_handler.send_terminate_to_all_sites()
        ConnectionHandler.publish.assert_called_once_with("ate/sct01/TestApp/cmd", "{\"type\": \"cmd\", \"command\": \"terminate\", \"sites\": [0, 1, 2]}", 0, False)
