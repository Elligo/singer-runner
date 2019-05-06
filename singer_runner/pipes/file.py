from smart_open import smart_open

from singer_runner.pipes.base import BasePipe

class FilePipe(BasePipe):
    def __init__(self, filepath, mode, *args, **kwargs):
        self.filepath = filepath
        self.mode = mode
        kwargs_override = {'encoding': 'utf-8'}
        self.file = smart_open(filepath, mode, **{**kwargs, **kwargs_override})

        super(FilePipe, self).__init__(*args, **{**kwargs, **kwargs_override})

    def close(self):
        super(FilePipe, self).close()
        self.file.close()

    def put(self, raw_singer_message):
        self.file.write(raw_singer_message + b'\n')

    def get(self):
        return self.file.readline()
