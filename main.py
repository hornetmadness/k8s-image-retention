from libs.config import config
from libs.storage import Storage
from libs.k8s import K8S
import os
from libs.helper_functions import db_find_expired


if __name__ == "__main__":
    # storage = Storage()
    # got = storage.get_db()
    # if not got:
    #     assert("Didnt get DB file")
    #     os.exit(1)

    # from libs.helper_functions import db_upsert as dbup
    # k8s = K8S()
    # images = k8s.get_all_images()
    # dbup(images)

    # storage.put_db()

    # print(db_find_expired(30))

    for uri in db_find_expired(config.registry.expire_age):
        print(uri.uri)




    

