import saver


class Input:
    def add_contact(self):
        user_name = input("Insert the user name => ")
        telephone = input("Insert telephone => ")

        saver.Agenda().saver([user_name, telephone])
