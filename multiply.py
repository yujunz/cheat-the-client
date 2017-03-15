import argparse
import copy
import json
import uuid


class Multiplier:
    def __init__(self, multi=5, list_key='servers', id_key='id', faker=uuid.uuid4):
        self.list_key = list_key
        self.multi = multi
        self.id_key = id_key
        self.faker = faker

    def response(self, flow):
        data = json.loads(flow.response.text)
        sample_list = data[self.list_key]

        craft = self.learn(sample_list)
        for i in range(len(sample_list) * self.multi):
            sample_list.append(craft())

        flow.response.text=json.dumps(data)

    def learn(self, sample_list):
        """TODO: machine learning from actual sample"""
        sample = sample_list[0]
        faker = self.faker

        def _craft():
            """craft a faked artifact"""
            faked = copy.deepcopy(sample)
            faked[self.id_key] = str(faker())
            return faked

        return _craft


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("mul", type=int)
    args = parser.parse_args()
    return Multiplier(multi=args.mul)