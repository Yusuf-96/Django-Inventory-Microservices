class AccountRouter(object):
    app_label = "account_service"

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return "account_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return "account_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # db_set = {"account_service"}
        # if obj1._state.db in db_set and obj2._state.db in db_set:
        #     return True
        if (
            obj1._meta.app_label == self.app_label
            or obj2._meta.app_label == self.app_label
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label:
            return db == "account_db"
        return "account_db"
