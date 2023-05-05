class Camera:
    def take_photo(self):
        print("take a photo")

    def delete_photo(self):
        print("delete a photo")

    def browse(self):
        print("browse photo album")

class Phone:
    def call(self, number):
        print("calling {}".format(number))

    def send_sms(self, number, message):
        print("sending {} to {}".format(message, number))

class MediaPlayer:
    def play(self, name):
        print("playing a song/video : {}".format(name))

    def browse1(self, liberry):
        print("browse media library : {}".format(liberry))

# class SmartPhone(MediaPlayer, Camera, Phone):
class SmartPhone(Camera, Phone, MediaPlayer):
    def share(self):
        print("share ...")


s = SmartPhone()
s.take_photo()
s.send_sms("1234123", "Hi")
s.play("madi")
s.browse1("music")