from tortoise import fields, Model


class User(Model):
    user_id = fields.BigIntField(pk=True)
    shop_id = fields.BigIntField()

    def __str__(self):
        return str(self.user_id)


class User_text(Model):
    user = fields.ForeignKeyField('models.User')
    message_rule = fields.TextField(max_length=4000,)
    stop_word = fields.TextField(max_length=4000,)
    otziv = fields.TextField(max_length=4000,)

    def __str__(self):
        return str(self.user)
