from apis.base import BaseApi


class FipeApi(BaseApi):

    sub_path = ""

    def build_url(self, subpath: str, **kwargs):
        return f"{self.base_url}{subpath}".format(**kwargs)
