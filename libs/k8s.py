import os
from libs.config import config as myconfig
from libs.helper_functions import unique_list
from kubernetes import client, config
from pprint import pprint
import re

   
class K8S:
    def __init__(self):
        config.load_kube_config()
        self.client = client.CoreV1Api()

    def get_all_images(self):
        try:
            ret = self.client.list_pod_for_all_namespaces(watch=False)
        except:
            assert("Failed to get any pods")

        _images = list()
        for item in ret.items:
            for container in item.spec.containers:
                _images.append( str(container.image) )
        return unique_list(_images)

if __name__ == "__main__":
    k8s = K8S()
    images = k8s.get_all_pods
    # pprint(list(images))
