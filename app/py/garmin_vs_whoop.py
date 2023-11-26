from garmin_fit_sdk import Decoder, Stream


def generate_garmin_whoop_graphs():
    pass


class GarminData:
    def __init__():
        stream = Stream.from_file("Activity.fit")
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        print(errors)
        print(messages)
