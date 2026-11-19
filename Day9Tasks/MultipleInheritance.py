"""12. Smart Home Devices (Multiple Inheritance)
A smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance."""

class WiFiDevice:
    def __init__(self, network_name):
        self.network_name = network_name
        self.is_connected = False

    def connect_wifi(self):
        self.is_connected = True
        print(f"Connected to WiFi network: {self.network_name}")


class VoiceAssistant:
    def __init__(self, wake_word):
        self.wake_word = wake_word

    def listen_command(self, command):
        print(f"[{self.wake_word}] Executing command: '{command}'")


# SmartSpeaker inherits from both WiFiDevice and VoiceAssistant
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def __init__(self, device_name, network_name, wake_word):
        # Explicitly initialize both parent classes
        WiFiDevice.__init__(self, network_name)
        VoiceAssistant.__init__(self, wake_word)
        self.device_name = device_name

    def device_status(self):
        status = "Online" if self.is_connected else "Offline"
        print(f"Device: {self.device_name} | Status: {status} | Wake Word: '{self.wake_word}'")


# --- Example Usage ---
speaker = SmartSpeaker("Living Room Echo", "Home_WiFi_5G", "Alexa")

speaker.device_status()
speaker.connect_wifi()
speaker.listen_command("Play relaxing jazz")
speaker.device_status()
