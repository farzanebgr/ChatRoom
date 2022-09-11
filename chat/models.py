from django.db import models
from django.contrib.auth.models import User

# Room Table in database / represents a chat room
class Room(models.Model):
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)

    # How many users are online in this chat room?
    def get_online_count(self):
        return self.online.count()

    # Change the online count when the user enters the room.
    def join(self,user):
        self.online.add(user)
        return self.save()

    # Change the online count when the user leaves the room
    def leave(self, user):
        self.online.remove(user)
        return self.save()

    # Display the name of the chat room and the number of users
    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'



# Message Table in database / represents a message sent to the chat room
class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Display the name of user and the content and the time of send content
    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'

